---
contributors:
- CrowdStrike Falcon OverWatch
- Jai Minton
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: OS API Execution'
- 'File: File Creation'
id: attack-pattern--90c4a591-d02d-490b-92aa-619d9701ac04
mitre_attack_url: https://attack.mitre.org/techniques/T1556/008
name: Network Provider DLL
platforms:
- Windows
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Network Provider DLL
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, Windows Registry: Windows Registry Key Modification, Process: OS API Execution, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/008](https://attack.mitre.org/techniques/T1556/008) |

# Network Provider DLL (attack-pattern--90c4a591-d02d-490b-92aa-619d9701ac04)

## Description
Adversaries may register malicious network provider dynamic link libraries (DLLs) to capture cleartext user credentials during the authentication process. Network provider DLLs allow Windows to interface with specific network protocols and can also support add-on credential management functions.(Citation: Network Provider API) During the logon process, Winlogon (the interactive logon module) sends credentials to the local `mpnotify.exe` process via RPC. The `mpnotify.exe` process then shares the credentials in cleartext with registered credential managers when notifying that a logon event is happening.(Citation: NPPSPY - Huntress)(Citation: NPPSPY Video)(Citation: NPLogonNotify) 

Adversaries can configure a malicious network provider DLL to receive credentials from `mpnotify.exe`.(Citation: NPPSPY) Once installed as a credential manager (via the Registry), a malicious DLL can receive and save credentials each time a user logs onto a Windows workstation or domain via the `NPLogonNotify()` function.(Citation: NPLogonNotify)

Adversaries may target planting malicious network provider DLLs on systems known to have increased logon activity and/or administrator logon activity, such as servers and domain controllers.(Citation: NPPSPY - Huntress)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/008)
- [NPPSPY - Huntress](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [NPPSPY Video](https://www.youtube.com/watch?v=ggY3srD9dYs)
- [NPPSPY](https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy)
- [Network Provider API](https://learn.microsoft.com/en-us/windows/win32/secauthn/network-provider-api)
- [NPLogonNotify](https://learn.microsoft.com/en-us/windows/win32/api/npapi/nf-npapi-nplogonnotify)
