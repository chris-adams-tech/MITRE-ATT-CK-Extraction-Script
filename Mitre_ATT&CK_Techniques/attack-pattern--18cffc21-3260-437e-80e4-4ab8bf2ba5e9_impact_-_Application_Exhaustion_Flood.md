---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Sensor Health: Host Status'
- 'Application Log: Application Log Content'
id: attack-pattern--18cffc21-3260-437e-80e4-4ab8bf2ba5e9
mitre_attack_url: https://attack.mitre.org/techniques/T1499/003
name: Application Exhaustion Flood
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- impact
title: impact - Application Exhaustion Flood
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Sensor Health: Host Status, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1499/003](https://attack.mitre.org/techniques/T1499/003) |

# Application Exhaustion Flood (attack-pattern--18cffc21-3260-437e-80e4-4ab8bf2ba5e9)

## Description
Adversaries may target resource intensive features of applications to cause a denial of service (DoS), denying availability to those applications. For example, specific features in web applications may be highly resource intensive. Repeated requests to those features may be able to exhaust system resources and deny access to the application or the server itself.(Citation: Arbor AnnualDoSreport Jan 2018)

## Detection
Detection of Endpoint DoS can sometimes be achieved before the effect is sufficient to cause significant impact to the availability of the service, but such response time typically requires very aggressive monitoring and responsiveness. Typical network throughput monitoring tools such as netflow, SNMP, and custom scripts can be used to detect sudden increases in circuit utilization.(Citation: Cisco DoSdetectNetflow) Real-time, automated, and qualitative study of the network traffic can identify a sudden surge in one type of protocol can be used to detect an attack as it starts.

In addition to network level detections, endpoint logging and instrumentation can be useful for detection. Attacks targeting web applications may generate logs in the web server, application server, and/or database server that can be used to identify the type of attack, possibly before the impact is felt.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1499/003)
- [Cisco DoSdetectNetflow](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/netflow/configuration/15-mt/nf-15-mt-book/nf-detct-analy-thrts.pdf)
- [Arbor AnnualDoSreport Jan 2018](https://pages.arbornetworks.com/rs/082-KNA-087/images/13th_Worldwide_Infrastructure_Security_Report.pdf)
