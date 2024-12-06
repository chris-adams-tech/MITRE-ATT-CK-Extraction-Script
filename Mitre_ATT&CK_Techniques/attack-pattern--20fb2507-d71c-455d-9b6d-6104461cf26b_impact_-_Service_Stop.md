---
data_sources:
- 'Process: Process Creation'
- 'Process: Process Termination'
- 'Windows Registry: Windows Registry Key Modification'
- 'Command: Command Execution'
- 'File: File Modification'
- 'Process: OS API Execution'
- 'Service: Service Metadata'
id: attack-pattern--20fb2507-d71c-455d-9b6d-6104461cf26b
mitre_attack_url: https://attack.mitre.org/techniques/T1489
name: Service Stop
platforms:
- Windows
- Linux
- macOS
tactics:
- impact
title: impact - Service Stop
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: Process Creation, Process: Process Termination, Windows Registry: Windows Registry Key Modification, Command: Command Execution, File: File Modification, Process: OS API Execution, Service: Service Metadata |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1489](https://attack.mitre.org/techniques/T1489) |

# Service Stop (attack-pattern--20fb2507-d71c-455d-9b6d-6104461cf26b)

## Description
Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.(Citation: Talos Olympic Destroyer 2018)(Citation: Novetta Blockbuster) 

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as <code>MSExchangeIS</code>, which will make Exchange content inaccessible.(Citation: Novetta Blockbuster) In some cases, adversaries may stop or disable many or all services to render systems unusable.(Citation: Talos Olympic Destroyer 2018) Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [Data Destruction](https://attack.mitre.org/techniques/T1485) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) on the data stores of services like Exchange and SQL Server.(Citation: SecureWorks WannaCry Analysis)

## Detection
Monitor processes and command-line arguments to see if critical processes are terminated or stop running.

Monitor for edits for modifications to services and startup programs that correspond to services of high importance. Look for changes to services that do not correlate with known software, patch cycles, etc. Windows service information is stored in the Registry at <code>HKLM\SYSTEM\CurrentControlSet\Services</code>. Systemd service unit files are stored within the /etc/systemd/system, /usr/lib/systemd/system/, and /home/.config/systemd/user/ directories, as well as associated symbolic links.

Alterations to the service binary path or the service startup type changed to disabled may be suspicious.

Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. For example, <code>ChangeServiceConfigW</code> may be used by an adversary to prevent services from starting.(Citation: Talos Olympic Destroyer 2018)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1489)
- [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
