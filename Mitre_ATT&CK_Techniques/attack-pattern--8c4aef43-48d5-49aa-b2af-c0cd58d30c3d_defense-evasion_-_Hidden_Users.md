---
contributors:
- Omkar Gudhate
data_sources:
- 'File: File Modification'
- 'User Account: User Account Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'User Account: User Account Metadata'
id: attack-pattern--8c4aef43-48d5-49aa-b2af-c0cd58d30c3d
mitre_attack_url: https://attack.mitre.org/techniques/T1564/002
name: Hidden Users
platforms:
- macOS
- Windows
- Linux
tactics:
- defense-evasion
title: defense-evasion - Hidden Users
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | File: File Modification, User Account: User Account Creation, Windows Registry: Windows Registry Key Modification, Process: Process Creation, Command: Command Execution, User Account: User Account Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1564/002](https://attack.mitre.org/techniques/T1564/002) |

# Hidden Users (attack-pattern--8c4aef43-48d5-49aa-b2af-c0cd58d30c3d)

## Description
Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users. 

In macOS, adversaries can create or modify a user to be hidden through manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen and in System Preferences, adversaries can set the userID to be under 500 and set the key value <code>Hide500Users</code> to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file.(Citation: Cybereason OSX Pirrit) Every user has a userID associated with it. When the <code>Hide500Users</code> key value is set to <code>TRUE</code>, users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries can use the <code>dscl</code> utility to create hidden user accounts by setting the <code>IsHidden</code> attribute to <code>1</code>. Adversaries can also hide a user’s home folder by changing the <code>chflags</code> to hidden.(Citation: Apple Support Hide a User Account) 

Adversaries may similarly hide user accounts in Windows. Adversaries can set the <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList</code> Registry key value to <code>0</code> for a specific user to prevent that user from being listed on the logon screen.(Citation: FireEye SMOKEDHAM June 2021)(Citation: US-CERT TA18-074A)

On Linux systems, adversaries may hide user accounts from the login screen, also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the greeter using the <code>gsettings</code> command (ex: <code>sudo -u gdm gsettings set org.gnome.login-screen disable-user-list true</code>).(Citation: Hide GDM User Accounts) Display Managers are not anchored to specific distributions and may be changed by a user or adversary.

## Detection
Monitor for users that may be hidden from the login screen but still present in additional artifacts of usage such as directories and authentication logs. 

Monitor processes and command-line events for actions that could be taken to add a new user and subsequently hide it from login screens. Monitor Registry events for modifications to the <code>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList</code> key.

In macOS, monitor for commands, processes, and file activity in combination with a user that has a userID under 500.(Citation: Cybereason OSX Pirrit) Monitor for modifications to set the <code>Hide500Users</code> key value to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file. Monitor the command line for usage of the <code>dscl . create</code> command with the <code>IsHidden</code> attribute set to <code>1</code>.(Citation: Apple Support Hide a User Account) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1564/002)
- [Cybereason OSX Pirrit](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)
- [Apple Support Hide a User Account](https://support.apple.com/en-us/HT203998)
- [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Hide GDM User Accounts](https://ubuntuhandbook.org/index.php/2021/06/hide-user-accounts-ubuntu-20-04-login-screen/)
- [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)
