---
contributors:
- Ted Samuels, Rapid7
- Jonhnathan Ribeiro, 3CORESec, @_w0rk3r
data_sources:
- 'Script: Script Execution'
- 'Active Directory: Active Directory Object Access'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--1b20efbf-8063-4fc3-a07d-b575318a301b
mitre_attack_url: https://attack.mitre.org/techniques/T1615
name: Group Policy Discovery
platforms:
- Windows
tactics:
- discovery
title: discovery - Group Policy Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows |
| **Data Sources** | Script: Script Execution, Active Directory: Active Directory Object Access, Process: Process Creation, Command: Command Execution, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1615](https://attack.mitre.org/techniques/T1615) |

# Group Policy Discovery (attack-pattern--1b20efbf-8063-4fc3-a07d-b575318a301b)

## Description
Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016)

Adversaries may use commands such as <code>gpresult</code> or various publicly available PowerShell functions, such as <code>Get-DomainGPO</code> and <code>Get-DomainGPOLocalGroup</code>, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation: Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [Domain or Tenant Policy Modification](https://attack.mitre.org/techniques/T1484)) for their benefit.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.

Monitor for suspicious use of <code>gpresult</code>. Monitor for the use of PowerShell functions such as <code>Get-DomainGPO</code> and <code>Get-DomainGPOLocalGroup</code> and processes spawning with command-line arguments containing <code>GPOLocalGroup</code>.

Monitor for abnormal LDAP queries with filters for <code>groupPolicyContainer</code> and high volumes of LDAP traffic to domain controllers. Windows Event ID 4661 can also be used to detect when a directory service has been accessed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1615)
- [ADSecurity GPO Persistence 2016](https://adsecurity.org/?p=2716)
- [Microsoft gpresult](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
- [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
- [TechNet Group Policy Basics](https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/)
