---
contributors:
- ExtraHop
- David Fiser, @anu4is, Trend Micro
- Alfredo Oliveira, Trend Micro
- Idan Frimark, Cisco
- Rory McCune, Aqua Security
- Yuval Avrahami, Palo Alto Networks
- Jay Chen, Palo Alto Networks
- Brad Geesaman, @bradgeesaman
- Magno Logan, @magnologan, Trend Micro
- Ariel Shuper, Cisco
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- Daniel Oakley
- Travis Smith, Tripwire
- David Tayouri
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Logon Session: Logon Session Metadata'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--10d51417-ee35-4589-b1ff-b6df1c334e8d
mitre_attack_url: https://attack.mitre.org/techniques/T1133
name: External Remote Services
platforms:
- Windows
- Linux
- Containers
- macOS
tactics:
- persistence
- initial-access
title: persistence - External Remote Services
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, initial-access |
| **Platforms** | Windows, Linux, Containers, macOS |
| **Data Sources** | Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow, Logon Session: Logon Session Metadata, Application Log: Application Log Content, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1133](https://attack.mitre.org/techniques/T1133) |

# External Remote Services (attack-pattern--10d51417-ee35-4589-b1ff-b6df1c334e8d)

## Description
Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006) and [VNC](https://attack.mitre.org/techniques/T1021/005) can also be used externally.(Citation: MacOS VNC software for Remote Desktop)

Access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.(Citation: Volexity Virtual Private Keylogging) Access to remote services may be used as a redundant or persistent access mechanism during an operation.

Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.(Citation: Trend Micro Exposed Docker Server)(Citation: Unit 42 Hildegard Malware)

## Detection
Follow best practices for detecting adversary use of [Valid Accounts](https://attack.mitre.org/techniques/T1078) for authenticating to remote services. Collect authentication logs and analyze for unusual access patterns, windows of activity, and access outside of normal business hours.

When authentication is not required to access an exposed remote service, monitor for follow-on activities such as anomalous external use of the exposed API or application.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1133)
- [Volexity Virtual Private Keylogging](https://www.volexity.com/blog/2015/10/07/virtual-private-keylogging-cisco-web-vpns-leveraged-for-access-and-persistence/)
- [MacOS VNC software for Remote Desktop](https://support.apple.com/guide/remote-desktop/set-up-a-computer-running-vnc-software-apdbed09830/mac)
- [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [Trend Micro Exposed Docker Server](https://www.trendmicro.com/en_us/research/20/f/xorddos-kaiji-botnet-malware-variants-target-exposed-docker-servers.html)
