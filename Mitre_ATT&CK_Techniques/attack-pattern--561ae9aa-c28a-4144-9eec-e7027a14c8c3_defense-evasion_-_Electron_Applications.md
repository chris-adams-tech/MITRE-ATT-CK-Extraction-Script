---
contributors:
- Debabrata Sharma
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--561ae9aa-c28a-4144-9eec-e7027a14c8c3
mitre_attack_url: https://attack.mitre.org/techniques/T1218/015
name: Electron Applications
platforms:
- macOS
- Windows
- Linux
tactics:
- defense-evasion
title: defense-evasion - Electron Applications
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/015](https://attack.mitre.org/techniques/T1218/015) |

# Electron Applications (attack-pattern--561ae9aa-c28a-4144-9eec-e7027a14c8c3)

## Description
Adversaries may abuse components of the Electron framework to execute malicious code. The Electron framework hosts many common applications such as Signal, Slack, and Microsoft Teams.(Citation: Electron 2) Originally developed by GitHub, Electron is a cross-platform desktop application development framework that employs web technologies like JavaScript, HTML, and CSS.(Citation: Electron 3) The Chromium engine is used to display web content and Node.js runs the backend code.(Citation: Electron 1)

Due to the functional mechanics of Electron (such as allowing apps to run arbitrary commands), adversaries may also be able to perform malicious functions in the background potentially disguised as legitimate tools within the framework.(Citation: Electron 1) For example, the abuse of `teams.exe` and `chrome.exe` may allow adversaries to execute malicious commands as child processes of the legitimate application (e.g., `chrome.exe --disable-gpu-sandbox --gpu-launcher="C:\Windows\system32\cmd.exe /c calc.exe`).(Citation: Electron 6-8)

Adversaries may also execute malicious content by planting malicious [JavaScript](https://attack.mitre.org/techniques/T1059/007) within Electron applications.(Citation: Electron Security)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/015)
- [Electron 3](https://www.kaspersky.com/blog/electron-framework-security-issues/49035/)
- [Electron Security](https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules)
- [Electron 6-8](https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf)
- [Electron 1](https://www.mend.io/blog/theres-a-new-stealer-variant-in-town-and-its-using-electron-to-stay-fully-undetected/)
- [Electron 2](https://www.first.org/resources/papers/conf2023/FIRSTCON23-TLP-CLEAR-Horejsi-Abusing-Electron-Based-Applications-in-Targeted-Attacks.pdf)
