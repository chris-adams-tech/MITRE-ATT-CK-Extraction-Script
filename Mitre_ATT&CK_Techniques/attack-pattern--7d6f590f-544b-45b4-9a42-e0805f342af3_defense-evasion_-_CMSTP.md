---
contributors:
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
- Nik Seetharaman, Palantir
id: attack-pattern--7d6f590f-544b-45b4-9a42-e0805f342af3
mitre_attack_url: https://attack.mitre.org/techniques/T1191
name: CMSTP
platforms:
- Windows
tactics:
- defense-evasion
- execution
title: defense-evasion - CMSTP
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Windows |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1191](https://attack.mitre.org/techniques/T1191) |

# CMSTP (attack-pattern--7d6f590f-544b-45b4-9a42-e0805f342af3)

## Description
The Microsoft Connection Manager Profile Installer (CMSTP.exe) is a command-line program used to install Connection Manager service profiles. (Citation: Microsoft Connection Manager Oct 2009) CMSTP.exe accepts an installation information file (INF) as a parameter and installs a service profile leveraged for remote access connections.

Adversaries may supply CMSTP.exe with INF files infected with malicious commands. (Citation: Twitter CMSTP Usage Jan 2018) Similar to [Regsvr32](https://attack.mitre.org/techniques/T1117) / ”Squiblydoo”, CMSTP.exe may be abused to load and execute DLLs (Citation: MSitPros CMSTP Aug 2017)  and/or COM scriptlets (SCT) from remote servers. (Citation: Twitter CMSTP Jan 2018) (Citation: GitHub Ultimate AppLocker Bypass List) (Citation: Endurant CMSTP July 2018) This execution may also bypass AppLocker and other whitelisting defenses since CMSTP.exe is a legitimate, signed Microsoft application.

CMSTP.exe can also be abused to [Bypass User Account Control](https://attack.mitre.org/techniques/T1088) and execute arbitrary commands from a malicious INF through an auto-elevated COM interface. (Citation: MSitPros CMSTP Aug 2017) (Citation: GitHub Ultimate AppLocker Bypass List) (Citation: Endurant CMSTP July 2018)

## Detection
Use process monitoring to detect and analyze the execution and arguments of CMSTP.exe. Compare recent invocations of CMSTP.exe with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity.

Sysmon events can also be used to identify potential abuses of CMSTP.exe. Detection strategy may depend on the specific adversary procedure, but potential rules include: (Citation: Endurant CMSTP July 2018)

* To detect loading and execution of local/remote payloads - Event 1 (Process creation) where ParentImage contains CMSTP.exe and/or Event 3 (Network connection) where Image contains CMSTP.exe and DestinationIP is external.
* To detect [Bypass User Account Control](https://attack.mitre.org/techniques/T1088) via an auto-elevated COM interface - Event 10 (ProcessAccess) where CallTrace contains CMLUA.dll and/or Event 12 or 13 (RegistryEvent) where TargetObject contains CMMGR32.exe. Also monitor for events, such as the creation of processes (Sysmon Event 1), that involve auto-elevated CMSTP COM interfaces such as CMSTPLUA (3E5FC7F9-9A51-4367-9063-A120244FBEC7) and CMLUAUTIL (3E000D72-A845-4CD9-BD83-80C07C3B881F).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1191)
- [Microsoft Connection Manager Oct 2009](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2003/cc786431(v=ws.10))
- [Twitter CMSTP Usage Jan 2018](https://twitter.com/ItsReallyNick/status/958789644165894146)
- [MSitPros CMSTP Aug 2017](https://msitpros.com/?p=3960)
- [Twitter CMSTP Jan 2018](https://twitter.com/NickTyrer/status/958450014111633408)
- [GitHub Ultimate AppLocker Bypass List](https://github.com/api0cradle/UltimateAppLockerByPassList)
- [Endurant CMSTP July 2018](http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/)
