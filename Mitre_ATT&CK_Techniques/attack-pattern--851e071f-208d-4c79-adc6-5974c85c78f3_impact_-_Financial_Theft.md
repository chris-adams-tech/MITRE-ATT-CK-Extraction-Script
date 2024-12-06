---
contributors:
- Blake Strom, Microsoft Threat Intelligence
- Pawel Partyka, Microsoft Threat Intelligence
- Menachem Goldstein
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--851e071f-208d-4c79-adc6-5974c85c78f3
mitre_attack_url: https://attack.mitre.org/techniques/T1657
name: Financial Theft
platforms:
- Linux
- macOS
- Windows
- SaaS
- Office Suite
tactics:
- impact
title: impact - Financial Theft
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows, SaaS, Office Suite |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1657](https://attack.mitre.org/techniques/T1657) |

# Financial Theft (attack-pattern--851e071f-208d-4c79-adc6-5974c85c78f3)

## Description
Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,(Citation: FBI-ransomware) business email compromise (BEC) and fraud,(Citation: FBI-BEC) "pig butchering,"(Citation: wired-pig butchering) bank hacking,(Citation: DOJ-DPRK Heist) and exploiting cryptocurrency networks.(Citation: BBC-Ronin) 

Adversaries may [Compromise Accounts](https://attack.mitre.org/techniques/T1586) to conduct unauthorized transfers of funds.(Citation: Internet crime report 2022) In the case of business email compromise or email fraud, an adversary may utilize [Impersonation](https://attack.mitre.org/techniques/T1656) of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary.(Citation: FBI-BEC) This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.(Citation: VEC)

Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) (Citation: NYT-Colonial) and [Exfiltration](https://attack.mitre.org/tactics/TA0010) of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary.(Citation: Mandiant-leaks) Adversaries may use dedicated leak sites to distribute victim data.(Citation: Crowdstrike-leaks)

Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as [Data Destruction](https://attack.mitre.org/techniques/T1485) and business disruption.(Citation: AP-NotPetya)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1657)
- [VEC](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.)
- [Crowdstrike-leaks](https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/)
- [Mandiant-leaks](https://www.mandiant.com/resources/blog/ransomware-extortion-ot-docs)
- [DOJ-DPRK Heist](https://www.justice.gov/usao-cdca/pr/3-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyber-attacks-and)
- [FBI-BEC](https://www.fbi.gov/file-repository/fy-2022-fbi-congressional-report-business-email-compromise-and-real-estate-wire-fraud-111422.pdf/view)
- [FBI-ransomware](https://www.cisa.gov/sites/default/files/Ransomware_Trifold_e-version.pdf)
- [AP-NotPetya](https://apnews.com/article/russia-ukraine-technology-business-europe-hacking-ce7a8aca506742ab8e8873e7f9f229c2)
- [Internet crime report 2022](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf)
- [BBC-Ronin](https://www.bbc.com/news/technology-60933174)
- [wired-pig butchering](https://www.wired.com/story/pig-butchering-fbi-ic3-2022-report/)
- [NYT-Colonial](https://www.nytimes.com/2021/05/13/technology/colonial-pipeline-ransom.html)
