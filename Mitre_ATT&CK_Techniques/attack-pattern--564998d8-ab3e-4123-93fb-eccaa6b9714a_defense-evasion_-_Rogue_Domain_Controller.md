---
contributors:
- Vincent Le Toux
data_sources:
- 'Active Directory: Active Directory Object Modification'
- 'Network Traffic: Network Traffic Content'
- 'User Account: User Account Authentication'
- 'Active Directory: Active Directory Object Creation'
id: attack-pattern--564998d8-ab3e-4123-93fb-eccaa6b9714a
mitre_attack_url: https://attack.mitre.org/techniques/T1207
name: Rogue Domain Controller
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Rogue Domain Controller
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Object Modification, Network Traffic: Network Traffic Content, User Account: User Account Authentication, Active Directory: Active Directory Object Creation |
| **Permissions Required** | Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1207](https://attack.mitre.org/techniques/T1207) |

# Rogue Domain Controller (attack-pattern--564998d8-ab3e-4123-93fb-eccaa6b9714a)

## Description
Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. (Citation: DCShadow Blog) Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.

Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema, which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. (Citation: Adsecurity Mimikatz Guide)

This technique may bypass system logging and security monitors such as security information and event management (SIEM) products (since actions taken on a rogue DC may not be reported to these sensors). (Citation: DCShadow Blog) The technique may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries may also utilize this technique to perform [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) and/or manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence. (Citation: DCShadow Blog)

## Detection
Monitor and analyze network traffic associated with data replication (such as calls to DrsAddEntry, DrsReplicaAdd, and especially GetNCChanges) between DCs as well as to/from non DC hosts. (Citation: GitHub DCSYNCMonitor) (Citation: DCShadow Blog) DC replication will naturally take place every 15 minutes but can be triggered by an adversary or by legitimate urgent changes (ex: passwords). Also consider monitoring and alerting on the replication of AD objects (Audit Detailed Directory Service Replication Events 4928 and 4929). (Citation: DCShadow Blog)

Leverage AD directory synchronization (DirSync) to monitor changes to directory state using AD replication cookies. (Citation: Microsoft DirSync) (Citation: ADDSecurity DCShadow Feb 2018)

Baseline and periodically analyze the Configuration partition of the AD schema and alert on creation of nTDSDSA objects. (Citation: DCShadow Blog)

Investigate usage of Kerberos Service Principal Names (SPNs), especially those associated with services (beginning with “GC/”) by computers not present in the DC organizational unit (OU). The SPN associated with the Directory Replication Service (DRS) Remote Protocol interface (GUID E3514235–4B06–11D1-AB04–00C04FC2DCD2) can be set without logging. (Citation: ADDSecurity DCShadow Feb 2018) A rogue DC must authenticate as a service using these two SPNs for the replication process to successfully complete.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1207)
- [DCShadow Blog](https://www.dcshadow.com/)
- [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)
- [GitHub DCSYNCMonitor](https://github.com/shellster/DCSYNCMonitor)
- [Microsoft DirSync](https://msdn.microsoft.com/en-us/library/ms677626.aspx)
- [ADDSecurity DCShadow Feb 2018](https://adds-security.blogspot.fr/2018/02/detecter-dcshadow-impossible.html)
