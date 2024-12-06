---
contributors:
- Thanabodi Phrakhun, @naikordian
data_sources:
- 'Logon Session: Logon Session Creation'
id: attack-pattern--45241b9e-9bbc-4826-a2cc-78855e51ca09
mitre_attack_url: https://attack.mitre.org/techniques/T1021/008
name: Direct Cloud VM Connections
platforms:
- IaaS
tactics:
- lateral-movement
title: lateral-movement - Direct Cloud VM Connections
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | IaaS |
| **Data Sources** | Logon Session: Logon Session Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/008](https://attack.mitre.org/techniques/T1021/008) |

# Direct Cloud VM Connections (attack-pattern--45241b9e-9bbc-4826-a2cc-78855e51ca09)

## Description
Adversaries may leverage [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the [Cloud API](https://attack.mitre.org/techniques/T1059/009), such as Azure Serial Console(Citation: Azure Serial Console), AWS EC2 Instance Connect(Citation: EC2 Instance Connect)(Citation: lucr-3: Getting SaaS-y in the cloud), and AWS System Manager.(Citation: AWS System Manager).

Methods of authentication for these connections can include passwords, application access tokens, or SSH keys. These cloud native methods may, by default, allow for privileged access on the host with SYSTEM or root level access. 

Adversaries may utilize these cloud native methods to directly access virtual infrastructure and pivot through an environment.(Citation: SIM Swapping and Abuse of the Microsoft Azure Serial Console) These connections typically provide direct console access to the VM rather than the execution of scripts (i.e., [Cloud Administration Command](https://attack.mitre.org/techniques/T1651)).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/008)
- [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html)
- [AWS System Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [lucr-3: Getting SaaS-y in the cloud](https://permiso.io/blog/lucr-3-scattered-spider-getting-saas-y-in-the-cloud)
- [SIM Swapping and Abuse of the Microsoft Azure Serial Console](https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial)
- [Azure Serial Console](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/serial-console-overview)
