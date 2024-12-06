---
contributors:
- Jimmy Astle, @AstleJimmy, Carbon Black
- Erika Noerenberg, @gutterchurl, Carbon Black
data_sources:
- 'Process: Process Creation'
- 'Process: OS API Execution'
id: attack-pattern--b84903f0-c7d5-435d-a69e-de47cc3578c0
mitre_attack_url: https://attack.mitre.org/techniques/T1548/004
name: Elevated Execution with Prompt
platforms:
- macOS
tactics:
- privilege-escalation
- defense-evasion
title: privilege-escalation - Elevated Execution with Prompt
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, defense-evasion |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Creation, Process: OS API Execution |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1548/004](https://attack.mitre.org/techniques/T1548/004) |

# Elevated Execution with Prompt (attack-pattern--b84903f0-c7d5-435d-a69e-de47cc3578c0)

## Description
Adversaries may leverage the <code>AuthorizationExecuteWithPrivileges</code> API to escalate privileges by prompting the user for credentials.(Citation: AppleDocs AuthorizationExecuteWithPrivileges) The purpose of this API is to give application developers an easy way to perform operations with root privileges, such as for application installation or updating. This API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously modified. 

Although this API is deprecated, it still fully functions in the latest releases of macOS. When calling this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior with elevated privileges.

Adversaries may abuse <code>AuthorizationExecuteWithPrivileges</code> to obtain root privileges in order to install malicious software on victims and install persistence mechanisms.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019)(Citation: OSX Coldroot RAT) This technique may be combined with [Masquerading](https://attack.mitre.org/techniques/T1036) to trick the user into granting escalated privileges to malicious code.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019) This technique has also been shown to work by modifying legitimate programs present on the machine that make use of this API.(Citation: Death by 1000 installers; it's all broken!)

## Detection
Consider monitoring for <code>/usr/libexec/security_authtrampoline</code> executions which may indicate that <code>AuthorizationExecuteWithPrivileges</code> is being executed. MacOS system logs may also indicate when <code>AuthorizationExecuteWithPrivileges</code> is being called. Monitoring OS API callbacks for the execution can also be a way to detect this behavior but requires specialized security tooling.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1548/004)
- [AppleDocs AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg)
- [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
- [Death by 1000 installers; it's all broken!](https://speakerdeck.com/patrickwardle/defcon-2017-death-by-1000-installers-its-all-broken?slide=8)
- [OSX Coldroot RAT](https://objective-see.com/blog/blog_0x2A.html)
