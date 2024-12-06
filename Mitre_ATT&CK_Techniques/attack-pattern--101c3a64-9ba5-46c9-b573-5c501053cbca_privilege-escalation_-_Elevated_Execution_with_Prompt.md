---
contributors:
- Erika Noerenberg, @gutterchurl, Carbon Black
- Jimmy Astle, @AstleJimmy, Carbon Black
id: attack-pattern--101c3a64-9ba5-46c9-b573-5c501053cbca
mitre_attack_url: https://attack.mitre.org/techniques/T1514
name: Elevated Execution with Prompt
platforms:
- macOS
tactics:
- privilege-escalation
title: privilege-escalation - Elevated Execution with Prompt
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation |
| **Platforms** | macOS |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1514](https://attack.mitre.org/techniques/T1514) |

# Elevated Execution with Prompt (attack-pattern--101c3a64-9ba5-46c9-b573-5c501053cbca)

## Description
Adversaries may leverage the AuthorizationExecuteWithPrivileges API to escalate privileges by prompting the user for credentials.(Citation: AppleDocs AuthorizationExecuteWithPrivileges) The purpose of this API is to give application developers an easy way to perform operations with root privileges, such as for application installation or updating.  This API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously modified. Although this API is deprecated, it still fully functions in the latest releases of macOS. When calling this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior with elevated privileges.

Adversaries may abuse AuthorizationExecuteWithPrivileges to obtain root privileges in order to install malicious software on victims and install persistence mechanisms.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019)(Citation: OSX Coldroot RAT) This technique may be combined with [Masquerading](https://attack.mitre.org/techniques/T1036) to trick the user into granting escalated privileges to malicious code.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019) This technique has also been shown to work by modifying legitimate programs present on the machine that make use of this API.(Citation: Death by 1000 installers; it's all broken!)

## Detection
Consider monitoring for <code>/usr/libexec/security_authtrampoline</code> executions which may indicate that AuthorizationExecuteWithPrivileges is being executed. MacOS system logs may also indicate when AuthorizationExecuteWithPrivileges is being called. Monitoring OS API callbacks for the execution can also be a way to detect this behavior but requires specialized security tooling.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1514)
- [AppleDocs AuthorizationExecuteWithPrivileges](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg)
- [Death by 1000 installers; it's all broken!](https://speakerdeck.com/patrickwardle/defcon-2017-death-by-1000-installers-its-all-broken?slide=8)
- [Carbon Black Shlayer Feb 2019](https://www.carbonblack.com/2019/02/12/tau-threat-intelligence-notification-new-macos-malware-variant-of-shlayer-osx-discovered/)
- [OSX Coldroot RAT](https://objective-see.com/blog/blog_0x2A.html)
