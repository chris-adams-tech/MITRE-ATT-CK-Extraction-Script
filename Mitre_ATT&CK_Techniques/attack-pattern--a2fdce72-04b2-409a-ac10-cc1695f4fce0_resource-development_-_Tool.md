---
contributors:
- SOCCRATES
- Mnemonic AS
data_sources:
- 'Malware Repository: Malware Metadata'
id: attack-pattern--a2fdce72-04b2-409a-ac10-cc1695f4fce0
mitre_attack_url: https://attack.mitre.org/techniques/T1588/002
name: Tool
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Tool
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Malware Repository: Malware Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1588/002](https://attack.mitre.org/techniques/T1588/002) |

# Tool (attack-pattern--a2fdce72-04b2-409a-ac10-cc1695f4fce0)

## Description
Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). Tool acquisition can involve the procurement of commercial software licenses, including for red teaming tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154). Commercial software may be obtained through purchase, stealing licenses (or licensed copies of the software), or cracking trial versions.(Citation: Recorded Future Beacon 2019)

Adversaries may obtain tools to support their operations, including to support execution of post-compromise behaviors. In addition to freely downloading or purchasing software, adversaries may steal software and/or software licenses from third-party entities (including other adversaries).

## Detection
In some cases, malware repositories can also be used to identify features of tool use associated with an adversary, such as watermarks in [Cobalt Strike](https://attack.mitre.org/software/S0154) payloads.(Citation: Analyzing CS Dec 2020)

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on post-compromise phases of the adversary lifecycle.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1588/002)
- [Analyzing CS Dec 2020](https://www.randhome.io/blog/2020/12/20/analyzing-cobalt-strike-for-fun-and-profit/)
- [Recorded Future Beacon 2019](https://www.recordedfuture.com/blog/identifying-cobalt-strike-servers)
