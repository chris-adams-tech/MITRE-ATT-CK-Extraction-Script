---
contributors:
- Itamar Mizrahi, Cymptom
- Tristan Bennett, Seamless Intelligence
data_sources:
- 'Command: Command Execution'
- 'Active Directory: Active Directory Object Creation'
- 'Active Directory: Active Directory Object Modification'
- 'Active Directory: Active Directory Object Deletion'
id: attack-pattern--5d2be8b9-d24c-4e98-83bf-2f5f79477163
mitre_attack_url: https://attack.mitre.org/techniques/T1484/001
name: Group Policy Modification
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Group Policy Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Active Directory: Active Directory Object Creation, Active Directory: Active Directory Object Modification, Active Directory: Active Directory Object Deletion |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1484/001](https://attack.mitre.org/techniques/T1484/001) |

# Group Policy Modification (attack-pattern--5d2be8b9-d24c-4e98-83bf-2f5f79477163)

## Description
Adversaries may modify Group Policy Objects (GPOs) to subvert the intended discretionary access controls for a domain, usually with the intention of escalating privileges on the domain. Group policy allows for centralized management of user and computer settings in Active Directory (AD). GPOs are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016) 

Like other objects in AD, GPOs have access controls associated with them. By default all user accounts in the domain have permission to read GPOs. It is possible to delegate GPO access control permissions, e.g. write access, to specific users or groups in the domain.

Malicious GPO modifications can be used to implement many other malicious behaviors such as [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), [Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001), [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105), [Create Account](https://attack.mitre.org/techniques/T1136), [Service Execution](https://attack.mitre.org/techniques/T1569/002),  and more.(Citation: ADSecurity GPO Persistence 2016)(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions)(Citation: Mandiant M Trends 2016)(Citation: Microsoft Hacking Team Breach) Since GPOs can control so many user and machine settings in the AD environment, there are a great number of potential attacks that can stem from this GPO abuse.(Citation: Wald0 Guide to GPOs)

For example, publicly available scripts such as <code>New-GPOImmediateTask</code> can be leveraged to automate the creation of a malicious [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053) by modifying GPO settings, in this case modifying <code>&lt;GPO_PATH&gt;\Machine\Preferences\ScheduledTasks\ScheduledTasks.xml</code>.(Citation: Wald0 Guide to GPOs)(Citation: Harmj0y Abusing GPO Permissions) In some cases an adversary might modify specific user rights like SeEnableDelegationPrivilege, set in <code>&lt;GPO_PATH&gt;\MACHINE\Microsoft\Windows NT\SecEdit\GptTmpl.inf</code>, to achieve a subtle AD backdoor with complete control of the domain because the user account under the adversary's control would then be able to modify GPOs.(Citation: Harmj0y SeEnableDelegationPrivilege Right)

## Detection
It is possible to detect GPO modifications by monitoring directory service changes using Windows event logs. Several events may be logged for such GPO modifications, including:

* Event ID 5136 - A directory service object was modified
* Event ID 5137 - A directory service object was created
* Event ID 5138 - A directory service object was undeleted
* Event ID 5139 - A directory service object was moved
* Event ID 5141 - A directory service object was deleted


GPO abuse will often be accompanied by some other behavior such as [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), which will have events associated with it to detect. Subsequent permission value modifications, like those to SeEnableDelegationPrivilege, can also be searched for in events associated with privileges assigned to new logons (Event ID 4672) and assignment of user rights (Event ID 4704).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1484/001)
- [Mandiant M Trends 2016](https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/rpt-mtrends-2016.pdf)
- [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)
- [Microsoft Hacking Team Breach](https://www.microsoft.com/security/blog/2016/06/01/hacking-team-breach-a-cyber-jurassic-park/)
- [Wald0 Guide to GPOs](https://wald0.com/?p=179)
- [Harmj0y Abusing GPO Permissions](https://blog.harmj0y.net/redteaming/abusing-gpo-permissions/)
- [Harmj0y SeEnableDelegationPrivilege Right](https://blog.harmj0y.net/activedirectory/the-most-dangerous-user-right-you-probably-have-never-heard-of/)
- [TechNet Group Policy Basics](https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/)
