---
contributors:
- Dave Westgard
- Elia Florio, Microsoft
- Mnemonic
- RedHuntLabs, @redhuntlabs
- ExtraHop
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Script: Script Execution'
- 'Network Traffic: Network Traffic Content'
- 'Process: OS API Execution'
id: attack-pattern--767dbf9e-df3f-45cb-8998-4903ab5f80c0
mitre_attack_url: https://attack.mitre.org/techniques/T1482
name: Domain Trust Discovery
platforms:
- Windows
tactics:
- discovery
title: discovery - Domain Trust Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, Script: Script Execution, Network Traffic: Network Traffic Content, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1482](https://attack.mitre.org/techniques/T1482) |

# Domain Trust Discovery (attack-pattern--767dbf9e-df3f-45cb-8998-4903ab5f80c0)

## Description
Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [SID-History Injection](https://attack.mitre.org/techniques/T1134/005), [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003), and [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).(Citation: AdSecurity Forging Trust Tickets)(Citation: Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [Nltest](https://attack.mitre.org/software/S0359) is known to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information, such as `nltest /domain_trusts`. Remote access tools with built-in features may interact directly with the Windows API to gather information. Look for the `DSEnumerateDomainTrusts()` Win32 API call to spot activity associated with [Domain Trust Discovery](https://attack.mitre.org/techniques/T1482).(Citation: Harmj0y Domain Trusts) Information may also be acquired through Windows system management tools such as [PowerShell](https://attack.mitre.org/techniques/T1059/001). The .NET method `GetAllTrustRelationships()` can be an indicator of [Domain Trust Discovery](https://attack.mitre.org/techniques/T1482).(Citation: Microsoft GetAllTrustRelationships)


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1482)
- [Microsoft Operation Wilysupply](https://www.microsoft.com/security/blog/2017/05/04/windows-defender-atp-thwarts-operation-wilysupply-software-supply-chain-cyberattack/)
- [AdSecurity Forging Trust Tickets](https://adsecurity.org/?p=1588)
- [Microsoft Trusts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10))
- [Microsoft GetAllTrustRelationships](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.domain.getalltrustrelationships?redirectedfrom=MSDN&view=netframework-4.7.2#System_DirectoryServices_ActiveDirectory_Domain_GetAllTrustRelationships)
- [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)
