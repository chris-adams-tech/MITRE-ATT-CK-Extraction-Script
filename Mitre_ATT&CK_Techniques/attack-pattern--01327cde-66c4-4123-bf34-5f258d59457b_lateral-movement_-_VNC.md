---
data_sources:
- 'Process: Process Creation'
- 'Logon Session: Logon Session Creation'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--01327cde-66c4-4123-bf34-5f258d59457b
mitre_attack_url: https://attack.mitre.org/techniques/T1021/005
name: VNC
platforms:
- Linux
- macOS
- Windows
tactics:
- lateral-movement
title: lateral-movement - VNC
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Logon Session: Logon Session Creation, Network Traffic: Network Connection Creation |
| **System Requirements** | VNC server installed and listening for connections. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1021/005](https://attack.mitre.org/techniques/T1021/005) |

# VNC (attack-pattern--01327cde-66c4-4123-bf34-5f258d59457b)

## Description
Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely control machines using Virtual Network Computing (VNC).  VNC is a platform-independent desktop sharing system that uses the RFB (“remote framebuffer”) protocol to enable users to remotely control another computer’s display by relaying the screen, mouse, and keyboard inputs over the network.(Citation: The Remote Framebuffer Protocol)

VNC differs from [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) as VNC is screen-sharing software rather than resource-sharing software. By default, VNC uses the system's authentication, but it can be configured to use credentials specific to VNC.(Citation: MacOS VNC software for Remote Desktop)(Citation: VNC Authentication)

Adversaries may abuse VNC to perform malicious actions as the logged-on user such as opening documents, downloading files, and running arbitrary commands. An adversary could use VNC to remotely control and monitor a system to collect data and information to pivot to other systems within the network. Specific VNC libraries/implementations have also been susceptible to brute force attacks and memory usage exploitation.(Citation: Hijacking VNC)(Citation: macOS root VNC login without authentication)(Citation: VNC Vulnerabilities)(Citation: Offensive Security VNC Authentication Check)(Citation: Attacking VNC Servers PentestLab)(Citation: Havana authentication bug)

## Detection
Use of VNC may be legitimate depending on the environment and how it’s used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior using VNC.

On macOS systems <code>log show --predicate 'process = "screensharingd" and eventMessage contains "Authentication:"'</code> can be used to review incoming VNC connection attempts for suspicious activity.(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

Monitor for use of built-in debugging environment variables (such as those containing credentials or other sensitive information) as well as test/default users on VNC servers, as these can leave openings for adversaries to abuse.(Citation: Gnome Remote Desktop grd-settings)(Citation: Gnome Remote Desktop gschema)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1021/005)
- [Attacking VNC Servers PentestLab](https://pentestlab.blog/2012/10/30/attacking-vnc-servers/)
- [MacOS VNC software for Remote Desktop](https://support.apple.com/guide/remote-desktop/set-up-a-computer-running-vnc-software-apdbed09830/mac)
- [Havana authentication bug](https://lists.openstack.org/pipermail/openstack/2013-December/004138.html)
- [macOS root VNC login without authentication](https://www.tenable.com/blog/detecting-macos-high-sierra-root-account-without-authentication)
- [Offensive Security VNC Authentication Check](https://www.offensive-security.com/metasploit-unleashed/vnc-authentication/)
- [Gnome Remote Desktop grd-settings](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/blob/9aa9181e/src/grd-settings.c#L207)
- [Gnome Remote Desktop gschema](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/blob/9aa9181e/src/org.gnome.desktop.remote-desktop.gschema.xml.in)
- [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
- [VNC Vulnerabilities](https://www.bleepingcomputer.com/news/security/dozens-of-vnc-vulnerabilities-found-in-linux-windows-solutions/)
- [The Remote Framebuffer Protocol](https://datatracker.ietf.org/doc/html/rfc6143#section-7.2.2)
- [VNC Authentication](https://help.realvnc.com/hc/en-us/articles/360002250097-Setting-up-System-Authentication)
- [Hijacking VNC](https://int0x33.medium.com/day-70-hijacking-vnc-enum-brute-access-and-crack-d3d18a4601cc)
