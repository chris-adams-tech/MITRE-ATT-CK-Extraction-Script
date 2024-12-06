---
contributors:
- Tim (Wadhwa-)Brown
- CrowdStrike
data_sources:
- 'Process: Process Creation'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--005cc321-08ce-4d17-b1ea-cb5275926520
mitre_attack_url: https://attack.mitre.org/techniques/T1205/002
name: Socket Filters
platforms:
- Linux
- macOS
- Windows
tactics:
- defense-evasion
- persistence
- command-and-control
title: defense-evasion - Socket Filters
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1205/002](https://attack.mitre.org/techniques/T1205/002) |

# Socket Filters (attack-pattern--005cc321-08ce-4d17-b1ea-cb5275926520)

## Description
Adversaries may attach filters to a network socket to monitor then activate backdoors used for persistence or command and control. With elevated permissions, adversaries can use features such as the `libpcap` library to open sockets and install filters to allow or disallow certain types of data to come through the socket. The filter may apply to all traffic passing through the specified network interface (or every interface if not specified). When the network interface receives a packet matching the filter criteria, additional actions can be triggered on the host, such as activation of a reverse shell.

To establish a connection, an adversary sends a crafted packet to the targeted host that matches the installed filter criteria.(Citation: haking9 libpcap network sniffing) Adversaries have used these socket filters to trigger the installation of implants, conduct ping backs, and to invoke command shells. Communication with these socket filters may also be used in conjunction with [Protocol Tunneling](https://attack.mitre.org/techniques/T1572).(Citation: exatrack bpf filters passive backdoors)(Citation: Leonardo Turla Penquin May 2020)

Filters can be installed on any Unix-like platform with `libpcap` installed or on Windows hosts using `Winpcap`.  Adversaries may use either `libpcap` with `pcap_setfilter` or the standard library function `setsockopt` with `SO_ATTACH_FILTER` options. Since the socket connection is not active until the packet is received, this behavior may be difficult to detect due to the lack of activity on a host, low CPU overhead, and limited visibility into raw socket usage.

## Detection
Identify running processes with raw sockets. Ensure processes listed have a need for an open raw socket and are in accordance with enterprise policy.(Citation: crowdstrike bpf socket filters)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1205/002)
- [exatrack bpf filters passive backdoors](https://exatrack.com/public/Tricephalic_Hellkeeper.pdf)
- [crowdstrike bpf socket filters](https://www.crowdstrike.com/blog/how-to-hunt-for-decisivearchitect-and-justforfun-implant/)
- [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [haking9 libpcap network sniffing](http://recursos.aldabaknocking.com/libpcapHakin9LuisMartinGarcia.pdf)
