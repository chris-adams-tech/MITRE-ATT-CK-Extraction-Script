---
contributors:
- Gordon Long, Box, Inc., @ethicalhax
- Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
- Nathaniel Quist, Palo Alto Networks
- Gal Singer, @galsinger29, Team Nautilus Aqua Security
- Daniel Feichter, @VirtualAllocEx, Infosec Tirol
- Cian Heasley
- Alex Soler, AttackIQ
- Sarathkumar Rajendran, Microsoft Defender365
- Lucas Heiligenstein
data_sources:
- 'Sensor Health: Host Status'
- 'Process: Process Termination'
- 'Process: Process Creation'
- 'Service: Service Metadata'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Windows Registry: Windows Registry Key Deletion'
- 'Driver: Driver Load'
id: attack-pattern--ac08589e-ee59-4935-8667-d845e38fe579
mitre_attack_url: https://attack.mitre.org/techniques/T1562/001
name: Disable or Modify Tools
platforms:
- Windows
- macOS
- Linux
- Containers
- IaaS
- Network
tactics:
- defense-evasion
title: defense-evasion - Disable or Modify Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, macOS, Linux, Containers, IaaS, Network |
| **Data Sources** | Sensor Health: Host Status, Process: Process Termination, Process: Process Creation, Service: Service Metadata, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Windows Registry: Windows Registry Key Deletion, Driver: Driver Load |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/001](https://attack.mitre.org/techniques/T1562/001) |

# Disable or Modify Tools (attack-pattern--ac08589e-ee59-4935-8667-d845e38fe579)

## Description
Adversaries may modify and/or disable security tools to avoid possible detection of their malware/tools and activities. This may take many forms, such as killing security software processes or services, modifying / deleting Registry keys or configuration files so that tools do not operate properly, or other methods to interfere with security tools scanning or reporting information. Adversaries may also disable updates to prevent the latest security patches from reaching tools on victim systems.(Citation: SCADAfence_ransomware)

Adversaries may also tamper with artifacts deployed and utilized by security tools. Security tools may make dynamic changes to system components in order to maintain visibility into specific events. For example, security products may load their own modules and/or modify those loaded by processes to facilitate data collection. Similar to [Indicator Blocking](https://attack.mitre.org/techniques/T1562/006), adversaries may unhook or otherwise modify these features added by tools (especially those that exist in userland or are otherwise potentially accessible to adversaries) to avoid detection.(Citation: OutFlank System Calls)(Citation: MDSec System Calls) 

Adversaries may also focus on specific applications such as Sysmon. For example, the “Start” and “Enable” values in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Microsoft-Windows-Sysmon-Operational</code> may be modified to tamper with and potentially disable Sysmon logging.(Citation: disable_win_evt_logging) 

On network devices, adversaries may attempt to skip digital signature verification checks by altering startup configuration files and effectively disabling firmware verification that typically occurs at boot.(Citation: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation)(Citation: Analysis of FG-IR-22-369)

In cloud environments, tools disabled by adversaries may include cloud monitoring agents that report back to services such as AWS CloudWatch or Google Cloud Monitor.

Furthermore, although defensive tools may have anti-tampering mechanisms, adversaries may abuse tools such as legitimate rootkit removal kits to impair and/or disable these tools.(Citation: chasing_avaddon_ransomware)(Citation: dharma_ransomware)(Citation: demystifying_ryuk)(Citation: doppelpaymer_crowdstrike) For example, adversaries have used tools such as GMER to find and shut down hidden processes and antivirus software on infected systems.(Citation: demystifying_ryuk)

Additionally, adversaries may exploit legitimate drivers from anti-virus software to gain access to kernel space (i.e. [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068)), which may lead to bypassing anti-tampering features.(Citation: avoslocker_ransomware)

## Detection
Monitor processes and command-line arguments to see if security tools/services are killed or stop running. Monitor Registry edits for modifications to services and startup programs that correspond to security tools. Monitoring for changes to other known features used by deployed security tools may also expose malicious activity.

Lack of expected log events may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/001)
- [Analysis of FG-IR-22-369](https://www.fortinet.com/blog/psirt-blogs/fg-ir-22-369-psirt-analysis)
- [Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [OutFlank System Calls](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)
- [disable_win_evt_logging](https://ptylu.github.io/content/report/report.html?report=25)
- [chasing_avaddon_ransomware](https://www.mandiant.com/resources/chasing-avaddon-ransomware)
- [doppelpaymer_crowdstrike](https://www.crowdstrike.com/blog/how-doppelpaymer-hunts-and-kills-windows-processes/)
- [avoslocker_ransomware](https://thehackernews.com/2022/05/avoslocker-ransomware-variant-using-new.html)
- [dharma_ransomware](https://www.crowdstrike.com/blog/targeted-dharma-ransomware-intrusions-exhibit-consistent-techniques/)
- [MDSec System Calls](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)
- [SCADAfence_ransomware](https://cdn.logic-control.com/docs/scadafence/Anatomy-Of-A-Targeted-Ransomware-Attack-WP.pdf)
- [demystifying_ryuk](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/demystifying-ransomware-attacks-against-microsoft-defender/ba-p/1928947)
