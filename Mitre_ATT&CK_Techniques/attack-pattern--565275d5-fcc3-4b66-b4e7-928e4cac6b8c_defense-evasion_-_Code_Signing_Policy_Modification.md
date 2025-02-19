---
contributors:
- Abel Morales, Exabeam
data_sources:
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
id: attack-pattern--565275d5-fcc3-4b66-b4e7-928e4cac6b8c
mitre_attack_url: https://attack.mitre.org/techniques/T1553/006
name: Code Signing Policy Modification
platforms:
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - Code Signing Policy Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS |
| **Data Sources** | Command: Command Execution, Windows Registry: Windows Registry Key Modification, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553/006](https://attack.mitre.org/techniques/T1553/006) |

# Code Signing Policy Modification (attack-pattern--565275d5-fcc3-4b66-b4e7-928e4cac6b8c)

## Description
Adversaries may modify code signing policies to enable execution of unsigned or self-signed code. Code signing provides a level of authenticity on a program from a developer and a guarantee that the program has not been tampered with. Security controls can include enforcement mechanisms to ensure that only valid, signed code can be run on an operating system. 

Some of these security controls may be enabled by default, such as Driver Signature Enforcement (DSE) on Windows or System Integrity Protection (SIP) on macOS.(Citation: Microsoft DSE June 2017)(Citation: Apple Disable SIP) Other such controls may be disabled by default but are configurable through application controls, such as only allowing signed Dynamic-Link Libraries (DLLs) to execute on a system. Since it can be useful for developers to modify default signature enforcement policies during the development and testing of applications, disabling of these features may be possible with elevated permissions.(Citation: Microsoft Unsigned Driver Apr 2017)(Citation: Apple Disable SIP)

Adversaries may modify code signing policies in a number of ways, including through use of command-line or GUI utilities, [Modify Registry](https://attack.mitre.org/techniques/T1112), rebooting the computer in a debug/recovery mode, or by altering the value of variables in kernel memory.(Citation: Microsoft TESTSIGNING Feb 2021)(Citation: Apple Disable SIP)(Citation: FireEye HIKIT Rootkit Part 2)(Citation: GitHub Turla Driver Loader) Examples of commands that can modify the code signing policy of a system include <code>bcdedit.exe -set TESTSIGNING ON</code> on Windows and <code>csrutil disable</code> on macOS.(Citation: Microsoft TESTSIGNING Feb 2021)(Citation: Apple Disable SIP) Depending on the implementation, successful modification of a signing policy may require reboot of the compromised system. Additionally, some implementations can introduce visible artifacts for the user (ex: a watermark in the corner of the screen stating the system is in Test Mode). Adversaries may attempt to remove such artifacts.(Citation: F-Secure BlackEnergy 2014)

To gain access to kernel memory to modify variables related to signature checks, such as modifying <code>g_CiOptions</code> to disable Driver Signature Enforcement, adversaries may conduct [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068) using a signed, but vulnerable driver.(Citation: Unit42 AcidBox June 2020)(Citation: GitHub Turla Driver Loader)

## Detection
Monitor processes and command-line arguments for actions that could be taken to modify the code signing policy of a system, such as <code>bcdedit.exe -set TESTSIGNING ON</code>.(Citation: Microsoft TESTSIGNING Feb 2021) Consider monitoring for modifications made to Registry keys associated with code signing policies, such as <code>HKCU\Software\Policies\Microsoft\Windows NT\Driver Signing</code>. Modifications to the code signing policy of a system are likely to be rare.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553/006)
- [Apple Disable SIP](https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection)
- [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [FireEye HIKIT Rootkit Part 2](https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-2.html)
- [Microsoft Unsigned Driver Apr 2017](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/installing-an-unsigned-driver-during-development-and-test)
- [Microsoft DSE June 2017](https://docs.microsoft.com/en-us/previous-versions/windows/hardware/design/dn653559(v=vs.85)?redirectedfrom=MSDN)
- [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)
- [Unit42 AcidBox June 2020](https://unit42.paloaltonetworks.com/acidbox-rare-malware/)
- [GitHub Turla Driver Loader](https://github.com/hfiref0x/TDL)
