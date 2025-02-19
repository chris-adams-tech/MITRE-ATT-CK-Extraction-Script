---
contributors:
- Tom Ueltschi @c_APT_ure
- Travis Smith, Tripwire
- Robby Winchester, @robwinchester3
- Jared Atkinson, @jaredcatkinson
data_sources:
- 'Process: OS API Execution'
- 'Command: Command Execution'
- 'User Account: User Account Metadata'
- 'Process: Process Metadata'
- 'Process: Process Creation'
- 'Active Directory: Active Directory Object Modification'
id: attack-pattern--dcaa092b-7de9-4a21-977f-7fcb77e89c48
mitre_attack_url: https://attack.mitre.org/techniques/T1134
name: Access Token Manipulation
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Access Token Manipulation
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Process: OS API Execution, Command: Command Execution, User Account: User Account Metadata, Process: Process Metadata, Process: Process Creation, Active Directory: Active Directory Object Modification |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1134](https://attack.mitre.org/techniques/T1134) |

# Access Token Manipulation (attack-pattern--dcaa092b-7de9-4a21-977f-7fcb77e89c48)

## Description
Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001)) or used to spawn a new process (i.e. [Create Process with Token](https://attack.mitre.org/techniques/T1134/002)). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.(Citation: Pentestlab Token Manipulation)

Any standard user can use the <code>runas</code> command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Detection
If an adversary is using a standard command-line shell, analysts can detect token manipulation by auditing command-line activity. Specifically, analysts should look for use of the <code>runas</code> command. Detailed command-line logging is not enabled by default in Windows.(Citation: Microsoft Command-line Logging)

If an adversary is using a payload that calls the Windows token APIs directly, analysts can detect token manipulation only through careful analysis of user network activity, examination of running processes, and correlation with other endpoint and network behavior. 

There are many Windows API calls a payload can take advantage of to manipulate access tokens (e.g., <code>LogonUser</code> (Citation: Microsoft LogonUser), <code>DuplicateTokenEx</code>(Citation: Microsoft DuplicateTokenEx), and <code>ImpersonateLoggedOnUser</code>(Citation: Microsoft ImpersonateLoggedOnUser)). Please see the referenced Windows API pages for more information.

Query systems for process and thread token information and look for inconsistencies such as user owns processes impersonating the local SYSTEM account.(Citation: BlackHat Atkinson Winchester Token Manipulation)

Look for inconsistencies between the various fields that store PPID information, such as the EventHeader ProcessId from data collected via Event Tracing for Windows (ETW), Creator Process ID/Name from Windows event logs, and the ProcessID and ParentProcessID (which are also produced from ETW and other utilities such as Task Manager and Process Explorer). The ETW provided EventHeader ProcessId identifies the actual parent process.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1134)
- [BlackHat Atkinson Winchester Token Manipulation](https://www.blackhat.com/docs/eu-17/materials/eu-17-Atkinson-A-Process-Is-No-One-Hunting-For-Token-Manipulation.pdf)
- [Microsoft Command-line Logging](https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/manage/component-updates/command-line-process-auditing)
- [Microsoft LogonUser](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378184(v=vs.85).aspx)
- [Microsoft DuplicateTokenEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa446617(v=vs.85).aspx)
- [Microsoft ImpersonateLoggedOnUser](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378612(v=vs.85).aspx)
- [Pentestlab Token Manipulation](https://pentestlab.blog/2017/04/03/token-manipulation/)
