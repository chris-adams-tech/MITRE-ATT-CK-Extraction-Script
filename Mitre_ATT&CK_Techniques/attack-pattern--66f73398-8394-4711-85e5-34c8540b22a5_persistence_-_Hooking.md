---
id: attack-pattern--66f73398-8394-4711-85e5-34c8540b22a5
mitre_attack_url: https://attack.mitre.org/techniques/T1179
name: Hooking
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
- credential-access
title: persistence - Hooking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation, credential-access |
| **Platforms** | Windows |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1179](https://attack.mitre.org/techniques/T1179) |

# Hooking (attack-pattern--66f73398-8394-4711-85e5-34c8540b22a5)

## Description
Windows processes often leverage application programming interface (API) functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. 

Hooking involves redirecting calls to these functions and can be implemented via:

* **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. (Citation: Microsoft Hook Overview) (Citation: Elastic Process Injection July 2017)
* **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored. (Citation: Elastic Process Injection July 2017) (Citation: Adlice Software IAT Hooks Oct 2014) (Citation: MWRInfoSecurity Dynamic Hooking 2015)
* **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow. (Citation: Elastic Process Injection July 2017) (Citation: HighTech Bridge Inline Hooking Sept 2011) (Citation: MWRInfoSecurity Dynamic Hooking 2015)

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), adversaries may use hooking to load and execute malicious code within the context of another process, masking the execution while also allowing access to the process's memory and possibly elevated privileges. Installing hooking mechanisms may also provide Persistence via continuous invocation when the functions are called through normal use.

Malicious hooking mechanisms may also capture API calls that include parameters that reveal user authentication credentials for Credential Access. (Citation: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017)

Hooking is commonly utilized by [Rootkit](https://attack.mitre.org/techniques/T1014)s to conceal files, processes, Registry keys, and other objects in order to hide malware and associated behaviors. (Citation: Symantec Windows Rootkits)

## Detection
Monitor for calls to the SetWindowsHookEx and SetWinEventHook functions, which install a hook procedure. (Citation: Microsoft Hook Overview) (Citation: Volatility Detecting Hooks Sept 2012) Also consider analyzing hook chains (which hold pointers to hook procedures for each type of hook) using tools  (Citation: Volatility Detecting Hooks Sept 2012) (Citation: PreKageo Winhook Jul 2011) (Citation: Jay GetHooks Sept 2011) or by programmatically examining internal kernel structures. (Citation: Zairon Hooking Dec 2006) (Citation: EyeofRa Detecting Hooking June 2017)

Rootkits detectors  (Citation: GMER Rootkits) can also be used to monitor for various flavors of hooking activity.

Verify integrity of live processes by comparing code in memory to that of corresponding static binaries, specifically checking for jumps and other instructions that redirect code flow. Also consider taking snapshots of newly started processes  (Citation: Microsoft Process Snapshot) to compare the in-memory IAT to the real addresses of the referenced functions. (Citation: StackExchange Hooks Jul 2012) (Citation: Adlice Software IAT Hooks Oct 2014)

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1179)
- [Microsoft Hook Overview](https://msdn.microsoft.com/library/windows/desktop/ms644959.aspx)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [Adlice Software IAT Hooks Oct 2014](https://www.adlice.com/userland-rootkits-part-1-iat-hooks/)
- [MWRInfoSecurity Dynamic Hooking 2015](https://www.mwrinfosecurity.com/our-thinking/dynamic-hooking-techniques-user-mode/)
- [HighTech Bridge Inline Hooking Sept 2011](https://www.exploit-db.com/docs/17802.pdf)
- [Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=TrojanSpy:Win32/Ursnif.gen!I&threatId=-2147336918)
- [Symantec Windows Rootkits](https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf)
- [Volatility Detecting Hooks Sept 2012](https://volatility-labs.blogspot.com/2012/09/movp-31-detecting-malware-hooks-in.html)
- [PreKageo Winhook Jul 2011](https://github.com/prekageo/winhook)
- [Jay GetHooks Sept 2011](https://github.com/jay/gethooks)
- [Zairon Hooking Dec 2006](https://zairon.wordpress.com/2006/12/06/any-application-defined-hook-procedure-on-my-machine/)
- [EyeofRa Detecting Hooking June 2017](https://eyeofrablog.wordpress.com/2017/06/27/windows-keylogger-part-2-defense-against-user-land/)
- [GMER Rootkits](http://www.gmer.net/)
- [Microsoft Process Snapshot](https://msdn.microsoft.com/library/windows/desktop/ms686701.aspx)
- [StackExchange Hooks Jul 2012](https://security.stackexchange.com/questions/17904/what-are-the-methods-to-find-hooked-functions-and-apis)
