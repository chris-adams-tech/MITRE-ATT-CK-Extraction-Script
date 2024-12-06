---
contributors:
- ESET
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'Process: OS API Execution'
- 'Windows Registry: Windows Registry Key Access'
id: attack-pattern--215d9700-5881-48b8-8265-6449dbb7195d
mitre_attack_url: https://attack.mitre.org/techniques/T1652
name: Device Driver Discovery
platforms:
- Linux
- macOS
- Windows
tactics:
- discovery
title: discovery - Device Driver Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Command: Command Execution, Process: Process Creation, Process: OS API Execution, Windows Registry: Windows Registry Key Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1652](https://attack.mitre.org/techniques/T1652) |

# Device Driver Discovery (attack-pattern--215d9700-5881-48b8-8265-6449dbb7195d)

## Description
Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001)) or other defenses (e.g., [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497)), as well as potential exploitable vulnerabilities (e.g., [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068)).

Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()` API function on Windows.(Citation: Microsoft Driverquery)(Citation: Microsoft EnumDeviceDrivers) Information about device drivers (as well as associated services, i.e., [System Service Discovery](https://attack.mitre.org/techniques/T1007)) may also be available in the Registry.(Citation: Microsoft Registry Drivers)

On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod` and `modinfo`.(Citation: Linux Kernel Programming)(Citation: lsmod man)(Citation: modinfo man)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1652)
- [lsmod man](https://man7.org/linux/man-pages/man8/lsmod.8.html)
- [Microsoft Registry Drivers](https://learn.microsoft.com/windows-hardware/drivers/install/overview-of-registry-trees-and-keys)
- [Microsoft EnumDeviceDrivers](https://learn.microsoft.com/windows/win32/api/psapi/nf-psapi-enumdevicedrivers)
- [Microsoft Driverquery](https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery)
- [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
- [modinfo man](https://linux.die.net/man/8/modinfo)
