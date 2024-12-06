---
contributors:
- ExtraHop
- Vincent Le Toux
data_sources:
- 'Active Directory: Active Directory Object Access'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--f303a39a-6255-4b89-aecc-18c4d8ca7163
mitre_attack_url: https://attack.mitre.org/techniques/T1003/006
name: DCSync
platforms:
- Windows
tactics:
- credential-access
title: credential-access - DCSync
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Object Access, Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/006](https://attack.mitre.org/techniques/T1003/006) |

# DCSync (attack-pattern--f303a39a-6255-4b89-aecc-18c4d8ca7163)

## Description
Adversaries may attempt to access credentials and other sensitive information by abusing a Windows Domain Controller's application programming interface (API)(Citation: Microsoft DRSR Dec 2017) (Citation: Microsoft GetNCCChanges) (Citation: Samba DRSUAPI) (Citation: Wine API samlib.dll) to simulate the replication process from a remote domain controller using a technique called DCSync.

Members of the Administrators, Domain Admins, and Enterprise Admin groups or computer accounts on the domain controller are able to run DCSync to pull password data(Citation: ADSecurity Mimikatz DCSync) from Active Directory, which may include current and historical hashes of potentially useful accounts such as KRBTGT and Administrators. The hashes can then in turn be used to create a [Golden Ticket](https://attack.mitre.org/techniques/T1558/001) for use in [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003)(Citation: Harmj0y Mimikatz and DCSync) or change an account's password as noted in [Account Manipulation](https://attack.mitre.org/techniques/T1098).(Citation: InsiderThreat ChangeNTLM July 2017)

DCSync functionality has been included in the "lsadump" module in [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub Mimikatz lsadump Module) Lsadump also includes NetSync, which performs DCSync over a legacy replication protocol.(Citation: Microsoft NRPC Dec 2017)

## Detection
Monitor domain controller logs for replication requests and other unscheduled activity possibly associated with DCSync.(Citation: Microsoft DRSR Dec 2017) (Citation: Microsoft GetNCCChanges) (Citation: Samba DRSUAPI) Also monitor for network protocols(Citation: Microsoft DRSR Dec 2017) (Citation: Microsoft NRPC Dec 2017) and other replication requests(Citation: Microsoft SAMR) from IPs not associated with known domain controllers.(Citation: AdSecurity DCSync Sept 2015)

Note: Domain controllers may not log replication requests originating from the default domain controller account.(Citation: Harmj0y DCSync Sept 2015)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/006)
- [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)
- [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)
- [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)
- [Microsoft DRSR Dec 2017](https://msdn.microsoft.com/library/cc228086.aspx)
- [Microsoft NRPC Dec 2017](https://msdn.microsoft.com/library/cc237008.aspx)
- [Microsoft GetNCCChanges](https://msdn.microsoft.com/library/dd207691.aspx)
- [Microsoft SAMR](https://msdn.microsoft.com/library/cc245496.aspx)
- [Samba DRSUAPI](https://wiki.samba.org/index.php/DRSUAPI)
- [Harmj0y DCSync Sept 2015](http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)
- [Harmj0y Mimikatz and DCSync](https://blog.harmj0y.net/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)
- [InsiderThreat ChangeNTLM July 2017](https://blog.stealthbits.com/manipulating-user-passwords-with-mimikatz-SetNTLM-ChangeNTLM)
- [Wine API samlib.dll](https://source.winehq.org/WineAPI/samlib.html)
