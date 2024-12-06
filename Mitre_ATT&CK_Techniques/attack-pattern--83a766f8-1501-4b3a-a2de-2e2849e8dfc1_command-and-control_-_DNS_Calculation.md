---
data_sources:
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--83a766f8-1501-4b3a-a2de-2e2849e8dfc1
mitre_attack_url: https://attack.mitre.org/techniques/T1568/003
name: DNS Calculation
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - DNS Calculation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1568/003](https://attack.mitre.org/techniques/T1568/003) |

# DNS Calculation (attack-pattern--83a766f8-1501-4b3a-a2de-2e2849e8dfc1)

## Description
Adversaries may perform calculations on addresses returned in DNS results to determine which port and IP address to use for command and control, rather than relying on a predetermined port number or the actual returned IP address. A IP and/or port number calculation can be used to bypass egress filtering on a C2 channel.(Citation: Meyers Numbered Panda)

One implementation of [DNS Calculation](https://attack.mitre.org/techniques/T1568/003) is to take the first three octets of an IP address in a DNS response and use those values to calculate the port for command and control traffic.(Citation: Meyers Numbered Panda)(Citation: Moran 2014)(Citation: Rapid7G20Espionage)

## Detection
Detection for this technique is difficult because it would require knowledge of the specific implementation of the port calculation algorithm. Detection may be possible by analyzing DNS records if the algorithm is known.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1568/003)
- [Meyers Numbered Panda](http://www.crowdstrike.com/blog/whois-numbered-panda/)
- [Moran 2014](https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html)
- [Rapid7G20Espionage](https://blog.rapid7.com/2013/08/26/upcoming-g20-summit-fuels-espionage-operations/)
