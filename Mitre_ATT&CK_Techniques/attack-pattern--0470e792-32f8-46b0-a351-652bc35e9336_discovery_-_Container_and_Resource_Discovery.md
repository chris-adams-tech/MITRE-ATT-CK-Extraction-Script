---
contributors:
- Vishwas Manral, McAfee
- Center for Threat-Informed Defense (CTID)
- Yossi Weizman, Azure Defender Research Team
data_sources:
- 'Pod: Pod Enumeration'
- 'Container: Container Enumeration'
id: attack-pattern--0470e792-32f8-46b0-a351-652bc35e9336
mitre_attack_url: https://attack.mitre.org/techniques/T1613
name: Container and Resource Discovery
platforms:
- Containers
tactics:
- discovery
title: discovery - Container and Resource Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Containers |
| **Data Sources** | Pod: Pod Enumeration, Container: Container Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1613](https://attack.mitre.org/techniques/T1613) |

# Container and Resource Discovery (attack-pattern--0470e792-32f8-46b0-a351-652bc35e9336)

## Description
Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution. 

## Detection
Establish centralized logging for the activity of container and Kubernetes cluster components. This can be done by deploying logging agents on Kubernetes nodes and retrieving logs from sidecar proxies for application pods to detect malicious activity at the cluster level.

Monitor logs for actions that could be taken to gather information about container infrastructure, including the use of discovery API calls by new or unexpected users. Monitor account activity logs to see actions performed and activity associated with the Kubernetes dashboard and other web applications. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1613)
- [Docker API](https://docs.docker.com/engine/api/v1.41/)
- [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
