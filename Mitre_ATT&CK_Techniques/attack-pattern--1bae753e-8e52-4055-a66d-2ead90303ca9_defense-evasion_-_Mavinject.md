---
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--1bae753e-8e52-4055-a66d-2ead90303ca9
mitre_attack_url: https://attack.mitre.org/techniques/T1218/013
name: Mavinject
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Mavinject
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/013](https://attack.mitre.org/techniques/T1218/013) |

# Mavinject (attack-pattern--1bae753e-8e52-4055-a66d-2ead90303ca9)

## Description
Adversaries may abuse mavinject.exe to proxy execution of malicious code. Mavinject.exe is the Microsoft Application Virtualization Injector, a Windows utility that can inject code into external processes as part of Microsoft Application Virtualization (App-V).(Citation: LOLBAS Mavinject)

Adversaries may abuse mavinject.exe to inject malicious DLLs into running processes (i.e. [Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001)), allowing for arbitrary code execution (ex. <code>C:\Windows\system32\mavinject.exe PID /INJECTRUNNING PATH_DLL</code>).(Citation: ATT Lazarus TTP Evolution)(Citation: Reaqta Mavinject) Since mavinject.exe may be digitally signed by Microsoft, proxying execution via this method may evade detection by security products because the execution is masked under a legitimate process. 

In addition to [Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001), Mavinject.exe can also be abused to perform import descriptor injection via its  <code>/HMODULE</code> command-line parameter (ex. <code>mavinject.exe PID /HMODULE=BASE_ADDRESS PATH_DLL ORDINAL_NUMBER</code>). This command would inject an import table entry consisting of the specified DLL into the module at the given base address.(Citation: Mavinject Functionality Deconstructed)

## Detection
Monitor the execution and arguments of mavinject.exe. Compare recent invocations of mavinject.exe with prior history of known good arguments and injected DLLs to determine anomalous and potentially adversarial activity.

Adversaries may rename abusable binaries to evade detections, but the argument <code>INJECTRUNNING</code> is required for mavinject.exe to perform [Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001) and may therefore be monitored to alert malicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/013)
- [ATT Lazarus TTP Evolution](https://cybersecurity.att.com/blogs/labs-research/lazarus-campaign-ttps-and-evolution)
- [LOLBAS Mavinject](https://lolbas-project.github.io/lolbas/Binaries/Mavinject/)
- [Mavinject Functionality Deconstructed](https://posts.specterops.io/mavinject-exe-functionality-deconstructed-c29ab2cf5c0e)
- [Reaqta Mavinject](https://reaqta.com/2017/12/mavinject-microsoft-injector/)
