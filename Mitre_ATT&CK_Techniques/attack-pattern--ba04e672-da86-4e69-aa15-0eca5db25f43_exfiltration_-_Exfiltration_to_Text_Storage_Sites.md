---
contributors:
- "Harun K\xFC\xDFner"
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--ba04e672-da86-4e69-aa15-0eca5db25f43
mitre_attack_url: https://attack.mitre.org/techniques/T1567/003
name: Exfiltration to Text Storage Sites
platforms:
- Linux
- macOS
- Windows
tactics:
- exfiltration
title: exfiltration - Exfiltration to Text Storage Sites
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1567/003](https://attack.mitre.org/techniques/T1567/003) |

# Exfiltration to Text Storage Sites (attack-pattern--ba04e672-da86-4e69-aa15-0eca5db25f43)

## Description
Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as <code>pastebin[.]com</code>, are commonly used by developers to share code and other information.  

Text storage sites are often used to host malicious code for C2 communication (e.g., [Stage Capabilities](https://attack.mitre.org/techniques/T1608)), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely.(Citation: Pastebin EchoSec)

**Note:** This is distinct from [Exfiltration to Code Repository](https://attack.mitre.org/techniques/T1567/001), which highlight access to code repositories via APIs.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1567/003)
- [Pastebin EchoSec](https://web.archive.org/web/20201107203304/https://www.echosec.net/blog/what-is-pastebin-and-why-do-hackers-love-it)
