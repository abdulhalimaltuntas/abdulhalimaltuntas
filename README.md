<!--
  GitHub profile README — github.com/abdulhalimaltuntas
  Special repository: must be named exactly "abdulhalimaltuntas".
  The hero banner is a hand-written animated SVG in assets/ — no third-party
  service, so it keeps working even if the badge providers go down.
-->

<div align="center">

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/hero.svg" alt="Abdulhalim Altuntaş — Web Application Pentester" width="100%">

<br>

<a href="https://github.com/abdulhalimaltuntas">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1200&color=9B8CFF&center=true&vCenter=true&width=760&height=42&lines=Mapping+attack+surface+before+touching+a+single+payload;Broken+access+control+%C2%B7+injection+%C2%B7+SSRF+%C2%B7+auth+flaws;Chaining+low-severity+bugs+into+something+that+matters;Writing+the+tool+when+the+existing+one+falls+short" alt="">
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=abdulhalimaltuntas&label=PROFILE+VIEWS&color=9b8cff&style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/FOCUS-WEB%20%26%20API-3DDC97?style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/SCOPE-AUTHORIZED%20ONLY-E8A33D?style=for-the-badge" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/whoami`

```console
$ id --pentester

  role     Web application penetration tester
  hunting  Broken access control · IDOR/BOLA · injection · SSRF
           Authentication & session flaws · business logic abuse
  method   Map the surface first, then chain what looks harmless.
           Impact is the argument — everything else is trivia.
  writing  Reports a developer can actually act on.
  rule     Written authorization, always. No exceptions.
```

The interesting bug is rarely the one the scanner finds. It is the endpoint that never made it into the docs, the object id nobody thought to check, the third-party script quietly executing on a checkout page. I map the whole surface first, then work the seams — and when the tool I need does not exist, I build it.

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/methodology`

<div align="center">

| `01` | `02` | `03` | `04` | `05` |
|:---:|:---:|:---:|:---:|:---:|
| **SCOPE** | **MAP** | **PROBE** | **CHAIN** | **REPORT** |
| Authorization<br>and boundaries | Assets, endpoints,<br>parameters, JS surface | Access control,<br>injection, auth, logic | Low severity → <br>real impact | Reproducible,<br>fixable, prioritised |

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/arsenal`

<div align="center">

### Recon & attack-surface mapping

![Nmap](https://img.shields.io/badge/Nmap-2E5E8C?style=for-the-badge&logo=nmap&logoColor=white)
![Amass](https://img.shields.io/badge/Amass-1B5E20?style=for-the-badge&logoColor=white)
![subfinder](https://img.shields.io/badge/subfinder-6D5BD0?style=for-the-badge&logoColor=white)
![httpx](https://img.shields.io/badge/httpx-6D5BD0?style=for-the-badge&logoColor=white)
![katana](https://img.shields.io/badge/katana-6D5BD0?style=for-the-badge&logoColor=white)
![ffuf](https://img.shields.io/badge/ffuf-1E1E1E?style=for-the-badge&logoColor=white)
![gobuster](https://img.shields.io/badge/gobuster-1E1E1E?style=for-the-badge&logoColor=white)
![waybackurls](https://img.shields.io/badge/waybackurls-37474F?style=for-the-badge&logoColor=white)
![Shodan](https://img.shields.io/badge/Shodan-C0392B?style=for-the-badge&logo=shodan&logoColor=white)

### Web & API testing

![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP%20ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Nuclei](https://img.shields.io/badge/Nuclei-9B8CFF?style=for-the-badge&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![DevTools](https://img.shields.io/badge/DevTools-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)

### Exploitation & post-exploitation

![sqlmap](https://img.shields.io/badge/sqlmap-B71C1C?style=for-the-badge&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white)
![XSStrike](https://img.shields.io/badge/XSStrike-AD1457?style=for-the-badge&logoColor=white)
![Hydra](https://img.shields.io/badge/Hydra-455A64?style=for-the-badge&logoColor=white)
![Hashcat](https://img.shields.io/badge/Hashcat-37474F?style=for-the-badge&logoColor=white)
![John](https://img.shields.io/badge/John%20the%20Ripper-37474F?style=for-the-badge&logoColor=white)

### Network & analysis

![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-455A64?style=for-the-badge&logoColor=white)
![mitmproxy](https://img.shields.io/badge/mitmproxy-8E24AA?style=for-the-badge&logoColor=white)
![OpenVPN](https://img.shields.io/badge/OpenVPN-EA7E20?style=for-the-badge&logo=openvpn&logoColor=white)

### Build & automate

<img src="https://skillicons.dev/icons?i=python,js,bash,linux,docker,git,github,nodejs,html,css,mysql,vscode&theme=dark&perline=12" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/stats`

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=abdulhalimaltuntas&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&bg_color=0D1117&title_color=9B8CFF&text_color=9AA5BA&icon_color=3DDC97&ring_color=9B8CFF" alt="">
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=abdulhalimaltuntas&layout=compact&hide_border=true&langs_count=8&bg_color=0D1117&title_color=9B8CFF&text_color=9AA5BA" alt="">

<br><br>

<img src="https://streak-stats.demolab.com?user=abdulhalimaltuntas&hide_border=true&background=0D1117&stroke=232C3A&ring=9B8CFF&fire=E8A33D&currStreakLabel=9B8CFF&sideLabels=9AA5BA&dates=67718A&currStreakNum=E7ECF5&sideNums=E7ECF5" alt="">

<br><br>

<img src="https://github-profile-trophy.vercel.app/?username=abdulhalimaltuntas&theme=darkhub&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8" alt="">

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=abdulhalimaltuntas&bg_color=0D1117&color=9B8CFF&line=3DDC97&point=E8A33D&area=true&area_color=6D5BD0&hide_border=true&radius=8" width="100%" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/contributions`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake.svg">
</picture>

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/contact`

<div align="center">

<a href="mailto:altuntashalim123@gmail.com">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
</a>
<a href="https://instagram.com/halimaltuntas33">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a>
<a href="https://github.com/abdulhalimaltuntas">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

<br><br>

<sub>Every engagement shown or discussed here runs against systems I own or hold written authorization to test.</sub>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9B8CFF,50:6D5BD0,100:0B0E14&height=130&section=footer" width="100%" alt="">

</div>
