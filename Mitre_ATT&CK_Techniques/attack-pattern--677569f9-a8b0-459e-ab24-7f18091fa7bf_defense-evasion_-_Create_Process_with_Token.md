---
contributors:
- Vadim Khrykov
- Jonny Johnson
data_sources:
- 'Command: Command Execution'
- 'Process: OS API Execution'
id: attack-pattern--677569f9-a8b0-459e-ab24-7f18091fa7bf
mitre_attack_url: https://attack.mitre.org/techniques/T1134/002
name: Create Process with Token
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Create Process with Token
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134/002](https://attack.mitre.org/techniques/T1134/002) |

# Create Process with Token (attack-pattern--677569f9-a8b0-459e-ab24-7f18091fa7bf)

## Description
Adversaries may create a new process with an existing token to escalate privileges and bypass access controls. Processes can be created with the token and resulting security context of another user using features such as <code>CreateProcessWithTokenW</code> and <code>runas</code>.(Citation: Microsoft RunAs)

Creating processes with a token not associated with the current user may require the credentials of the target user, specific privileges to impersonate that user, or access to the token to be used. For example, the token could be duplicated via [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) or created via [Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003) before being used to create a process.

While this technique is distinct from [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001), the techniques can be used in conjunction where a token is duplicated and then used to create a new process.

## Detection
If an adversary is using a standard command-line shell (i.e. [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003)), analysts may detect token manipulation by auditing command-line activity. Specifically, analysts should look for use of the <code>runas</code> command or similar artifacts. Detailed command-line logging is not enabled by default in Windows.(Citation: Microsoft Command-line Logging)

If an adversary is using a payload that calls the Windows token APIs directly, analysts may detect token manipulation only through careful analysis of user activity, examination of running processes, and correlation with other endpoint and network behavior.

Analysts can also monitor for use of Windows APIs such as <code>CreateProcessWithTokenW</code> and correlate activity with other suspicious behavior to reduce false positives that may be due to normal benign use by users and administrators.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134/002)
- [Microsoft Command-line Logging](https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/manage/component-updates/command-line-process-auditing)
- [Microsoft RunAs](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11))
