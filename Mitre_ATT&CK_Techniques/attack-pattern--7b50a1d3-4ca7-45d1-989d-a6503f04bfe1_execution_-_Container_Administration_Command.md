---
contributors:
- Alfredo Oliveira, Trend Micro
- David Fiser, @anu4is, Trend Micro
- Brad Geesaman, @bradgeesaman
- Center for Threat-Informed Defense (CTID)
- Magno Logan, @magnologan, Trend Micro
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--7b50a1d3-4ca7-45d1-989d-a6503f04bfe1
mitre_attack_url: https://attack.mitre.org/techniques/T1609
name: Container Administration Command
platforms:
- Containers
tactics:
- execution
title: execution - Container Administration Command
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Containers |
| **Data Sources** | Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1609](https://attack.mitre.org/techniques/T1609) |

# Container Administration Command (attack-pattern--7b50a1d3-4ca7-45d1-989d-a6503f04bfe1)

## Description
Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.(Citation: Docker Daemon CLI)(Citation: Kubernetes API)(Citation: Kubernetes Kubelet)

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as <code>docker exec</code> to execute a command within a running container.(Citation: Docker Entrypoint)(Citation: Docker Exec) In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as <code>kubectl exec</code>.(Citation: Kubectl Exec Get Shell)

## Detection
Container administration service activities and executed commands can be captured through logging of process execution with command-line arguments on the container and the underlying host. In Docker, the daemon log provides insight into events at the daemon and container service level. Kubernetes system component logs may also detect activities running in and out of containers in the cluster. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1609)
- [Docker Exec](https://docs.docker.com/engine/reference/commandline/exec/)
- [Docker Entrypoint](https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime)
- [Docker Daemon CLI](https://docs.docker.com/engine/reference/commandline/dockerd/)
- [Kubectl Exec Get Shell](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/)
- [Kubernetes Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
- [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
