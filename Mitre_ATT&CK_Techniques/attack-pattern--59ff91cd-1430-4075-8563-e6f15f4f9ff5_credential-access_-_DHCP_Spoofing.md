---
contributors:
- Alex Spivakovsky, Pentera
- Andrew Allen, @whitehat_zero
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--59ff91cd-1430-4075-8563-e6f15f4f9ff5
mitre_attack_url: https://attack.mitre.org/techniques/T1557/003
name: DHCP Spoofing
platforms:
- Linux
- Windows
- macOS
tactics:
- credential-access
- collection
title: credential-access - DHCP Spoofing
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, collection |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Network Traffic: Network Traffic Content, Application Log: Application Log Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1557/003](https://attack.mitre.org/techniques/T1557/003) |

# DHCP Spoofing (attack-pattern--59ff91cd-1430-4075-8563-e6f15f4f9ff5)

## Description
Adversaries may redirect network traffic to adversary-owned systems by spoofing Dynamic Host Configuration Protocol (DHCP) traffic and acting as a malicious DHCP server on the victim network. By achieving the adversary-in-the-middle (AiTM) position, adversaries may collect network communications, including passed credentials, especially those sent over insecure, unencrypted protocols. This may also enable follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040) or [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002).

DHCP is based on a client-server model and has two functionalities: a protocol for providing network configuration settings from a DHCP server to a client and a mechanism for allocating network addresses to clients.(Citation: rfc2131) The typical server-client interaction is as follows: 

1. The client broadcasts a `DISCOVER` message.

2. The server responds with an `OFFER` message, which includes an available network address. 

3. The client broadcasts a `REQUEST` message, which includes the network address offered. 

4. The server acknowledges with an `ACK` message and the client receives the network configuration parameters.

Adversaries may spoof as a rogue DHCP server on the victim network, from which legitimate hosts may receive malicious network configurations. For example, malware can act as a DHCP server and provide adversary-owned DNS servers to the victimized computers.(Citation: new_rogue_DHCP_serv_malware)(Citation: w32.tidserv.g) Through the malicious network configurations, an adversary may achieve the AiTM position, route client traffic through adversary-controlled systems, and collect information from the client network.

DHCPv6 clients can receive network configuration information without being assigned an IP address by sending a <code>INFORMATION-REQUEST (code 11)</code> message to the <code>All_DHCP_Relay_Agents_and_Servers</code> multicast address.(Citation: rfc3315) Adversaries may use their rogue DHCP server to respond to this request message with malicious network configurations.

Rather than establishing an AiTM position, adversaries may also abuse DHCP spoofing to perform a DHCP exhaustion attack (i.e, [Service Exhaustion Flood](https://attack.mitre.org/techniques/T1499/002)) by generating many broadcast DISCOVER messages to exhaust a network’s DHCP allocation pool. 

## Detection
Monitor network traffic for suspicious/malicious behavior involving DHCP, such as changes in DNS and/or gateway parameters. Additionally, monitor Windows logs for Event IDs (EIDs) 1341, 1342, 1020 and 1063, which specify that the IP allocations are low or have run out; these EIDs may indicate a denial of service attack.(Citation: dhcp_serv_op_events)(Citation: solution_monitor_dhcp_scopes)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1557/003)
- [rfc2131](https://datatracker.ietf.org/doc/html/rfc2131)
- [new_rogue_DHCP_serv_malware](https://isc.sans.edu/forums/diary/new+rogueDHCP+server+malware/6025/)
- [rfc3315](https://datatracker.ietf.org/doc/html/rfc3315)
- [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))
- [solution_monitor_dhcp_scopes](https://web.archive.org/web/20231202025258/https://lockstepgroup.com/blog/monitor-dhcp-scopes-and-detect-man-in-the-middle-attacks/)
- [w32.tidserv.g](https://web.archive.org/web/20150923175837/http://www.symantec.com/security_response/writeup.jsp?docid=2009-032211-2952-99&tabid=2)
