---
contributors:
- Center for Threat-Informed Defense (CTID)
- Jay Chen, Palo Alto Networks
- Yossi Weizman, Azure Defender Research Team
data_sources:
- 'User Account: User Account Authentication'
- 'Command: Command Execution'
id: attack-pattern--f8ef3a62-3f44-40a4-abca-761ab235c436
mitre_attack_url: https://attack.mitre.org/techniques/T1552/007
name: Container API
platforms:
- Containers
tactics:
- credential-access
title: credential-access - Container API
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Containers |
| **Data Sources** | User Account: User Account Authentication, Command: Command Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1552/007](https://attack.mitre.org/techniques/T1552/007) |

# Container API (attack-pattern--f8ef3a62-3f44-40a4-abca-761ab235c436)

## Description
Adversaries may gather credentials via APIs within a containers environment. APIs in these environments, such as the Docker API and Kubernetes APIs, allow a user to remotely manage their container resources and cluster components.(Citation: Docker API)(Citation: Kubernetes API)

An adversary may access the Docker API to collect logs that contain credentials to cloud, container, and various other resources in the environment.(Citation: Unit 42 Unsecured Docker Daemons) An adversary with sufficient permissions, such as via a pod's service account, may also use the Kubernetes API to retrieve credentials from the Kubernetes API server. These credentials may include those needed for Docker API authentication or secrets from Kubernetes cluster components. 

## Detection
Establish centralized logging for the activity of container and Kubernetes cluster components. Monitor logs for actions that could be taken to gather credentials to container and cloud infrastructure, including the use of discovery API calls by new or unexpected users and APIs that access Docker logs.

It may be possible to detect adversary use of credentials they have obtained such as in [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1552/007)
- [Unit 42 Unsecured Docker Daemons](https://unit42.paloaltonetworks.com/attackers-tactics-and-techniques-in-unsecured-docker-daemons-revealed/)
- [Docker API](https://docs.docker.com/engine/api/v1.41/)
- [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
