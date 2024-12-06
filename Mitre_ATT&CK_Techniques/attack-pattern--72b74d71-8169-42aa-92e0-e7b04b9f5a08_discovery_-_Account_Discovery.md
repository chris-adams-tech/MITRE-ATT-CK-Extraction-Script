---
contributors:
- Daniel Stepanic, Elastic
- Microsoft Threat Intelligence Center (MSTIC)
- Travis Smith, Tripwire
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Access'
id: attack-pattern--72b74d71-8169-42aa-92e0-e7b04b9f5a08
mitre_attack_url: https://attack.mitre.org/techniques/T1087
name: Account Discovery
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Office Suite
- Identity Provider
tactics:
- discovery
title: discovery - Account Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Office Suite, Identity Provider |
| **Data Sources** | Process: Process Creation, Command: Command Execution, File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1087](https://attack.mitre.org/techniques/T1087) |

# Account Discovery (attack-pattern--72b74d71-8169-42aa-92e0-e7b04b9f5a08)

## Description
Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List Users)(Citation: Google Cloud - IAM Servie Accounts List API) On hosts, adversaries can use default [PowerShell](https://attack.mitre.org/techniques/T1059/001) and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Detection
System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

Monitor for processes that can be used to enumerate user accounts, such as <code>net.exe</code> and <code>net1.exe</code>, especially when executed in quick succession.(Citation: Elastic - Koadiac Detection with EQL)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1087)
- [AWS List Users](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)
- [Google Cloud - IAM Servie Accounts List API](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)
- [Elastic - Koadiac Detection with EQL](https://www.elastic.co/blog/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
