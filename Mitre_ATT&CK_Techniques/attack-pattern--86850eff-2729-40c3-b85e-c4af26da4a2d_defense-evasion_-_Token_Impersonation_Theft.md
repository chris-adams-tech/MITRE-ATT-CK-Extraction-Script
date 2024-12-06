---
contributors:
- Jonny Johnson
data_sources:
- 'Command: Command Execution'
- 'Process: OS API Execution'
id: attack-pattern--86850eff-2729-40c3-b85e-c4af26da4a2d
mitre_attack_url: https://attack.mitre.org/techniques/T1134/001
name: Token Impersonation/Theft
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Token Impersonation/Theft
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134/001](https://attack.mitre.org/techniques/T1134/001) |

# Token Impersonation/Theft (attack-pattern--86850eff-2729-40c3-b85e-c4af26da4a2d)

## Description
Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`.(Citation: DuplicateToken function) The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate a logged on user's security context, or with `SetThreadToken` to assign the impersonated token to a thread.

An adversary may perform [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) when they have a specific, existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has a non-network logon session on the system.

When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process, they can additionally [Create Process with Token](https://attack.mitre.org/techniques/T1134/002) using `CreateProcessWithTokenW` or `CreateProcessAsUserW`. [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) is also distinct from [Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003) in that it refers to duplicating an existing token, rather than creating a new one.

## Detection
If an adversary is using a standard command-line shell, analysts can detect token manipulation by auditing command-line activity. Specifically, analysts should look for use of the <code>runas</code> command. Detailed command-line logging is not enabled by default in Windows.(Citation: Microsoft Command-line Logging)

Analysts can also monitor for use of Windows APIs such as <code>DuplicateToken(Ex)</code>, <code> ImpersonateLoggedOnUser </code>, and <code> SetThreadToken </code> and correlate activity with other suspicious behavior to reduce false positives that may be due to normal benign use by users and administrators.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134/001)
- [Microsoft Command-line Logging](https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/manage/component-updates/command-line-process-auditing)
- [DuplicateToken function](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken)
