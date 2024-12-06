---
contributors:
- Oleg Kolesnikov, Securonix
- Tiago Faria, 3CORESec
- Austin Clark, @c2defense
- Itamar Mizrahi, Cymptom
- Eliraz Levi, Hunters
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--3257eb21-f9a7-4430-8de1-d8b6e288f529
mitre_attack_url: https://attack.mitre.org/techniques/T1040
name: Network Sniffing
platforms:
- Linux
- macOS
- Windows
- Network
- IaaS
tactics:
- credential-access
- discovery
title: credential-access - Network Sniffing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, discovery |
| **Platforms** | Linux, macOS, Windows, Network, IaaS |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **System Requirements** | Network interface access and packet capture driver |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1040](https://attack.mitre.org/techniques/T1040) |

# Network Sniffing (attack-pattern--3257eb21-f9a7-4430-8de1-d8b6e288f529)

## Description
Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as [LLMNR/NBT-NS Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001), can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent [Lateral Movement](https://attack.mitre.org/tactics/TA0008) and/or [Defense Evasion](https://attack.mitre.org/tactics/TA0005) activities. Adversaries may likely also utilize network sniffing during [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) (AiTM) to passively gain additional knowledge about the environment.

In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.(Citation: AWS Traffic Mirroring)(Citation: GCP Packet Mirroring)(Citation: Azure Virtual Network TAP) Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic.(Citation: Rhino Security Labs AWS VPC Traffic Mirroring)(Citation: SpecterOps AWS Traffic Mirroring) The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.(Citation: Rhino Security Labs AWS VPC Traffic Mirroring)

On network devices, adversaries may perform network captures using [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `monitor capture`.(Citation: US-CERT-TA18-106A)(Citation: capture_embedded_packet_on_software)

## Detection
Detecting the events leading up to sniffing network traffic may be the best method of detection. From the host level, an adversary would likely need to perform a [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) attack against other devices on a wired network in order to capture traffic that was not to or from the current compromised system. This change in the flow of information is detectable at the enclave network level. Monitor for ARP spoofing and gratuitous ARP broadcasts. Detecting compromised network devices is a bit more challenging. Auditing administrator logins, configuration changes, and device images is required to detect malicious changes.

In cloud-based environments, monitor for the creation of new traffic mirrors or modification of existing traffic mirrors. For network infrastructure devices, collect AAA logging to monitor for the capture of network traffic.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1040)
- [AWS Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html)
- [capture_embedded_packet_on_software](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html)
- [GCP Packet Mirroring](https://cloud.google.com/vpc/docs/packet-mirroring)
- [SpecterOps AWS Traffic Mirroring](https://posts.specterops.io/through-the-looking-glass-part-1-f539ae308512)
- [Azure Virtual Network TAP](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview)
- [Rhino Security Labs AWS VPC Traffic Mirroring](https://rhinosecuritylabs.com/aws/abusing-vpc-traffic-mirroring-in-aws/)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
