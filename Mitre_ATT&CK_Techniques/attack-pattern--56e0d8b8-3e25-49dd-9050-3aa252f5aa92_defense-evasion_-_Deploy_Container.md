---
contributors:
- Pawan Kinger, @kingerpawan, Trend Micro
- Alfredo Oliveira, Trend Micro
- Idan Frimark, Cisco
- Center for Threat-Informed Defense (CTID)
- Magno Logan, @magnologan, Trend Micro
- Ariel Shuper, Cisco
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
- Joas Antonio dos Santos, @C0d3Cr4zy
data_sources:
- 'Container: Container Start'
- 'Application Log: Application Log Content'
- 'Pod: Pod Creation'
- 'Container: Container Creation'
- 'Pod: Pod Modification'
id: attack-pattern--56e0d8b8-3e25-49dd-9050-3aa252f5aa92
mitre_attack_url: https://attack.mitre.org/techniques/T1610
name: Deploy Container
platforms:
- Containers
tactics:
- defense-evasion
- execution
title: defense-evasion - Deploy Container
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, execution |
| **Platforms** | Containers |
| **Data Sources** | Container: Container Start, Application Log: Application Log Content, Pod: Pod Creation, Container: Container Creation, Pod: Pod Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1610](https://attack.mitre.org/techniques/T1610) |

# Deploy Container (attack-pattern--56e0d8b8-3e25-49dd-9050-3aa252f5aa92)

## Description
Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt to deploy a privileged or vulnerable container into a specific node in order to [Escape to Host](https://attack.mitre.org/techniques/T1611) and access other containers running on the node. (Citation: AppSecco Kubernetes Namespace Breakout 2020)

Containers can be deployed by various means, such as via Docker's <code>create</code> and <code>start</code> APIs or via a web application such as the Kubernetes dashboard or Kubeflow. (Citation: Docker Containers API)(Citation: Kubernetes Dashboard)(Citation: Kubeflow Pipelines) In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets, which can allow containers to be deployed across multiple nodes.(Citation: Kubernetes Workload Management) Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.(Citation: Aqua Build Images on Hosts)

## Detection
Monitor for suspicious or unknown container images and pods in your environment. Deploy logging agents on Kubernetes nodes and retrieve logs from sidecar proxies for application pods to detect malicious activity at the cluster level. In Docker, the daemon log provides insight into remote API calls, including those that deploy containers. Logs for management services or applications used to deploy containers other than the native technologies themselves should also be monitored.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1610)
- [AppSecco Kubernetes Namespace Breakout 2020](https://blog.appsecco.com/kubernetes-namespace-breakout-using-insecure-host-path-volume-part-1-b382f2a6e216)
- [Aqua Build Images on Hosts](https://blog.aquasec.com/malicious-container-image-docker-container-host)
- [Docker Containers API](https://docs.docker.com/engine/api/v1.41/#tag/Container)
- [Kubernetes Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/)
- [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/overview/pipelines-overview/)
- [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
