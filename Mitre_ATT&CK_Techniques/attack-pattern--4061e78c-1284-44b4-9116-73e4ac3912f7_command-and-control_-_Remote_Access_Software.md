---
contributors:
- Matt Kelly, @breakersall
- Zachary Stanford, @svch0st
- Dray Agha, @Purp1eW0lf, Huntress Labs
data_sources:
- 'Process: Process Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--4061e78c-1284-44b4-9116-73e4ac3912f7
mitre_attack_url: https://attack.mitre.org/techniques/T1219
name: Remote Access Software
platforms:
- Linux
- Windows
- macOS
tactics:
- command-and-control
title: command-and-control - Remote Access Software
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, Windows, macOS |
| **Data Sources** | Process: Process Creation, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1219](https://attack.mitre.org/techniques/T1219) |

# Remote Access Software (attack-pattern--4061e78c-1284-44b4-9116-73e4ac3912f7)

## Description
An adversary may use legitimate desktop support and remote access software to establish an interactive command and control channel to target systems within networks. These services, such as `VNC`, `Team Viewer`, `AnyDesk`, `ScreenConnect`, `LogMein`, `AmmyyAdmin`, and other remote monitoring and management (RMM) tools, are commonly used as legitimate technical support software and may be allowed by application control within a target environment.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy)

Remote access software may be installed and used post-compromise as an alternate communications channel for redundant access or as a way to establish an interactive remote desktop session with the target system. They may also be used as a component of malware to establish a reverse connection or back-connect to a service or adversary-controlled system.
 
Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.

Installation of many remote access software may also include persistence (e.g., the software's installation routine creates a [Windows Service](https://attack.mitre.org/techniques/T1543/003)). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).(Citation: Google Chrome Remote Desktop)(Citation: Chrome Remote Desktop)

## Detection
Monitor for applications and processes related to remote admin tools. Correlate activity with other suspicious behavior that may reduce false positives if these tools are used by legitimate users and administrators.

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect application layer protocols that do not follow the expected protocol for the port that is being used.

[Domain Fronting](https://attack.mitre.org/techniques/T1090/004) may be used in conjunction to avoid defenses. Adversaries will likely need to deploy and/or install these remote tools to compromised systems. It may be possible to detect or prevent the installation of these tools with host-based solutions.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1219)
- [CrowdStrike 2015 Global Threat Report](https://go.crowdstrike.com/rs/281-OBQ-266/images/15GlobalThreatReport.pdf)
- [CrySyS Blog TeamSpy](https://blog.crysys.hu/2013/03/teamspy/)
- [Google Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523)
- [Chrome Remote Desktop](https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708)
- [Symantec Living off the Land](https://www.symantec.com/content/dam/symantec/docs/security-center/white-papers/istr-living-off-the-land-and-fileless-attack-techniques-en.pdf)
