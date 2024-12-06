---
contributors:
  - Eric Kuehn, Secure Ideas
  - Matthew Demaske, Adaptforward
id: attack-pattern--0dbf5f1b-a560-4d51-ac1b-d70caab3e1f0
mitre_attack_url: https://attack.mitre.org/techniques/T1171
name: LLMNR/NBT-NS Poisoning and Relay
platforms:
  - Windows
tactics:
  - credential-access
title: T1171 - credential-access - LLMNR/NBT-NS Poisoning and Relay
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1171](https://attack.mitre.org/techniques/T1171) |

# LLMNR/NBT-NS Poisoning and Relay (attack-pattern--0dbf5f1b-a560-4d51-ac1b-d70caab3e1f0)

## Description
Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts. NBT-NS identifies systems on a local network by their NetBIOS name. (Citation: Wikipedia LLMNR) (Citation: TechNet NetBIOS)

Adversaries can spoof an authoritative source for name resolution on a victim network by responding to LLMNR (UDP 5355)/NBT-NS (UDP 137) traffic as if they know the identity of the requested host, effectively poisoning the service so that the victims will communicate with the adversary controlled system. If the requested host belongs to a resource that requires identification/authentication, the username and NTLMv2 hash will then be sent to the adversary controlled system. The adversary can then collect the hash information sent over the wire through tools that monitor the ports for traffic or through [Network Sniffing](https://attack.mitre.org/techniques/T1040) and crack the hashes offline through [Brute Force](https://attack.mitre.org/techniques/T1110) to obtain the plaintext passwords. In some cases where an adversary has access to a system that is in the authentication path between systems or when automated scans that use credentials attempt to authenticate to an adversary controlled system, the NTLMv2 hashes can be intercepted and relayed to access and execute code against a target system. The relay step can happen in conjunction with poisoning but may also be independent of it. (Citation: byt3bl33d3r NTLM Relaying)(Citation: Secure Ideas SMB Relay)

Several tools exist that can be used to poison name services within local networks such as NBNSpoof, Metasploit, and [Responder](https://attack.mitre.org/software/S0174). (Citation: GitHub NBNSpoof) (Citation: Rapid7 LLMNR Spoofer) (Citation: GitHub Responder)

## Detection
Monitor <code>HKLM\Software\Policies\Microsoft\Windows NT\DNSClient</code> for changes to the "EnableMulticast" DWORD value. A value of “0” indicates LLMNR is disabled. (Citation: Sternsecurity LLMNR-NBTNS)

Monitor for traffic on ports UDP 5355 and UDP 137 if LLMNR/NetBIOS is disabled by security policy.

Deploy an LLMNR/NBT-NS spoofing detection tool.(Citation: GitHub Conveigh) Monitoring of Windows event logs for event IDs 4697 and 7045 may help in detecting successful relay techniques.(Citation: Secure Ideas SMB Relay)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1171)
- [Wikipedia LLMNR](https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution)
- [TechNet NetBIOS](https://technet.microsoft.com/library/cc958811.aspx)
- [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)
- [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)
- [GitHub NBNSpoof](https://github.com/nomex/nbnspoof)
- [Rapid7 LLMNR Spoofer](https://www.rapid7.com/db/modules/auxiliary/spoof/llmnr/llmnr_response)
- [GitHub Responder](https://github.com/SpiderLabs/Responder)
- [Sternsecurity LLMNR-NBTNS](https://www.sternsecurity.com/blog/local-network-attacks-llmnr-and-nbt-ns-poisoning)
- [GitHub Conveigh](https://github.com/Kevin-Robertson/Conveigh)
