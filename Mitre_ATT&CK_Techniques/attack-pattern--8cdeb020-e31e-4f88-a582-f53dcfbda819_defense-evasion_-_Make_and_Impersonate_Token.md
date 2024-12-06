---
contributors:
- Jonny Johnson
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
id: attack-pattern--8cdeb020-e31e-4f88-a582-f53dcfbda819
mitre_attack_url: https://attack.mitre.org/techniques/T1134/003
name: Make and Impersonate Token
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Make and Impersonate Token
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution, Command: Command Execution |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134/003](https://attack.mitre.org/techniques/T1134/003) |

# Make and Impersonate Token (attack-pattern--8cdeb020-e31e-4f88-a582-f53dcfbda819)

## Description
Adversaries may make new tokens and impersonate users to escalate privileges and bypass access controls. For example, if an adversary has a username and password but the user is not logged onto the system the adversary can then create a logon session for the user using the `LogonUser` function.(Citation: LogonUserW function) The function will return a copy of the new session's access token and the adversary can use `SetThreadToken` to assign the token to a thread.

This behavior is distinct from [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) in that this refers to creating a new user token instead of stealing or duplicating an existing one.

## Detection
If an adversary is using a standard command-line shell, analysts can detect token manipulation by auditing command-line activity. Specifically, analysts should look for use of the <code>runas</code> command. Detailed command-line logging is not enabled by default in Windows.(Citation: Microsoft Command-line Logging)

If an adversary is using a payload that calls the Windows token APIs directly, analysts can detect token manipulation only through careful analysis of user network activity, examination of running processes, and correlation with other endpoint and network behavior.

Analysts can also monitor for use of Windows APIs such as <code>LogonUser</code> and <code> SetThreadToken</code> and correlate activity with other suspicious behavior to reduce false positives that may be due to normal benign use by users and administrators.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134/003)
- [Microsoft Command-line Logging](https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/manage/component-updates/command-line-process-auditing)
- [LogonUserW function](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-logonuserw)
