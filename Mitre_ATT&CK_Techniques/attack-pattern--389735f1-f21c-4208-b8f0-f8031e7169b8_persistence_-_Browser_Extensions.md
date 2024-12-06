---
contributors:
- Chris Ross @xorrior
- Justin Warner, ICEBRG
- Manikantan Srinivasan, NEC Corporation India
data_sources:
- 'Windows Registry: Windows Registry Key Creation'
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Creation'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--389735f1-f21c-4208-b8f0-f8031e7169b8
mitre_attack_url: https://attack.mitre.org/techniques/T1176
name: Browser Extensions
platforms:
- Linux
- macOS
- Windows
tactics:
- persistence
title: persistence - Browser Extensions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Creation, Process: Process Creation, Command: Command Execution, File: File Creation, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1176](https://attack.mitre.org/techniques/T1176) |

# Browser Extensions (attack-pattern--389735f1-f21c-4208-b8f0-f8031e7169b8)

## Description
Adversaries may abuse Internet browser extensions to establish persistent access to victim systems. Browser extensions or plugins are small programs that can add functionality and customize aspects of Internet browsers. They can be installed directly or through a browser's app store and generally have access and permissions to everything that the browser can access.(Citation: Wikipedia Browser Extension)(Citation: Chrome Extensions Definition)

Malicious extensions can be installed into a browser through malicious app store downloads masquerading as legitimate extensions, through social engineering, or by an adversary that has already compromised a system. Security can be limited on browser app stores so it may not be difficult for malicious extensions to defeat automated scanners.(Citation: Malicious Chrome Extension Numbers) Depending on the browser, adversaries may also manipulate an extension's update url to install updates from an adversary controlled server or manipulate the mobile configuration file to silently install additional extensions.

Previous to macOS 11, adversaries could silently install browser extensions via the command line using the <code>profiles</code> tool to install malicious <code>.mobileconfig</code> files. In macOS 11+, the use of the <code>profiles</code> tool can no longer install configuration profiles, however <code>.mobileconfig</code> files can be planted and installed with user interaction.(Citation: xorrior chrome extensions macOS)

Once the extension is installed, it can browse to websites in the background, steal all information that a user enters into a browser (including credentials), and be used as an installer for a RAT for persistence.(Citation: Chrome Extension Crypto Miner)(Citation: ICEBRG Chrome Extensions)(Citation: Banker Google Chrome Extension Steals Creds)(Citation: Catch All Chrome Extension)

There have also been instances of botnets using a persistent backdoor through malicious Chrome extensions for [Command and Control](https://attack.mitre.org/tactics/TA0011).(Citation: Stantinko Botnet)(Citation: Chrome Extension C2 Malware) Adversaries may also use browser extensions to modify browser permissions and components, privacy settings, and other security controls for [Defense Evasion](https://attack.mitre.org/tactics/TA0005).(Citation: Browers FriarFox)(Citation: Browser Adrozek) 

## Detection
Inventory and monitor browser extension installations that deviate from normal, expected, and benign extensions. Process and network monitoring can be used to detect browsers communicating with a C2 server. However, this may prove to be a difficult way of initially detecting a malicious extension depending on the nature and volume of the traffic it generates.

Monitor for any new items written to the Registry or PE files written to disk. That may correlate with browser extension installation.

On macOS, monitor the command line for usage of the profiles tool, such as <code>profiles install -type=configuration</code>. Additionally, all installed extensions maintain a <code>plist</code> file in the <code>/Library/Managed Preferences/username/</code> directory. Ensure all listed files are in alignment with approved extensions.(Citation: xorrior chrome extensions macOS)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1176)
- [Chrome Extension Crypto Miner](https://www.ghacks.net/2017/09/19/first-chrome-extension-with-javascript-crypto-miner-detected/)
- [xorrior chrome extensions macOS](https://www.xorrior.com/No-Place-Like-Chrome/)
- [Chrome Extensions Definition](https://developer.chrome.com/extensions)
- [ICEBRG Chrome Extensions](https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses)
- [Malicious Chrome Extension Numbers](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43824.pdf)
- [Chrome Extension C2 Malware](https://web.archive.org/web/20240608001937/https://kjaer.io/extension-malware/)
- [Catch All Chrome Extension](https://isc.sans.edu/forums/diary/CatchAll+Google+Chrome+Malicious+Extension+Steals+All+Posted+Data/22976/https:/threatpost.com/malicious-chrome-extension-steals-data-posted-to-any-website/128680/))
- [Banker Google Chrome Extension Steals Creds](https://isc.sans.edu/forums/diary/BankerGoogleChromeExtensiontargetingBrazil/22722/)
- [Browser Adrozek](https://www.microsoft.com/en-us/security/blog/2020/12/10/widespread-malware-campaign-seeks-to-silently-inject-ads-into-search-results-affects-multiple-browsers/)
- [Browers FriarFox](https://www.proofpoint.com/us/blog/threat-insight/ta413-leverages-new-friarfox-browser-extension-target-gmail-accounts-global)
- [Stantinko Botnet](https://www.welivesecurity.com/2017/07/20/stantinko-massive-adware-campaign-operating-covertly-since-2012/)
- [Wikipedia Browser Extension](https://en.wikipedia.org/wiki/Browser_extension)
