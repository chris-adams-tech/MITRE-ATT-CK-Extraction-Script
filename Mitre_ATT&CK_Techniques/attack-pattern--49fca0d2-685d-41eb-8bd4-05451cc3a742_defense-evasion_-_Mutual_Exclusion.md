---
contributors:
- Manikantan Srinivasan, NEC Corporation India
- Pooja Natarajan, NEC Corporation India
- "Nagahama Hiroki \u2013 NEC Corporation Japan"
data_sources:
- 'Process: OS API Execution'
- 'File: File Creation'
id: attack-pattern--49fca0d2-685d-41eb-8bd4-05451cc3a742
mitre_attack_url: https://attack.mitre.org/techniques/T1480/002
name: Mutual Exclusion
platforms:
- Windows
- Linux
- macOS
tactics:
- defense-evasion
title: defense-evasion - Mutual Exclusion
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows, Linux, macOS |
| **Data Sources** | Process: OS API Execution, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1480/002](https://attack.mitre.org/techniques/T1480/002) |

# Mutual Exclusion (attack-pattern--49fca0d2-685d-41eb-8bd4-05451cc3a742)

## Description
Adversaries may constrain execution or actions based on the presence of a mutex associated with malware. A mutex is a locking mechanism used to synchronize access to a resource. Only one thread or process can acquire a mutex at a given time.(Citation: Microsoft Mutexes)

While local mutexes only exist within a given process, allowing multiple threads to synchronize access to a resource, system mutexes can be used to synchronize the activities of multiple processes.(Citation: Microsoft Mutexes) By creating a unique system mutex associated with a particular malware, adversaries can verify whether or not a system has already been compromised.(Citation: Sans Mutexes 2012)

In Linux environments, malware may instead attempt to acquire a lock on a mutex file. If the malware is able to acquire the lock, it continues to execute; if it fails, it exits to avoid creating a second instance of itself.(Citation: Intezer RedXOR 2021)(Citation: Deep Instinct BPFDoor 2023)

Mutex names may be hard-coded or dynamically generated using a predictable algorithm.(Citation: ICS Mutexes 2015)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1480/002)
- [Intezer RedXOR 2021](https://intezer.com/blog/malware-analysis/new-linux-backdoor-redxor-likely-operated-by-chinese-nation-state-actor/)
- [Sans Mutexes 2012](https://www.sans.org/blog/looking-at-mutex-objects-for-malware-discovery-indicators-of-compromise/)
- [ICS Mutexes 2015](https://isc.sans.edu/diary/How+Malware+Generates+Mutex+Names+to+Evade+Detection/19429/)
- [Microsoft Mutexes](https://learn.microsoft.com/en-us/dotnet/standard/threading/mutexes)
- [Deep Instinct BPFDoor 2023](https://www.deepinstinct.com/blog/bpfdoor-malware-evolves-stealthy-sniffing-backdoor-ups-its-game)
