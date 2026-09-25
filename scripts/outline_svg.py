#!/usr/bin/env python3
"""Build portable SVG artwork with font outlines instead of installed-font dependencies.

Requires fontTools. Editable input is kept in assets/src; generated assets live in assets.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)


def number(value):
    return f'{value:.3f}'.rstrip('0').rstrip('.') or '0'


class Typography:
    def __init__(self, display_font, mono_font):
        self.fonts = {'display': TTFont(display_font), 'mono': TTFont(mono_font)}
        self.glyph_sets = {}

    def outline(self, element):
        family = element.get('font-family', '')
        font_key = 'mono' if 'Mono' in family else 'display'
        font = self.fonts[font_key]
        weight = float(element.get('font-weight', '400'))
        key = (font_key, weight)
        if key not in self.glyph_sets:
            axes = {axis.axisTag for axis in font['fvar'].axes} if 'fvar' in font else set()
            location = {'wght': weight} if 'wght' in axes else None
            self.glyph_sets[key] = font.getGlyphSet(location=location)
        glyphs = self.glyph_sets[key]
        cmap = font.getBestCmap()
        scale = float(element.get('font-size', '16')) / font['head'].unitsPerEm
        tracking = float(element.get('letter-spacing', '0').removesuffix('px'))
        label = ''.join(element.itertext())
        sequence = []
        for character in label:
            if ord(character) not in cmap:
                raise ValueError(f'{font_key} font lacks {character!r} in {label!r}')
            name = cmap[ord(character)]
            sequence.append((name, glyphs[name].width * scale))
        width = sum(advance for _, advance in sequence) + max(0, len(sequence) - 1) * tracking
        x = float(element.get('x', '0'))
        y = float(element.get('y', '0'))
        anchor = element.get('text-anchor', 'start')
        if anchor == 'middle':
            x -= width / 2
        elif anchor == 'end':
            x -= width
        pen = SVGPathPen(glyphs, ntos=number)
        for name, advance in sequence:
            glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
            x += advance + tracking
        excluded = {'x', 'y', 'font-family', 'font-size', 'font-weight', 'letter-spacing', 'text-anchor'}
        attributes = {key: value for key, value in element.attrib.items() if key not in excluded}
        attributes.update({'d': pen.getCommands(), 'aria-label': label, 'role': 'img'})
        replacement = ET.Element(f'{{{SVG}}}path', attributes)
        replacement.tail = element.tail
        return replacement

    def build(self, source, output):
        tree = ET.parse(source)
        for parent in list(tree.iter()):
            for index, child in enumerate(list(parent)):
                if child.tag == f'{{{SVG}}}text':
                    if list(child):
                        raise ValueError(f'Use separate text nodes instead of tspan: {source}')
                    parent.remove(child)
                    parent.insert(index, self.outline(child))
        output.write_text(ET.tostring(tree.getroot(), encoding='unicode') + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--display-font', type=Path, required=True, help='Space Grotesk TTF file')
    parser.add_argument('--mono-font', type=Path, required=True, help='JetBrains Mono TTF file')
    parser.add_argument('--source', type=Path, default=Path('assets/src'))
    parser.add_argument('--output', type=Path, default=Path('assets'))
    args = parser.parse_args()
    typography = Typography(args.display_font, args.mono_font)
    args.output.mkdir(parents=True, exist_ok=True)
    for source in sorted(args.source.glob('*.svg')):
        target = args.output / source.name
        typography.build(source, target)
        print(f'{source} -> {target} ({target.stat().st_size // 1024} KiB)')


if __name__ == '__main__':
    main()
