---
contributors:
- Cisco
- Nichols Jasper
- Jared Wilson
- Caio Silva
- Adrien Bataille
- Anders Vejlby
- Nader Zaveri
- Tamir Yehuda
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Script: Script Execution'
id: attack-pattern--d94b3ae9-8059-4989-8e9f-ea0f601f80a7
mitre_attack_url: https://attack.mitre.org/techniques/T1651
name: Cloud Administration Command
platforms:
- IaaS
tactics:
- execution
title: execution - Cloud Administration Command
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | IaaS |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1651](https://attack.mitre.org/techniques/T1651) |

# Cloud Administration Command (attack-pattern--d94b3ae9-8059-4989-8e9f-ea0f601f80a7)

## Description
Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [Trusted Relationship](https://attack.mitre.org/techniques/T1199) to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1651)
- [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)
- [MSTIC Nobelium Oct 2021](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)
- [Microsoft Run Command](https://learn.microsoft.com/en-us/azure/virtual-machines/run-command-overview)
