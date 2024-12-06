---
contributors:
- Edward Millington
- Ed Williams, Trustwave, SpiderLabs
- Olaf Hartong, Falcon Force
- Michael Forret, Quorum Cyber
data_sources:
- 'Process: Process Access'
- 'Windows Registry: Windows Registry Key Modification'
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Logon Session: Logon Session Creation'
- 'Command: Command Execution'
- 'File: File Creation'
id: attack-pattern--65f2d882-3f41-4d48-8a06-29af77ec9f90
mitre_attack_url: https://attack.mitre.org/techniques/T1003/001
name: LSASS Memory
platforms:
- Windows
tactics:
- credential-access
title: credential-access - LSASS Memory
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | Process: Process Access, Windows Registry: Windows Registry Key Modification, Process: Process Creation, Process: OS API Execution, Logon Session: Logon Session Creation, Command: Command Execution, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1003/001](https://attack.mitre.org/techniques/T1003/001) |

# LSASS Memory (attack-pattern--65f2d882-3f41-4d48-8a06-29af77ec9f90)

## Description
Adversaries may attempt to access credential material stored in the process memory of the Local Security Authority Subsystem Service (LSASS). After a user logs on, the system generates and stores a variety of credential materials in LSASS process memory. These credential materials can be harvested by an administrative user or SYSTEM and used to conduct [Lateral Movement](https://attack.mitre.org/tactics/TA0008) using [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550).

As well as in-memory techniques, the LSASS process memory can be dumped from the target host and analyzed on a local system.

For example, on the target host use procdump:

* <code>procdump -ma lsass.exe lsass_dump</code>

Locally, mimikatz can be run using:

* <code>sekurlsa::Minidump lsassdump.dmp</code>
* <code>sekurlsa::logonPasswords</code>

Built-in Windows tools such as `comsvcs.dll` can also be used:

* <code>rundll32.exe C:\Windows\System32\comsvcs.dll MiniDump PID  lsass.dmp full</code>(Citation: Volexity Exchange Marauder March 2021)(Citation: Symantec Attacks Against Government Sector)

Similar to [Image File Execution Options Injection](https://attack.mitre.org/techniques/T1546/012), the silent process exit mechanism can be abused to create a memory dump of `lsass.exe` through Windows Error Reporting (`WerFault.exe`).(Citation: Deep Instinct LSASS)

Windows Security Support Provider (SSP) DLLs are loaded into LSASS process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs. The SSP configuration is stored in two Registry keys: <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages</code> and <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages</code>. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called.(Citation: Graeber 2014)

The following SSPs can be used to access credentials:

* Msv: Interactive logons, batch logons, and service logons are done through the MSV authentication package.
* Wdigest: The Digest Authentication protocol is designed for use with Hypertext Transfer Protocol (HTTP) and Simple Authentication Security Layer (SASL) exchanges.(Citation: TechNet Blogs Credential Protection)
* Kerberos: Preferred for mutual client-server domain authentication in Windows 2000 and later.
* CredSSP:  Provides SSO and Network Level Authentication for Remote Desktop Services.(Citation: TechNet Blogs Credential Protection)


## Detection
Monitor for unexpected processes interacting with LSASS.exe.(Citation: Medium Detecting Attempts to Steal Passwords from Memory) Common credential dumpers such as Mimikatz access LSASS.exe by opening the process, locating the LSA secrets key, and decrypting the sections in memory where credential details are stored. Credential dumpers may also use methods for reflective [Process Injection](https://attack.mitre.org/techniques/T1055) to reduce potential indicators of malicious activity.

On Windows 8.1 and Windows Server 2012 R2, monitor Windows Logs for LSASS.exe creation to verify that LSASS started as a protected process.

Monitor processes and command-line arguments for program execution that may be indicative of credential dumping. Remote access tools may contain built-in features or incorporate existing tools like Mimikatz. PowerShell scripts also exist that contain credential dumping functionality, such as PowerSploit's Invoke-Mimikatz module,(Citation: Powersploit) which may require additional logging features to be configured in the operating system to collect necessary information for analysis.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1003/001)
- [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)
- [Deep Instinct LSASS](https://www.deepinstinct.com/blog/lsass-memory-dumps-are-stealthier-than-ever-before-part-2)
- [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)
- [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)
- [Powersploit](https://github.com/mattifestation/PowerSploit)
- [Symantec Attacks Against Government Sector](https://symantec.broadcom.com/hubfs/Attacks-Against-Government-Sector.pdf)
- [TechNet Blogs Credential Protection](https://blogs.technet.microsoft.com/askpfeplat/2016/04/18/the-importance-of-kb2871997-and-kb2928120-for-credential-protection/)
