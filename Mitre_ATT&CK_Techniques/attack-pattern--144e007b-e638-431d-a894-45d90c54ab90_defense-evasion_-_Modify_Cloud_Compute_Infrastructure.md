---
data_sources:
- 'Instance: Instance Metadata'
- 'Instance: Instance Stop'
- 'Snapshot: Snapshot Creation'
- 'Volume: Volume Modification'
- 'Instance: Instance Modification'
- 'Instance: Instance Creation'
- 'Volume: Volume Metadata'
- 'Instance: Instance Start'
- 'Cloud Service: Cloud Service Metadata'
- 'Volume: Volume Creation'
- 'Snapshot: Snapshot Modification'
- 'Snapshot: Snapshot Metadata'
- 'Volume: Volume Deletion'
- 'Snapshot: Snapshot Deletion'
- 'Instance: Instance Deletion'
id: attack-pattern--144e007b-e638-431d-a894-45d90c54ab90
mitre_attack_url: https://attack.mitre.org/techniques/T1578
name: Modify Cloud Compute Infrastructure
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Modify Cloud Compute Infrastructure
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Data Sources** | Instance: Instance Metadata, Instance: Instance Stop, Snapshot: Snapshot Creation, Volume: Volume Modification, Instance: Instance Modification, Instance: Instance Creation, Volume: Volume Metadata, Instance: Instance Start, Cloud Service: Cloud Service Metadata, Volume: Volume Creation, Snapshot: Snapshot Modification, Snapshot: Snapshot Metadata, Volume: Volume Deletion, Snapshot: Snapshot Deletion, Instance: Instance Deletion |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1578](https://attack.mitre.org/techniques/T1578) |

# Modify Cloud Compute Infrastructure (attack-pattern--144e007b-e638-431d-a894-45d90c54ab90)

## Description
An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Detection
Establish centralized logging for the activity of cloud compute infrastructure components. Monitor for suspicious sequences of events, such as the creation of multiple snapshots within a short period of time or the mount of a snapshot to a new instance by a new or unexpected user. To reduce false positives, valid change management procedures could introduce a known identifier that is logged with the change (e.g., tag or header) if supported by the cloud provider, to help distinguish valid, expected actions from malicious ones.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1578)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
