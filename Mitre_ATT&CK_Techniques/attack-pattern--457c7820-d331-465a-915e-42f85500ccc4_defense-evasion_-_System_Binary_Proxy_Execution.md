---
contributors:
- Nishan Maharjan, @loki248
- "Hans Christoffer Gaardl\xF8s"
- Praetorian
- Wes Hurd
data_sources:
- 'Network Traffic: Network Connection Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
- 'File: File Creation'
- 'Process: OS API Execution'
- 'Process: Process Creation'
- 'Command: Command Execution'
id: attack-pattern--457c7820-d331-465a-915e-42f85500ccc4
mitre_attack_url: https://attack.mitre.org/techniques/T1218
name: System Binary Proxy Execution
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - System Binary Proxy Execution
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Network Traffic: Network Connection Creation, Windows Registry: Windows Registry Key Modification, Module: Module Load, File: File Creation, Process: OS API Execution, Process: Process Creation, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218](https://attack.mitre.org/techniques/T1218) |

# System Binary Proxy Execution (attack-pattern--457c7820-d331-465a-915e-42f85500ccc4)

## Description
Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system.(Citation: LOLBAS Project) Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands.

Similarly, on Linux systems adversaries may abuse trusted binaries such as <code>split</code> to proxy execution of malicious commands.(Citation: split man page)(Citation: GTFO split)

## Detection
Monitor processes and command-line parameters for signed binaries that may be used to proxy execution of malicious files. Compare recent invocations of signed binaries that may be used to proxy execution with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity. Legitimate programs used in suspicious ways, like msiexec.exe downloading an MSI file from the Internet, may be indicative of an intrusion. Correlate activity with other suspicious behavior to reduce false positives that may be due to normal benign use by users and administrators.

Monitor for file activity (creations, downloads, modifications, etc.), especially for file types that are not typical within an environment and may be indicative of adversary activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218)
- [GTFO split](https://gtfobins.github.io/gtfobins/split/)
- [LOLBAS Project](https://github.com/LOLBAS-Project/LOLBAS#criteria)
- [split man page](https://man7.org/linux/man-pages/man1/split.1.html)
