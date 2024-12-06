---
contributors:
- Dan Borges, @1njection
data_sources:
- 'Module: Module Load'
- 'Network Traffic: Network Connection Creation'
- 'Command: Command Execution'
- 'Network Share: Network Share Access'
- 'WMI: WMI Creation'
- 'Logon Session: Logon Session Creation'
- 'Network Traffic: Network Traffic Flow'
- 'Process: Process Creation'
id: attack-pattern--54a649ff-439a-41a4-9856-8d144a2551ba
mitre_attack_url: https://attack.mitre.org/techniques/T1021
name: Remote Services
platforms:
- Linux
- macOS
- Windows
- IaaS
tactics:
- lateral-movement
title: lateral-movement - Remote Services
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS, Windows, IaaS |
| **Data Sources** | Module: Module Load, Network Traffic: Network Connection Creation, Command: Command Execution, Network Share: Network Share Access, WMI: WMI Creation, Logon Session: Logon Session Creation, Network Traffic: Network Traffic Flow, Process: Process Creation |
| **System Requirements** | Active remote service accepting connections and valid credentials |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021](https://attack.mitre.org/techniques/T1021) |

# Remote Services (attack-pattern--54a649ff-439a-41a4-9856-8d144a2551ba)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).(Citation: SSH Secure Shell)(Citation: TechNet Remote Desktop Services) They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain. 

Legitimate applications (such as [Software Deployment Tools](https://attack.mitre.org/techniques/T1072) and other administrative programs) may utilize [Remote Services](https://attack.mitre.org/techniques/T1021) to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [VNC](https://attack.mitre.org/techniques/T1021/005) to send the screen and control buffers and [SSH](https://attack.mitre.org/techniques/T1021/004) for secure file transfer.(Citation: Remote Management MDM macOS)(Citation: Kickstart Apple Remote Desktop commands)(Citation: Apple Remote Desktop Admin Guide 3.3) Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.(Citation: FireEye 2019 Apple Remote Desktop)(Citation: Lockboxx ARD 2019)(Citation: Kickstart Apple Remote Desktop commands)

## Detection
Correlate use of login activity related to remote services with unusual behavior or other malicious or suspicious activity. Adversaries will likely need to learn about an environment and the relationships between systems through Discovery techniques prior to attempting Lateral Movement. 

Use of applications such as ARD may be legitimate depending on the environment and how it’s used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior using these applications. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time. 

In macOS, you can review logs for "screensharingd" and "Authentication" event messages. Monitor network connections regarding remote management (ports tcp:3283 and tcp:5900) and for remote login (port tcp:22).(Citation: Lockboxx ARD 2019)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021)
- [Apple Remote Desktop Admin Guide 3.3](https://images.apple.com/remotedesktop/pdf/ARD_Admin_Guide_v3.3.pdf)
- [Remote Management MDM macOS](https://support.apple.com/en-us/HT209161)
- [Kickstart Apple Remote Desktop commands](https://support.apple.com/en-us/HT201710)
- [Lockboxx ARD 2019](http://lockboxx.blogspot.com/2019/07/macos-red-teaming-206-ard-apple-remote.html)
- [FireEye 2019 Apple Remote Desktop](https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html)
- [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
- [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
- [SSH Secure Shell](https://www.ssh.com/ssh)
