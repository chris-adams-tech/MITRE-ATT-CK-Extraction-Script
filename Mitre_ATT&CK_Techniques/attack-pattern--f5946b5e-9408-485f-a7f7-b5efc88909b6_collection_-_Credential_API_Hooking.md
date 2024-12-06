---
data_sources:
- 'Process: Process Metadata'
- 'Process: OS API Execution'
id: attack-pattern--f5946b5e-9408-485f-a7f7-b5efc88909b6
mitre_attack_url: https://attack.mitre.org/techniques/T1056/004
name: Credential API Hooking
platforms:
- Windows
tactics:
- collection
- credential-access
title: collection - Credential API Hooking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | collection, credential-access |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Metadata, Process: OS API Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1056/004](https://attack.mitre.org/techniques/T1056/004) |

# Credential API Hooking (attack-pattern--f5946b5e-9408-485f-a7f7-b5efc88909b6)

## Description
Adversaries may hook into Windows application programming interface (API) functions to collect user credentials. Malicious hooking mechanisms may capture API calls that include parameters that reveal user authentication credentials.(Citation: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017) Unlike [Keylogging](https://attack.mitre.org/techniques/T1056/001),  this technique focuses specifically on API functions that include parameters that reveal user credentials. Hooking involves redirecting calls to these functions and can be implemented via:

* **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs.(Citation: Microsoft Hook Overview)(Citation: Elastic Process Injection July 2017)
* **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored.(Citation: Elastic Process Injection July 2017)(Citation: Adlice Software IAT Hooks Oct 2014)(Citation: MWRInfoSecurity Dynamic Hooking 2015)
* **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow.(Citation: Elastic Process Injection July 2017)(Citation: HighTech Bridge Inline Hooking Sept 2011)(Citation: MWRInfoSecurity Dynamic Hooking 2015)


## Detection
Monitor for calls to the `SetWindowsHookEx` and `SetWinEventHook` functions, which install a hook procedure.(Citation: Microsoft Hook Overview)(Citation: Volatility Detecting Hooks Sept 2012) Also consider analyzing hook chains (which hold pointers to hook procedures for each type of hook) using tools(Citation: Volatility Detecting Hooks Sept 2012)(Citation: PreKageo Winhook Jul 2011)(Citation: Jay GetHooks Sept 2011) or by programmatically examining internal kernel structures.(Citation: Zairon Hooking Dec 2006)(Citation: EyeofRa Detecting Hooking June 2017)

Rootkits detectors(Citation: GMER Rootkits) can also be used to monitor for various types of hooking activity.

Verify integrity of live processes by comparing code in memory to that of corresponding static binaries, specifically checking for jumps and other instructions that redirect code flow. Also consider taking snapshots of newly started processes(Citation: Microsoft Process Snapshot) to compare the in-memory IAT to the real addresses of the referenced functions.(Citation: StackExchange Hooks Jul 2012)(Citation: Adlice Software IAT Hooks Oct 2014)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1056/004)
- [EyeofRa Detecting Hooking June 2017](https://eyeofrablog.wordpress.com/2017/06/27/windows-keylogger-part-2-defense-against-user-land/)
- [Zairon Hooking Dec 2006](https://zairon.wordpress.com/2006/12/06/any-application-defined-hook-procedure-on-my-machine/)
- [GMER Rootkits](http://www.gmer.net/)
- [MWRInfoSecurity Dynamic Hooking 2015](https://www.mwrinfosecurity.com/our-thinking/dynamic-hooking-techniques-user-mode/)
- [Elastic Process Injection July 2017](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process)
- [HighTech Bridge Inline Hooking Sept 2011](https://www.exploit-db.com/docs/17802.pdf)
- [Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=TrojanSpy:Win32/Ursnif.gen!I&threatId=-2147336918)
- [Microsoft Hook Overview](https://msdn.microsoft.com/library/windows/desktop/ms644959.aspx)
- [Microsoft Process Snapshot](https://msdn.microsoft.com/library/windows/desktop/ms686701.aspx)
- [PreKageo Winhook Jul 2011](https://github.com/prekageo/winhook)
- [Jay GetHooks Sept 2011](https://github.com/jay/gethooks)
- [StackExchange Hooks Jul 2012](https://security.stackexchange.com/questions/17904/what-are-the-methods-to-find-hooked-functions-and-apis)
- [Adlice Software IAT Hooks Oct 2014](https://www.adlice.com/userland-rootkits-part-1-iat-hooks/)
- [Volatility Detecting Hooks Sept 2012](https://volatility-labs.blogspot.com/2012/09/movp-31-detecting-malware-hooks-in.html)
