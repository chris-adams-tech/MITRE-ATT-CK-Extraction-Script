---
contributors:
- Mathieu Tartare, ESET
- Tahseen Bin Taj
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'File: File Creation'
- 'Driver: Driver Load'
- 'Module: Module Load'
- 'Process: OS API Execution'
id: attack-pattern--2de47683-f398-448f-b947-9abcc3e32fad
mitre_attack_url: https://attack.mitre.org/techniques/T1547/012
name: Print Processors
platforms:
- Windows
tactics:
- persistence
- privilege-escalation
title: persistence - Print Processors
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, File: File Creation, Driver: Driver Load, Module: Module Load, Process: OS API Execution |
| **Permissions Required** | Administrator, SYSTEM |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1547/012](https://attack.mitre.org/techniques/T1547/012) |

# Print Processors (attack-pattern--2de47683-f398-448f-b947-9abcc3e32fad)

## Description
Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, `spoolsv.exe`, during boot.(Citation: Microsoft Intro Print Processors)

Adversaries may abuse the print spooler service by adding print processors that load malicious DLLs at startup. A print processor can be installed through the <code>AddPrintProcessor</code> API call with an account that has <code>SeLoadDriverPrivilege</code> enabled. Alternatively, a print processor can be registered to the print spooler service by adding the <code>HKLM\SYSTEM\\[CurrentControlSet or ControlSet001]\Control\Print\Environments\\[Windows architecture: e.g., Windows x64]\Print Processors\\[user defined]\Driver</code> Registry key that points to the DLL.

For the malicious print processor to be correctly installed, the payload must be located in the dedicated system print-processor directory, that can be found with the <code>GetPrintProcessorDirectory</code> API call, or referenced via a relative path from this directory.(Citation: Microsoft AddPrintProcessor May 2018) After the print processors are installed, the print spooler service, which starts during boot, must be restarted in order for them to run.(Citation: ESET PipeMon May 2020)

The print spooler service runs under SYSTEM level permissions, therefore print processors installed by an adversary may run under elevated privileges.

## Detection
Monitor process API calls to <code>AddPrintProcessor</code> and <code>GetPrintProcessorDirectory</code>. New print processor DLLs are written to the print processor directory. Also monitor Registry writes to <code>HKLM\SYSTEM\ControlSet001\Control\Print\Environments\\[Windows architecture]\Print Processors\\[user defined]\\Driver</code> or <code>HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\\[Windows architecture]\Print Processors\\[user defined]\Driver</code> as they pertain to print processor installations.

Monitor for abnormal DLLs that are loaded by spoolsv.exe. Print processors that do not correlate with known good software or patching may be suspicious.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1547/012)
- [Microsoft AddPrintProcessor May 2018](https://docs.microsoft.com/en-us/windows/win32/printdocs/addprintprocessor)
- [Microsoft Intro Print Processors](https://learn.microsoft.com/windows-hardware/drivers/print/introduction-to-print-processors)
- [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
