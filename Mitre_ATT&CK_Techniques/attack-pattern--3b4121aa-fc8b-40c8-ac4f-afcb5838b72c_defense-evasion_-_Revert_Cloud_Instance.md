---
contributors:
- Netskope
id: attack-pattern--3b4121aa-fc8b-40c8-ac4f-afcb5838b72c
mitre_attack_url: https://attack.mitre.org/techniques/T1536
name: Revert Cloud Instance
platforms:
- IaaS
tactics:
- defense-evasion
title: defense-evasion - Revert Cloud Instance
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1536](https://attack.mitre.org/techniques/T1536) |

# Revert Cloud Instance (attack-pattern--3b4121aa-fc8b-40c8-ac4f-afcb5838b72c)

## Description
An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)

## Detection
Establish centralized logging of instance activity, which can be used to monitor and review system events even after reverting to a snapshot, rolling back changes, or changing persistence/type of storage. Monitor specifically for events related to snapshots and rollbacks and VM configuration changes, that are occurring outside of normal activity. To reduce false positives, valid change management procedures could introduce a known identifier that is logged with the change (e.g., tag or header) if supported by the cloud provider, to help distinguish valid, expected actions from malicious ones.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1536)
- [Tech Republic - Restore AWS Snapshots](https://www.techrepublic.com/blog/the-enterprise-cloud/backing-up-and-restoring-snapshots-on-amazon-ec2-machines/)
- [Google - Restore Cloud Snapshot](https://cloud.google.com/compute/docs/disks/restore-and-delete-snapshots)
