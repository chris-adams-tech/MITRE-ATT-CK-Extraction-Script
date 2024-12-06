---
id: attack-pattern--36675cd3-fe00-454c-8516-aebecacbe9d9
mitre_attack_url: https://attack.mitre.org/techniques/T1162
name: Login Item
platforms:
- macOS
tactics:
- persistence
title: persistence - Login Item
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | macOS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1162](https://attack.mitre.org/techniques/T1162) |

# Login Item (attack-pattern--36675cd3-fe00-454c-8516-aebecacbe9d9)

## Description
MacOS provides the option to list specific applications to run when a user logs in. These applications run under the logged in user's context, and will be started every time the user logs in. Login items installed using the Service Management Framework are not visible in the System Preferences and can only be removed by the application that created them (Citation: Adding Login Items). Users have direct control over login items installed using a shared file list which are also visible in System Preferences (Citation: Adding Login Items). These login items are stored in the user's <code>~/Library/Preferences/</code> directory in a plist file called <code>com.apple.loginitems.plist</code> (Citation: Methods of Mac Malware Persistence). Some of these applications can open visible dialogs to the user, but they don’t all have to since there is an option to ‘Hide’ the window. If an adversary can register their own login item or modified an existing one, then they can use it to execute their code for a persistence mechanism each time the user logs in (Citation: Malware Persistence on OS X) (Citation: OSX.Dok Malware). The API method <code> SMLoginItemSetEnabled </code> can be used to set Login Items, but scripting languages like [AppleScript](https://attack.mitre.org/techniques/T1155) can do this as well  (Citation: Adding Login Items).

## Detection
All the login items created via shared file lists are viewable by going to the Apple menu -> System Preferences -> Users & Groups -> Login items. This area (and the corresponding file locations) should be monitored and whitelisted for known good applications. Otherwise, Login Items are located in <code> Contents/Library/LoginItems </code> within an application bundle, so these paths should be monitored as well  (Citation: Adding Login Items). Monitor process execution resulting from login actions for unusual or unknown applications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1162)
- [Adding Login Items](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLoginItems.html)
- [Methods of Mac Malware Persistence](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [OSX.Dok Malware](https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/)
- [capec](https://capec.mitre.org/data/definitions/564.html)
