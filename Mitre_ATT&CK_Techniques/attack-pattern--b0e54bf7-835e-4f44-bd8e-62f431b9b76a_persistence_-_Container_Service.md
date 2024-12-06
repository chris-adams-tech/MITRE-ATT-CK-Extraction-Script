---
data_sources:
- 'Command: Command Execution'
- 'Container: Container Creation'
id: attack-pattern--b0e54bf7-835e-4f44-bd8e-62f431b9b76a
mitre_attack_url: https://attack.mitre.org/techniques/T1543/005
name: Container Service
platforms:
- Containers
tactics:
- persistence
- privilege-escalation
title: persistence - Container Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Containers |
| **Data Sources** | Command: Command Execution, Container: Container Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1543/005](https://attack.mitre.org/techniques/T1543/005) |

# Container Service (attack-pattern--b0e54bf7-835e-4f44-bd8e-62f431b9b76a)

## Description
Adversaries may create or modify container or container cluster management tools that run as daemons, agents, or services on individual hosts. These include software for creating and managing individual containers, such as Docker and Podman, as well as container cluster node-level agents such as kubelet. By modifying these services, an adversary may be able to achieve persistence or escalate their privileges on a host.

For example, by using the `docker run` or `podman run` command with the `restart=always` directive, a container can be configured to persistently restart on the host.(Citation: AquaSec TeamTNT 2023) A user with access to the (rootful) docker command may also be able to escalate their privileges on the host.(Citation: GTFOBins Docker)

In Kubernetes environments, DaemonSets allow an adversary to persistently [Deploy Container](https://attack.mitre.org/techniques/T1610)s on all nodes, including ones added later to the cluster.(Citation: Aquasec Kubernetes Attack 2023)(Citation: Kubernetes DaemonSet) Pods can also be deployed to specific nodes using the `nodeSelector` or `nodeName` fields in the pod spec.(Citation: Kubernetes Assigning Pods to Nodes)(Citation: AppSecco Kubernetes Namespace Breakout 2020)

Note that containers can also be configured to run as [Systemd Service](https://attack.mitre.org/techniques/T1543/002)s.(Citation: Podman Systemd)(Citation: Docker Systemd)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1543/005)
- [AppSecco Kubernetes Namespace Breakout 2020](https://blog.appsecco.com/kubernetes-namespace-breakout-using-insecure-host-path-volume-part-1-b382f2a6e216)
- [Docker Systemd](https://docs.docker.com/config/containers/start-containers-automatically/)
- [GTFOBins Docker](https://gtfobins.github.io/gtfobins/docker/)
- [Kubernetes Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Kubernetes DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
- [Aquasec Kubernetes Attack 2023](https://blog.aquasec.com/leveraging-kubernetes-rbac-to-backdoor-clusters)
- [AquaSec TeamTNT 2023](https://blog.aquasec.com/teamtnt-reemerged-with-new-aggressive-cloud-campaign)
- [Podman Systemd](https://www.redhat.com/sysadmin/podman-run-pods-systemd-services)
