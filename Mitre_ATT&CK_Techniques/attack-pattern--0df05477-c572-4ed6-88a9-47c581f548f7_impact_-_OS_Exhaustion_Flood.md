---
data_sources:
  - "Network Traffic: Network Traffic Flow"
  - "Network Traffic: Network Traffic Content"
  - "Sensor Health: Host Status"
id: attack-pattern--0df05477-c572-4ed6-88a9-47c581f548f7
mitre_attack_url: https://attack.mitre.org/techniques/T1499/001
name: OS Exhaustion Flood
platforms:
  - Linux
  - macOS
  - Windows
tactics:
  - impact
title: T1499.001 - impact - OS Exhaustion Flood
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Sensor Health: Host Status |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1499/001](https://attack.mitre.org/techniques/T1499/001) |

# OS Exhaustion Flood (attack-pattern--0df05477-c572-4ed6-88a9-47c581f548f7)

## Description
Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS). A system's OS is responsible for managing the finite resources as well as preventing the entire system from being overwhelmed by excessive demands on its capacity. These attacks do not need to exhaust the actual resources on a system; the attacks may simply exhaust the limits and available resources that an OS self-imposes.

Different ways to achieve this exist, including TCP state-exhaustion attacks such as SYN floods and ACK floods.(Citation: Arbor AnnualDoSreport Jan 2018) With SYN floods, excessive amounts of SYN packets are sent, but the 3-way TCP handshake is never completed. Because each OS has a maximum number of concurrent TCP connections that it will allow, this can quickly exhaust the ability of the system to receive new requests for TCP connections, thus preventing access to any TCP service provided by the server.(Citation: Cloudflare SynFlood)

ACK floods leverage the stateful nature of the TCP protocol. A flood of ACK packets are sent to the target. This forces the OS to search its state table for a related TCP connection that has already been established. Because the ACK packets are for connections that do not exist, the OS will have to search the entire state table to confirm that no match exists. When it is necessary to do this for a large flood of packets, the computational requirements can cause the server to become sluggish and/or unresponsive, due to the work it must do to eliminate the rogue ACK packets. This greatly reduces the resources available for providing the targeted service.(Citation: Corero SYN-ACKflood)

## Detection
Detection of Endpoint DoS can sometimes be achieved before the effect is sufficient to cause significant impact to the availability of the service, but such response time typically requires very aggressive monitoring and responsiveness. Typical network throughput monitoring tools such as netflow, SNMP, and custom scripts can be used to detect sudden increases in circuit utilization.(Citation: Cisco DoSdetectNetflow) Real-time, automated, and qualitative study of the network traffic can identify a sudden surge in one type of protocol can be used to detect an attack as it starts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1499/001)
- [Cisco DoSdetectNetflow](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/netflow/configuration/15-mt/nf-15-mt-book/nf-detct-analy-thrts.pdf)
- [Cloudflare SynFlood](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)
- [Corero SYN-ACKflood](https://www.corero.com/resources/ddos-attack-types/syn-flood-ack.html)
- [Arbor AnnualDoSreport Jan 2018](https://pages.arbornetworks.com/rs/082-KNA-087/images/13th_Worldwide_Infrastructure_Security_Report.pdf)
