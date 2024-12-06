---
contributors:
- "Eduardo Gonz\xE1lez Hern\xE1ndez (@codexlynx)"
- "Eder P\xE9rez Ignacio, @ch4ik0"
- Wirapong Petshagun
- '@grahamhelton3'
- Ruben Groenewoud, Elastic
data_sources:
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--f4c3f644-ab33-433d-8648-75cc03a95792
mitre_attack_url: https://attack.mitre.org/techniques/T1546/017
name: Udev Rules
platforms:
- Linux
tactics:
- persistence
- privilege-escalation
title: persistence - Udev Rules
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux |
| **Data Sources** | Process: Process Creation, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/017](https://attack.mitre.org/techniques/T1546/017) |

# Udev Rules (attack-pattern--f4c3f644-ab33-433d-8648-75cc03a95792)

## Description
Adversaries may maintain persistence through executing malicious content triggered using udev rules. Udev is the Linux kernel device manager that dynamically manages device nodes, handles access to pseudo-device files in the `/dev` directory, and responds to hardware events, such as when external devices like hard drives or keyboards are plugged in or removed. Udev uses rule files with `match keys` to specify the conditions a hardware event must meet and `action keys` to define the actions that should follow. Root permissions are required to create, modify, or delete rule files located in `/etc/udev/rules.d/`, `/run/udev/rules.d/`, `/usr/lib/udev/rules.d/`, `/usr/local/lib/udev/rules.d/`, and `/lib/udev/rules.d/`. Rule priority is determined by both directory and by the digit prefix in the rule filename.(Citation: Ignacio Udev research 2024)(Citation: Elastic Linux Persistence 2024)

Adversaries may abuse the udev subsystem by adding or modifying rules in udev rule files to execute malicious content. For example, an adversary may configure a rule to execute their binary each time the pseudo-device file, such as `/dev/random`, is accessed by an application. Although udev is limited to running short tasks and is restricted by systemd-udevd's sandbox (blocking network and filesystem access), attackers may use scripting commands under the action key `RUN+=` to detach and run the malicious content’s process in the background to bypass these controls.(Citation: Reichert aon sedexp 2024)

## Detection
Monitor file creation and modification of Udev rule files in `/etc/udev/rules.d/`, `/lib/udev/rules.d/`, and /usr/lib/udev/rules.d/, specifically the `RUN` action key commands.(Citation: Ignacio Udev research 2024) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/017)
- [Ignacio Udev research 2024](https://ch4ik0.github.io/en/posts/leveraging-Linux-udev-for-persistence/)
- [Elastic Linux Persistence 2024](https://www.elastic.co/security-labs/sequel-on-persistence-mechanisms)
- [Reichert aon sedexp 2024](https://www.aon.com/en/insights/cyber-labs/unveiling-sedexp)
