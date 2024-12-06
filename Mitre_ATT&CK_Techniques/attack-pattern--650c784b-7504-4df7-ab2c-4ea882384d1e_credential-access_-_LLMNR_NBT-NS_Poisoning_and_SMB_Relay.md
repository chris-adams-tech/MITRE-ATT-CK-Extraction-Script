---
contributors:
- Eric Kuehn, Secure Ideas
- Matthew Demaske, Adaptforward
- Andrew Allen, @whitehat_zero
data_sources:
- 'Service: Service Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Windows Registry: Windows Registry Key Modification'
id: attack-pattern--650c784b-7504-4df7-ab2c-4ea882384d1e
mitre_attack_url: https://attack.mitre.org/techniques/T1557/001
name: LLMNR/NBT-NS Poisoning and SMB Relay
platforms:
- Windows
tactics:
- credential-access
- collection
title: credential-access - LLMNR/NBT-NS Poisoning and SMB Relay
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, collection |
| **Platforms** | Windows |
| **Data Sources** | Service: Service Creation, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Windows Registry: Windows Registry Key Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1557/001](https://attack.mitre.org/techniques/T1557/001) |

# LLMNR/NBT-NS Poisoning and SMB Relay (attack-pattern--650c784b-7504-4df7-ab2c-4ea882384d1e)

## Description
By responding to LLMNR/NBT-NS network traffic, adversaries may spoof an authoritative source for name resolution to force communication with an adversary controlled system. This activity may be used to collect or relay authentication materials. 

Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts. NBT-NS identifies systems on a local network by their NetBIOS name. (Citation: Wikipedia LLMNR)(Citation: TechNet NetBIOS)

Adversaries can spoof an authoritative source for name resolution on a victim network by responding to LLMNR (UDP 5355)/NBT-NS (UDP 137) traffic as if they know the identity of the requested host, effectively poisoning the service so that the victims will communicate with the adversary controlled system. If the requested host belongs to a resource that requires identification/authentication, the username and NTLMv2 hash will then be sent to the adversary controlled system. The adversary can then collect the hash information sent over the wire through tools that monitor the ports for traffic or through [Network Sniffing](https://attack.mitre.org/techniques/T1040) and crack the hashes offline through [Brute Force](https://attack.mitre.org/techniques/T1110) to obtain the plaintext passwords.

In some cases where an adversary has access to a system that is in the authentication path between systems or when automated scans that use credentials attempt to authenticate to an adversary controlled system, the NTLMv1/v2 hashes can be intercepted and relayed to access and execute code against a target system. The relay step can happen in conjunction with poisoning but may also be independent of it.(Citation: byt3bl33d3r NTLM Relaying)(Citation: Secure Ideas SMB Relay) Additionally, adversaries may encapsulate the NTLMv1/v2 hashes into various protocols, such as LDAP, SMB, MSSQL and HTTP, to expand and use multiple services with the valid NTLM response. 

Several tools may be used to poison name services within local networks such as NBNSpoof, Metasploit, and [Responder](https://attack.mitre.org/software/S0174).(Citation: GitHub NBNSpoof)(Citation: Rapid7 LLMNR Spoofer)(Citation: GitHub Responder)

## Detection
Monitor <code>HKLM\Software\Policies\Microsoft\Windows NT\DNSClient</code> for changes to the "EnableMulticast" DWORD value. A value of “0” indicates LLMNR is disabled. (Citation: Sternsecurity LLMNR-NBTNS)

Monitor for traffic on ports UDP 5355 and UDP 137 if LLMNR/NetBIOS is disabled by security policy.

Deploy an LLMNR/NBT-NS spoofing detection tool.(Citation: GitHub Conveigh) Monitoring of Windows event logs for event IDs 4697 and 7045 may help in detecting successful relay techniques.(Citation: Secure Ideas SMB Relay)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1557/001)
- [Rapid7 LLMNR Spoofer](https://www.rapid7.com/db/modules/auxiliary/spoof/llmnr/llmnr_response)
- [GitHub Responder](https://github.com/SpiderLabs/Responder)
- [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)
- [TechNet NetBIOS](https://technet.microsoft.com/library/cc958811.aspx)
- [GitHub NBNSpoof](https://github.com/nomex/nbnspoof)
- [GitHub Conveigh](https://github.com/Kevin-Robertson/Conveigh)
- [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)
- [Sternsecurity LLMNR-NBTNS](https://www.sternsecurity.com/blog/local-network-attacks-llmnr-and-nbt-ns-poisoning)
- [Wikipedia LLMNR](https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution)
