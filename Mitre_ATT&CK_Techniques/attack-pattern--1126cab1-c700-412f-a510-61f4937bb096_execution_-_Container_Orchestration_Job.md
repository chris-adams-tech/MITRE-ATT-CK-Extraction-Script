---
contributors:
- Center for Threat-Informed Defense (CTID)
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
data_sources:
- 'File: File Creation'
- 'Container: Container Creation'
- 'Scheduled Job: Scheduled Job Creation'
id: attack-pattern--1126cab1-c700-412f-a510-61f4937bb096
mitre_attack_url: https://attack.mitre.org/techniques/T1053/007
name: Container Orchestration Job
platforms:
- Containers
tactics:
- execution
- persistence
- privilege-escalation
title: execution - Container Orchestration Job
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, persistence, privilege-escalation |
| **Platforms** | Containers |
| **Data Sources** | File: File Creation, Container: Container Creation, Scheduled Job: Scheduled Job Creation |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1053/007](https://attack.mitre.org/techniques/T1053/007) |

# Container Orchestration Job (attack-pattern--1126cab1-c700-412f-a510-61f4937bb096)

## Description
Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Linux system. Deployments of this type can also be configured to maintain a quantity of containers over time, automating the process of maintaining persistence within a cluster.

In Kubernetes, a CronJob may be used to schedule a Job that runs one or more containers to perform specific tasks.(Citation: Kubernetes Jobs)(Citation: Kubernetes CronJob) An adversary therefore may utilize a CronJob to schedule deployment of a Job that executes malicious code in various nodes within a cluster.(Citation: Threat Matrix for Kubernetes)

## Detection
Monitor for the anomalous creation of scheduled jobs in container orchestration environments. Use logging agents on Kubernetes nodes and retrieve logs from sidecar proxies for application and resource pods to monitor malicious container orchestration job deployments. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1053/007)
- [Kubernetes CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
- [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [Threat Matrix for Kubernetes](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/)
