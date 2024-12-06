---
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--7c46b364-8496-4234-8a56-f7e6727e21e1
mitre_attack_url: https://attack.mitre.org/techniques/T1020/001
name: Traffic Duplication
platforms:
- Network
- IaaS
tactics:
- exfiltration
title: exfiltration - Traffic Duplication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | exfiltration |
| **Platforms** | Network, IaaS |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1020/001](https://attack.mitre.org/techniques/T1020/001) |

# Traffic Duplication (attack-pattern--7c46b364-8496-4234-8a56-f7e6727e21e1)

## Description
Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised infrastructure. Traffic mirroring is a native feature for some devices, often used for network analysis. For example, devices may be configured to forward network traffic to one or more destinations for analysis by a network analyzer or other monitoring device. (Citation: Cisco Traffic Mirroring)(Citation: Juniper Traffic Mirroring)

Adversaries may abuse traffic mirroring to mirror or redirect network traffic through other infrastructure they control. Malicious modifications to network devices to enable traffic redirection may be possible through [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) or [Patch System Image](https://attack.mitre.org/techniques/T1601/001).(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks)

Many cloud-based environments also support traffic mirroring. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.(Citation: AWS Traffic Mirroring)(Citation: GCP Packet Mirroring)(Citation: Azure Virtual Network TAP)

Adversaries may use traffic duplication in conjunction with [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Input Capture](https://attack.mitre.org/techniques/T1056), or [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) depending on the goals and objectives of the adversary.

## Detection
Monitor network traffic for uncommon data flows (e.g. unusual network communications, suspicious communications that have never been seen before, communications sending fixed size data packets at regular intervals).  Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1020/001)
- [AWS Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html)
- [Cisco Traffic Mirroring](https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r5-1/interfaces/configuration/guide/hc51xcrsbook/hc51span.html)
- [GCP Packet Mirroring](https://cloud.google.com/vpc/docs/packet-mirroring)
- [Juniper Traffic Mirroring](https://www.juniper.net/documentation/en_US/junos/topics/concept/port-mirroring-ex-series.html)
- [Azure Virtual Network TAP](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview)
- [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
