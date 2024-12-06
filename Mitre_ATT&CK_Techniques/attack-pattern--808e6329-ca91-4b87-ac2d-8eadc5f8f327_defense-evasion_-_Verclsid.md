---
contributors:
- Rodrigo Garcia, Red Canary
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--808e6329-ca91-4b87-ac2d-8eadc5f8f327
mitre_attack_url: https://attack.mitre.org/techniques/T1218/012
name: Verclsid
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - Verclsid
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/012](https://attack.mitre.org/techniques/T1218/012) |

# Verclsid (attack-pattern--808e6329-ca91-4b87-ac2d-8eadc5f8f327)

## Description
Adversaries may abuse verclsid.exe to proxy execution of malicious code. Verclsid.exe is known as the Extension CLSID Verification Host and is responsible for verifying each shell extension before they are used by Windows Explorer or the Windows Shell.(Citation: WinOSBite verclsid.exe)

Adversaries may abuse verclsid.exe to execute malicious payloads. This may be achieved by running <code>verclsid.exe /S /C {CLSID}</code>, where the file is referenced by a Class ID (CLSID), a unique identification number used to identify COM objects. COM payloads executed by verclsid.exe may be able to perform various malicious actions, such as loading and executing COM scriptlets (SCT) from remote servers (similar to [Regsvr32](https://attack.mitre.org/techniques/T1218/010)). Since the binary may be signed and/or native on Windows systems, proxying execution via verclsid.exe may bypass application control solutions that do not account for its potential abuse.(Citation: LOLBAS Verclsid)(Citation: Red Canary Verclsid.exe)(Citation: BOHOPS Abusing the COM Registry)(Citation: Nick Tyrer GitHub) 

## Detection
Use process monitoring to monitor the execution and arguments of verclsid.exe. Compare recent invocations of verclsid.exe with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity. Command arguments used before and after the invocation of verclsid.exe may also be useful in determining the origin and purpose of the payload being executed. Depending on the environment, it may be unusual for verclsid.exe to have a parent process of a Microsoft Office product. It may also be unusual for verclsid.exe to have any child processes or to make network connections or file modifications.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/012)
- [BOHOPS Abusing the COM Registry](https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/)
- [Red Canary Verclsid.exe](https://redcanary.com/blog/verclsid-exe-threat-detection/)
- [LOLBAS Verclsid](https://lolbas-project.github.io/lolbas/Binaries/Verclsid/)
- [Nick Tyrer GitHub](https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5)
- [WinOSBite verclsid.exe](https://www.winosbite.com/verclsid-exe/)
