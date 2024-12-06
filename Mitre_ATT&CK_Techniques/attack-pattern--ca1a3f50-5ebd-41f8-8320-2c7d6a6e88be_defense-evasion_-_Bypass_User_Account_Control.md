---
contributors:
- Stefan Kanthak
- Casey Smith
id: attack-pattern--ca1a3f50-5ebd-41f8-8320-2c7d6a6e88be
mitre_attack_url: https://attack.mitre.org/techniques/T1088
name: Bypass User Account Control
platforms:
- Windows
tactics:
- defense-evasion
- privilege-escalation
title: defense-evasion - Bypass User Account Control
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, privilege-escalation |
| **Platforms** | Windows |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1088](https://attack.mitre.org/techniques/T1088) |

# Bypass User Account Control (attack-pattern--ca1a3f50-5ebd-41f8-8320-2c7d6a6e88be)

## Description
Windows User Account Control (UAC) allows a program to elevate its privileges to perform a task under administrator-level permissions by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action. (Citation: TechNet How UAC Works)

If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs are allowed to elevate privileges or execute some elevated COM objects without prompting the user through the UAC notification box. (Citation: TechNet Inside UAC) (Citation: MSDN COM Elevation) An example of this is use of rundll32.exe to load a specifically crafted DLL which loads an auto-elevated COM object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user. (Citation: Davidson Windows) Adversaries can use these techniques to elevate privileges to administrator if the target process is unprotected.

Many methods have been discovered to bypass UAC. The Github readme page for UACMe contains an extensive list of methods (Citation: Github UACMe) that have been discovered and implemented within UACMe, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as:

* <code>eventvwr.exe</code> can auto-elevate and execute a specified binary or script. (Citation: enigma0x3 Fileless UAC Bypass) (Citation: Fortinet Fareit)

Another bypass is possible through some Lateral Movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on lateral systems and default to high integrity. (Citation: SANS UAC Bypass)

## Detection
There are many ways to perform UAC bypasses when a user is in the local administrator group on a system, so it may be difficult to target detection on all variations. Efforts should likely be placed on mitigation and collecting enough information on process launches and actions that could be performed before and after a UAC bypass is performed. Monitor process API calls for behavior that may be indicative of [Process Injection](https://attack.mitre.org/techniques/T1055) and unusual loaded DLLs through [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1038), which indicate attempts to gain access to higher privileged processes.

Some UAC bypass methods rely on modifying specific, user-accessible Registry settings. For example:

* The <code>eventvwr.exe</code> bypass uses the <code>[HKEY_CURRENT_USER]\Software\Classes\mscfile\shell\open\command</code> Registry key. (Citation: enigma0x3 Fileless UAC Bypass)
* The <code>sdclt.exe</code> bypass uses the <code>[HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe</code> and <code>[HKEY_CURRENT_USER]\Software\Classes\exefile\shell\runas\command\isolatedCommand</code> Registry keys. (Citation: enigma0x3 sdclt app paths) (Citation: enigma0x3 sdclt bypass)

Analysts should monitor these Registry settings for unauthorized changes.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1088)
- [TechNet How UAC Works](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works)
- [TechNet Inside UAC](https://technet.microsoft.com/en-US/magazine/2009.07.uac.aspx)
- [MSDN COM Elevation](https://msdn.microsoft.com/en-us/library/ms679687.aspx)
- [Davidson Windows](http://www.pretentiousname.com/misc/win7_uac_whitelist2.html)
- [Github UACMe](https://github.com/hfiref0x/UACME)
- [enigma0x3 Fileless UAC Bypass](https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/)
- [Fortinet Fareit](https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware)
- [SANS UAC Bypass](http://pen-testing.sans.org/blog/pen-testing/2013/08/08/psexec-uac-bypass)
- [enigma0x3 sdclt app paths](https://enigma0x3.net/2017/03/14/bypassing-uac-using-app-paths/)
- [enigma0x3 sdclt bypass](https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdclt-exe/)
