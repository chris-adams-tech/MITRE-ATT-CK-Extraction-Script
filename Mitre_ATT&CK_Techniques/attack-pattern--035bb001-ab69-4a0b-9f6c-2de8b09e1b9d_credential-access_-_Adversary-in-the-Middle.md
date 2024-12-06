---
contributors:
- Mayuresh Dani, Qualys
- Daniil Yugoslavskiy, @yugoslavskiy, Atomic Threat Coverage project
- NEC
data_sources:
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
- 'Windows Registry: Windows Registry Key Modification'
- 'Network Traffic: Network Traffic Flow'
- 'Service: Service Creation'
id: attack-pattern--035bb001-ab69-4a0b-9f6c-2de8b09e1b9d
mitre_attack_url: https://attack.mitre.org/techniques/T1557
name: Adversary-in-the-Middle
platforms:
- Windows
- macOS
- Linux
- Network
tactics:
- credential-access
- collection
title: credential-access - Adversary-in-the-Middle
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, collection |
| **Platforms** | Windows, macOS, Linux, Network |
| **Data Sources** | Application Log: Application Log Content, Network Traffic: Network Traffic Content, Windows Registry: Windows Registry Key Modification, Network Traffic: Network Traffic Flow, Service: Service Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1557](https://attack.mitre.org/techniques/T1557) |

# Adversary-in-the-Middle (attack-pattern--035bb001-ab69-4a0b-9f6c-2de8b09e1b9d)

## Description
Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002), or replay attacks ([Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212)). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions.(Citation: Rapid7 MiTM Basics)

For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware.(Citation: ttint_rat)(Citation: dns_changer_trojans)(Citation: ad_blocker_with_miner) Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens ([Steal Application Access Token](https://attack.mitre.org/techniques/T1528)) and session cookies ([Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)).(Citation: volexity_0day_sophos_FW)(Citation: Token tactics) [Downgrade Attack](https://attack.mitre.org/techniques/T1562/010)s can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm.(Citation: mitm_tls_downgrade_att)(Citation: taxonomy_downgrade_att_tls)(Citation: tlseminar_downgrade_att)

Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002). Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to [Impair Defenses](https://attack.mitre.org/techniques/T1562) and/or in support of a [Network Denial of Service](https://attack.mitre.org/techniques/T1498).

## Detection
Monitor network traffic for anomalies associated with known AiTM behavior. Consider monitoring for modifications to system configuration files involved in shaping network traffic flow.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1557)
- [dns_changer_trojans](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/web-attack/125/how-dns-changer-trojans-direct-users-to-threats)
- [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [taxonomy_downgrade_att_tls](https://arxiv.org/abs/1809.05681)
- [ad_blocker_with_miner](https://securelist.com/ad-blocker-with-miner-included/101105/)
- [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)
- [mitm_tls_downgrade_att](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)
- [Rapid7 MiTM Basics](https://www.rapid7.com/fundamentals/man-in-the-middle-attacks/)
- [tlseminar_downgrade_att](https://tlseminar.github.io/downgrade-attacks/)
- [ttint_rat](https://blog.netlab.360.com/ttint-an-iot-remote-control-trojan-spread-through-2-0-day-vulnerabilities/)
