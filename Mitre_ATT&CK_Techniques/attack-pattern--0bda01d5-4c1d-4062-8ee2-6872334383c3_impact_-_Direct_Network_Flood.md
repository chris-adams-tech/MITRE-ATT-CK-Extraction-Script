---
data_sources:
  - "Network Traffic: Network Traffic Flow"
  - "Sensor Health: Host Status"
id: attack-pattern--0bda01d5-4c1d-4062-8ee2-6872334383c3
mitre_attack_url: https://attack.mitre.org/techniques/T1498/001
name: Direct Network Flood
platforms:
  - Windows
  - IaaS
  - Linux
  - macOS
tactics:
  - impact
title: T1498.001 - impact - Direct Network Flood
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Network Traffic: Network Traffic Flow, Sensor Health: Host Status |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1498/001](https://attack.mitre.org/techniques/T1498/001) |

# Direct Network Flood (attack-pattern--0bda01d5-4c1d-4062-8ee2-6872334383c3)

## Description
Adversaries may attempt to cause a denial of service (DoS) by directly sending a high-volume of network traffic to a target. This DoS attack may also reduce the availability and functionality of the targeted system(s) and network. [Direct Network Flood](https://attack.mitre.org/techniques/T1498/001)s are when one or more systems are used to send a high-volume of network packets towards the targeted service's network. Almost any network protocol may be used for flooding. Stateless protocols such as UDP or ICMP are commonly used but stateful protocols such as TCP can be used as well.

Botnets are commonly used to conduct network flooding attacks against networks and services. Large botnets can generate a significant amount of traffic from systems spread across the global Internet. Adversaries may have the resources to build out and control their own botnet infrastructure or may rent time on an existing botnet to conduct an attack. In some of the worst cases for distributed DoS (DDoS), so many systems are used to generate the flood that each one only needs to send out a small amount of traffic to produce enough volume to saturate the target network. In such circumstances, distinguishing DDoS traffic from legitimate clients becomes exceedingly difficult. Botnets have been used in some of the most high-profile DDoS flooding attacks, such as the 2012 series of incidents that targeted major US banks.(Citation: USNYAG IranianBotnet March 2016)

## Detection
Detection of a network flood can sometimes be achieved before the traffic volume is sufficient to cause impact to the availability of the service, but such response time typically requires very aggressive monitoring and responsiveness or services provided by an upstream network service provider. Typical network throughput monitoring tools such as netflow(Citation: Cisco DoSdetectNetflow), SNMP, and custom scripts can be used to detect sudden increases in network or service utilization. Real-time, automated, and qualitative study of the network traffic can identify a sudden surge in one type of protocol can be used to detect a network flood event as it starts. Often, the lead time may be small and the indicator of an event availability of the network or service drops. The analysis tools mentioned can then be used to determine the type of DoS causing the outage and help with remediation.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1498/001)
- [Cisco DoSdetectNetflow](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/netflow/configuration/15-mt/nf-15-mt-book/nf-detct-analy-thrts.pdf)
- [USNYAG IranianBotnet March 2016](https://www.justice.gov/opa/pr/seven-iranians-working-islamic-revolutionary-guard-corps-affiliated-entities-charged)
