<!--
  GitHub profil README'si — Turkce surum.
  Ana surum README.md; ikisi de assets/ altindaki elle yazilmis animasyonlu
  SVG'leri kullanir.
-->

<div align="center">

[English](README.md) · **Türkçe**

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/hero.svg" alt="Abdulhalim Altuntaş — Web Uygulama Sızma Testi Uzmanı" width="100%">

<br>

<a href="https://github.com/abdulhalimaltuntas">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1200&color=9B8CFF&center=true&vCenter=true&width=760&height=42&lines=Tek+bir+payload+denemeden+%C3%B6nce+y%C3%BCzeyi+haritalarim;Yetkilendirme+%C2%B7+enjeksiyon+%C2%B7+SSRF+%C2%B7+kimlik+do%C4%9Frulama;K%C3%BC%C3%A7%C3%BCk+bulgulari+zincirleyip+ger%C3%A7ek+etkiye+%C3%A7eviririm;Arac+yoksa+kendim+yazarim" alt="">
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=abdulhalimaltuntas&label=PROF%C4%B0L+G%C3%96R%C3%9CNT%C3%9CLENME&color=9b8cff&style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/ODAK-WEB%20%26%20API-3DDC97?style=for-the-badge" alt="">
<img src="https://img.shields.io/badge/KAPSAM-YALNIZCA%20YETK%C4%B0L%C4%B0-E8A33D?style=for-the-badge" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/kimim`

```console
$ id --pentester

  rol       Web uygulama sızma testi uzmanı
  avlanma   Kırık erişim kontrolü · IDOR/BOLA · enjeksiyon · SSRF
            Kimlik doğrulama ve oturum açıkları · iş mantığı istismarı
  yöntem    Önce yüzeyi haritala, sonra zararsız görüneni zincirle.
            Argüman etkidir — gerisi teferruat.
  raporlama Geliştiricinin gerçekten uygulayabileceği raporlar.
  kural     Her zaman yazılı yetki. İstisnasız.
```

İlgi çekici zafiyet, nadiren tarayıcının bulduğudur. Asıl olan; dokümantasyona hiç girmemiş endpoint, kimsenin kontrol etmeyi akıl etmediği nesne kimliği, ödeme sayfasında sessizce çalışan üçüncü taraf script'idir. Önce tüm yüzeyi çıkarır, sonra dikiş yerlerinde çalışırım — ihtiyacım olan araç yoksa yazarım.

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/metodoloji`

<div align="center">

| `01` | `02` | `03` | `04` | `05` |
|:---:|:---:|:---:|:---:|:---:|
| **KAPSAM** | **HARİTALA** | **SINA** | **ZİNCİRLE** | **RAPORLA** |
| Yetki ve<br>sınırların tespiti | Varlıklar, endpoint'ler,<br>parametreler, JS yüzeyi | Erişim kontrolü, enjeksiyon,<br>kimlik doğrulama, mantık | Düşük önem →<br>gerçek etki | Tekrarlanabilir,<br>düzeltilebilir, önceliklendirilmiş |

<br>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/terminal.svg" alt="Recon zinciri: subfinder, httpx, ffuf ve nuclei — sonunda zincirlenmiş bir bulgu" width="100%">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/kapsam`

<div align="center">

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/owasp.svg" alt="OWASP Top 10 2021 — kategori bazında çalışma derinliği" width="100%">

<br><br>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/focus.svg" alt="Bir testte zamanın recon, test, araç geliştirme ve raporlama arasındaki dağılımı" width="100%">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/cephanelik`

<div align="center">

### Keşif & saldırı yüzeyi haritalama

![Nmap](https://img.shields.io/badge/Nmap-2E5E8C?style=for-the-badge&logo=nmap&logoColor=white)
![Amass](https://img.shields.io/badge/Amass-1B5E20?style=for-the-badge&logoColor=white)
![subfinder](https://img.shields.io/badge/subfinder-6D5BD0?style=for-the-badge&logoColor=white)
![httpx](https://img.shields.io/badge/httpx-6D5BD0?style=for-the-badge&logoColor=white)
![katana](https://img.shields.io/badge/katana-6D5BD0?style=for-the-badge&logoColor=white)
![ffuf](https://img.shields.io/badge/ffuf-1E1E1E?style=for-the-badge&logoColor=white)
![gobuster](https://img.shields.io/badge/gobuster-1E1E1E?style=for-the-badge&logoColor=white)
![waybackurls](https://img.shields.io/badge/waybackurls-37474F?style=for-the-badge&logoColor=white)
![Shodan](https://img.shields.io/badge/Shodan-C0392B?style=for-the-badge&logo=shodan&logoColor=white)

### Web & API testi

![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP%20ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Nuclei](https://img.shields.io/badge/Nuclei-9B8CFF?style=for-the-badge&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![DevTools](https://img.shields.io/badge/DevTools-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)

### İstismar & sonrası

![sqlmap](https://img.shields.io/badge/sqlmap-B71C1C?style=for-the-badge&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white)
![XSStrike](https://img.shields.io/badge/XSStrike-AD1457?style=for-the-badge&logoColor=white)
![Hydra](https://img.shields.io/badge/Hydra-455A64?style=for-the-badge&logoColor=white)
![Hashcat](https://img.shields.io/badge/Hashcat-37474F?style=for-the-badge&logoColor=white)
![John](https://img.shields.io/badge/John%20the%20Ripper-37474F?style=for-the-badge&logoColor=white)

### Ağ & analiz

![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-455A64?style=for-the-badge&logoColor=white)
![mitmproxy](https://img.shields.io/badge/mitmproxy-8E24AA?style=for-the-badge&logoColor=white)
![OpenVPN](https://img.shields.io/badge/OpenVPN-EA7E20?style=for-the-badge&logo=openvpn&logoColor=white)

### Geliştirme & otomasyon

<img src="https://skillicons.dev/icons?i=python,js,bash,linux,docker,git,github,nodejs,html,css,mysql,vscode&theme=dark&perline=12" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/istatistik`

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=abdulhalimaltuntas&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&locale=tr&bg_color=0D1117&title_color=9B8CFF&text_color=9AA5BA&icon_color=3DDC97&ring_color=9B8CFF" alt="">
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=abdulhalimaltuntas&layout=compact&hide_border=true&langs_count=8&locale=tr&bg_color=0D1117&title_color=9B8CFF&text_color=9AA5BA" alt="">

<br><br>

<img src="https://streak-stats.demolab.com?user=abdulhalimaltuntas&locale=tr&hide_border=true&background=0D1117&stroke=232C3A&ring=9B8CFF&fire=E8A33D&currStreakLabel=9B8CFF&sideLabels=9AA5BA&dates=67718A&currStreakNum=E7ECF5&sideNums=E7ECF5" alt="">

<br><br>

<img src="https://github-profile-trophy.vercel.app/?username=abdulhalimaltuntas&theme=darkhub&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8" alt="">

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=abdulhalimaltuntas&bg_color=0D1117&color=9B8CFF&line=3DDC97&point=E8A33D&area=true&area_color=6D5BD0&hide_border=true&radius=8" width="100%" alt="">

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/katkilar`

<div align="center">

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/profile-3d-contrib/profile-night-rainbow.svg" alt="İzometrik 3B katkı grafiği" width="100%">

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake.svg">
  <img alt="Katkı yılanı" src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/output/snake.svg">
</picture>

</div>

<img src="https://raw.githubusercontent.com/abdulhalimaltuntas/abdulhalimaltuntas/main/assets/divider.svg" width="100%" alt="">

## `~/iletisim`

<div align="center">

<a href="mailto:altuntashalim123@gmail.com">
  <img src="https://img.shields.io/badge/E--posta-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="E-posta">
</a>
<a href="https://instagram.com/halimaltuntas33">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a>
<a href="https://github.com/abdulhalimaltuntas">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

<br><br>

<sub>Burada gösterilen ve anlatılan tüm çalışmalar, sahibi olduğum ya da test etmek için yazılı yetki aldığım sistemler üzerinde yürütülür.</sub>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9B8CFF,50:6D5BD0,100:0B0E14&height=130&section=footer" width="100%" alt="">

</div>
