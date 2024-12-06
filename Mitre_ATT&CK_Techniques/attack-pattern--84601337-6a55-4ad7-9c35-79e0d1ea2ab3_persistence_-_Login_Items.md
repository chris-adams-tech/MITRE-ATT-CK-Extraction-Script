---
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
- 'File: File Modification'
id: attack-pattern--84601337-6a55-4ad7-9c35-79e0d1ea2ab3
mitre_attack_url: https://attack.mitre.org/techniques/T1547/015
name: Login Items
platforms:
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Login Items
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Creation, File: File Creation, File: File Modification |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/015](https://attack.mitre.org/techniques/T1547/015) |

# Login Items (attack-pattern--84601337-6a55-4ad7-9c35-79e0d1ea2ab3)

## Description
Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login items are applications, documents, folders, or server connections that are automatically launched when a user logs in.(Citation: Open Login Items Apple) Login items can be added via a shared file list or Service Management Framework.(Citation: Adding Login Items) Shared file list login items can be set using scripting languages such as [AppleScript](https://attack.mitre.org/techniques/T1059/002), whereas the Service Management Framework uses the API call <code>SMLoginItemSetEnabled</code>.

Login items installed using the Service Management Framework leverage <code>launchd</code>, are not visible in the System Preferences, and can only be removed by the application that created them.(Citation: Adding Login Items)(Citation: SMLoginItemSetEnabled Schroeder 2013) Login items created using a shared file list are visible in System Preferences, can hide the application when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without using Finder.(Citation: Launch Services Apple Developer) Users and applications use login items to configure their user environment to launch commonly used services or applications, such as email, chat, and music applications.

Adversaries can utilize [AppleScript](https://attack.mitre.org/techniques/T1059/002) and [Native API](https://attack.mitre.org/techniques/T1106) calls to create a login item to spawn malicious executables.(Citation: ELC Running at startup) Prior to version 10.5 on macOS, adversaries can add login items by using [AppleScript](https://attack.mitre.org/techniques/T1059/002) to send an Apple events to the “System Events” process, which has an AppleScript dictionary for manipulating login items.(Citation: Login Items AE) Adversaries can use a command such as <code>tell application “System Events” to make login item at end with properties /path/to/executable</code>.(Citation: Startup Items Eclectic)(Citation: hexed osx.dok analysis 2019)(Citation: Add List Remove Login Items Apple Script) This command adds the path of the malicious executable to the login item file list located in <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code>.(Citation: Startup Items Eclectic) Adversaries can also use login items to launch executables that can be used to control the victim system remotely or as a means to gain privilege escalation by prompting for user credentials.(Citation: objsee mac malware 2017)(Citation: CheckPoint Dok)(Citation: objsee netwire backdoor 2019)

## Detection
All login items created via shared file lists are viewable by using the System Preferences GUI or in the <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code> file.(Citation: Open Login Items Apple)(Citation: Startup Items Eclectic)(Citation: objsee block blocking login items)(Citation: sentinelone macos persist Jun 2019) These locations should be monitored and audited for known good applications.

Otherwise, login Items are located in <code>Contents/Library/LoginItems</code> within an application bundle, so these paths should be monitored as well.(Citation: Adding Login Items) Monitor applications that leverage login items with either the LSUIElement or LSBackgroundOnly key in the Info.plist file set to true.(Citation: Adding Login Items)(Citation: Launch Service Keys Developer Apple)

Monitor processes that start at login for unusual or unknown applications. Usual applications for login items could include what users add to configure their user environment, such as email, chat, or music applications, or what administrators include for organization settings and protections. Check for running applications from login items that also have abnormal behavior,, such as establishing network connections.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/015)
- [Open Login Items Apple](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac)
- [Adding Login Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLoginItems.html)
- [SMLoginItemSetEnabled Schroeder 2013](https://blog.timschroeder.net/2013/04/21/smloginitemsetenabled-demystified/)
- [Launch Services Apple Developer](https://developer.apple.com/documentation/coreservices/launch_services)
- [ELC Running at startup](https://eclecticlight.co/2018/05/22/running-at-startup-when-to-use-a-login-item-or-a-launchagent-launchdaemon/)
- [Login Items AE](https://developer.apple.com/library/archive/samplecode/LoginItemsAE/Introduction/Intro.html#//apple_ref/doc/uid/DTS10003788)
- [Startup Items Eclectic](https://eclecticlight.co/2021/09/16/how-to-run-an-app-or-tool-at-startup/)
- [hexed osx.dok analysis 2019](http://www.hexed.in/2019/07/osxdok-analysis.html)
- [Add List Remove Login Items Apple Script](https://gist.github.com/kaloprominat/6111584)
- [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
- [CheckPoint Dok](https://blog.checkpoint.com/2017/04/27/osx-malware-catching-wants-read-https-traffic/)
- [objsee netwire backdoor 2019](https://objective-see.com/blog/blog_0x44.html)
- [objsee block blocking login items](https://objective-see.com/blog/blog_0x31.html)
- [sentinelone macos persist Jun 2019](https://www.sentinelone.com/blog/how-malware-persists-on-macos/)
- [Launch Service Keys Developer Apple](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW1)
