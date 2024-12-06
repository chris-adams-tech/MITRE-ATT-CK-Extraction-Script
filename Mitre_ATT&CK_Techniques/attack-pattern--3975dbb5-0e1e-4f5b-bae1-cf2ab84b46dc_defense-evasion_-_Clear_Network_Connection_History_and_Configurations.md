---
contributors:
- CrowdStrike Falcon OverWatch
data_sources:
- 'Process: Process Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'Firewall: Firewall Rule Modification'
- 'File: File Modification'
id: attack-pattern--3975dbb5-0e1e-4f5b-bae1-cf2ab84b46dc
mitre_attack_url: https://attack.mitre.org/techniques/T1070/007
name: Clear Network Connection History and Configurations
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- defense-evasion
title: defense-evasion - Clear Network Connection History and Configurations
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Process: Process Creation, Windows Registry: Windows Registry Key Modification, Command: Command Execution, Firewall: Firewall Rule Modification, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1070/007](https://attack.mitre.org/techniques/T1070/007) |

# Clear Network Connection History and Configurations (attack-pattern--3975dbb5-0e1e-4f5b-bae1-cf2ab84b46dc)

## Description
Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as [Remote Services](https://attack.mitre.org/techniques/T1021) or [External Remote Services](https://attack.mitre.org/techniques/T1133). Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries.

Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows Registry values under (Citation: Microsoft RDP Removal):

* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code>
* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code>

Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code> and `C:\Users\%username%\AppData\Local\Microsoft\Terminal
Server Client\Cache\`.(Citation: Moran RDPieces) Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`).(Citation: Apple Culprit Access)(Citation: FreeDesktop Journal)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

Malicious network connections may also require changes to third-party applications or network configuration settings, such as [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004) or tampering to enable [Proxy](https://attack.mitre.org/techniques/T1090). Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1070/007)
- [FreeDesktop Journal](https://www.freedesktop.org/software/systemd/man/systemd-journald.service.html)
- [Microsoft RDP Removal](https://docs.microsoft.com/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer)
- [Moran RDPieces](https://www.osdfcon.org/presentations/2020/Brian-Moran_Putting-Together-the-RDPieces.pdf)
- [Apple Culprit Access](https://discussions.apple.com/thread/3991574)
- [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
