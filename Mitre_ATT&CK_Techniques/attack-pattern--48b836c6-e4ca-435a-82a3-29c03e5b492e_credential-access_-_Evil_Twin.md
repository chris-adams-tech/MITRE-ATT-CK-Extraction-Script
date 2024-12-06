---
contributors:
- Menachem Goldstein
- DeFord L. Smith
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--48b836c6-e4ca-435a-82a3-29c03e5b492e
mitre_attack_url: https://attack.mitre.org/techniques/T1557/004
name: Evil Twin
platforms:
- Network
tactics:
- credential-access
- collection
title: credential-access - Evil Twin
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, collection |
| **Platforms** | Network |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1557/004](https://attack.mitre.org/techniques/T1557/004) |

# Evil Twin (attack-pattern--48b836c6-e4ca-435a-82a3-29c03e5b492e)

## Description
Adversaries may host seemingly genuine Wi-Fi access points to deceive users into connecting to malicious networks as a way of supporting follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002), or [Input Capture](https://attack.mitre.org/techniques/T1056).(Citation: Australia ‘Evil Twin’)

By using a Service Set Identifier (SSID) of a legitimate Wi-Fi network, fraudulent Wi-Fi access points may trick devices or users into connecting to malicious Wi-Fi networks.(Citation: Kaspersky evil twin)(Citation: medium evil twin)  Adversaries may provide a stronger signal strength or block access to Wi-Fi access points to coerce or entice victim devices into connecting to malicious networks.(Citation: specter ops evil twin)  A Wi-Fi Pineapple – a network security auditing and penetration testing tool – may be deployed in Evil Twin attacks for ease of use and broader range. Custom certificates may be used in an attempt to intercept HTTPS traffic. 

Similarly, adversaries may also listen for client devices sending probe requests for known or previously connected networks (Preferred Network Lists or PNLs). When a malicious access point receives a probe request, adversaries can respond with the same SSID to imitate the trusted, known network.(Citation: specter ops evil twin)  Victim devices are led to believe the responding access point is from their PNL and initiate a connection to the fraudulent network.

Upon logging into the malicious Wi-Fi access point, a user may be directed to a fake login page or captive portal webpage to capture the victim’s credentials. Once a user is logged into the fraudulent Wi-Fi network, the adversary may able to monitor network activity, manipulate data, or steal additional credentials. Locations with high concentrations of public Wi-Fi access, such as airports, coffee shops, or libraries, may be targets for adversaries to set up illegitimate Wi-Fi access points. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1557/004)
- [Kaspersky evil twin](https://usa.kaspersky.com/resource-center/preemptive-safety/evil-twin-attacks)
- [medium evil twin](https://kavigihan.medium.com/wireless-security-evil-twin-attack-d3842f4aef59)
- [specter ops evil twin](https://posts.specterops.io/modern-wireless-attacks-pt-i-basic-rogue-ap-theory-evil-twin-and-karma-attacks-35a8571550ee)
- [Australia ‘Evil Twin’](https://www.bleepingcomputer.com/news/security/australian-charged-for-evil-twin-wifi-attack-on-plane/)
