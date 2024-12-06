---
contributors:
- Yuval Avrahami, Palo Alto Networks
- Daniel Prizmant, Palo Alto Networks
- Alfredo Oliveira, Trend Micro
- David Fiser, @anu4is, Trend Micro
- Idan Frimark, Cisco
- Magno Logan, @magnologan, Trend Micro
- Ariel Shuper, Cisco
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- CrowdStrike
- Eran Ayalon, Cybereason
- Oren Ofer, Cybereason
- Ilan Sokol, Cybereason
- Joas Antonio dos Santos, @C0d3Cr4zy
data_sources:
- 'Process: Process Creation'
- 'Kernel: Kernel Module Load'
- 'Container: Container Creation'
- 'Volume: Volume Modification'
- 'Process: OS API Execution'
id: attack-pattern--4a5b7ade-8bb5-4853-84ed-23f262002665
mitre_attack_url: https://attack.mitre.org/techniques/T1611
name: Escape to Host
platforms:
- Windows
- Linux
- Containers
tactics:
- privilege-escalation
title: privilege-escalation - Escape to Host
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation |
| **Platforms** | Windows, Linux, Containers |
| **Data Sources** | Process: Process Creation, Kernel: Kernel Module Load, Container: Container Creation, Volume: Volume Modification, Process: OS API Execution |
| **Permissions Required** | Administrator, User, root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1611](https://attack.mitre.org/techniques/T1611) |

# Escape to Host (attack-pattern--4a5b7ade-8bb5-4853-84ed-23f262002665)

## Description
Adversaries may break out of a container to gain access to the underlying host. This can allow an adversary access to other containerized resources from the host level or to the host itself. In principle, containerized resources should provide a clear separation of application functionality and be isolated from the host environment.(Citation: Docker Overview)

There are multiple ways an adversary may escape to a host environment. Examples include creating a container configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute control utilities such as cron on the host; utilizing a privileged container to run commands or load a malicious kernel module on the underlying host; or abusing system calls such as `unshare` and `keyctl` to escalate privileges and steal secrets.(Citation: Docker Bind Mounts)(Citation: Trend Micro Privileged Container)(Citation: Intezer Doki July 20)(Citation: Container Escape)(Citation: Crowdstrike Kubernetes Container Escape)(Citation: Keyctl-unmask)

Additionally, an adversary may be able to exploit a compromised container with a mounted container management socket, such as `docker.sock`, to break out of the container via a [Container Administration Command](https://attack.mitre.org/techniques/T1609).(Citation: Container Escape) Adversaries may also escape via [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068), such as exploiting vulnerabilities in global symbolic links in order to access the root directory of a host machine.(Citation: Windows Server Containers Are Open)

Gaining access to the host may provide the adversary with the opportunity to achieve follow-on objectives, such as establishing persistence, moving laterally within the environment, accessing other containers running on the host, or setting up a command and control channel on the host.

## Detection
Monitor for the deployment of suspicious or unknown container images and pods in your environment, particularly containers running as root. Additionally, monitor for unexpected usage of syscalls such as <code>mount</code> (as well as resulting process activity) that may indicate an attempt to escape from a privileged container to host. In Kubernetes, monitor for cluster-level events associated with changing containers' volume configurations.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1611)
- [Container Escape](https://0xn3va.gitbook.io/cheat-sheets/container/escaping)
- [Windows Server Containers Are Open](https://unit42.paloaltonetworks.com/windows-server-containers-vulnerabilities/)
- [Docker Overview](https://docs.docker.com/get-started/overview/)
- [Docker Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
- [Trend Micro Privileged Container](https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html)
- [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [Crowdstrike Kubernetes Container Escape](https://www.crowdstrike.com/blog/cve-2022-0185-kubernetes-container-escape-using-linux-kernel-exploit/)
- [Keyctl-unmask](https://www.antitree.com/2020/07/keyctl-unmask-going-florida-on-the-state-of-containerizing-linux-keyrings/)
