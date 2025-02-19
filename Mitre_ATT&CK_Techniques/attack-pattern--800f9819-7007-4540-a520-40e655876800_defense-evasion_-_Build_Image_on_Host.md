---
contributors:
- Assaf Morag, @MoragAssaf, Team Nautilus Aqua Security
- Roi Kol, @roykol1, Team Nautilus Aqua Security
- Michael Katchinskiy, @michael64194968, Team Nautilus Aqua Security
- Vishwas Manral, McAfee
data_sources:
- 'Image: Image Creation'
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Connection Creation'
- 'Network Traffic: Network Traffic Flow'
id: attack-pattern--800f9819-7007-4540-a520-40e655876800
mitre_attack_url: https://attack.mitre.org/techniques/T1612
name: Build Image on Host
platforms:
- Containers
tactics:
- defense-evasion
title: defense-evasion - Build Image on Host
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Containers |
| **Data Sources** | Image: Image Creation, Network Traffic: Network Traffic Content, Network Traffic: Network Connection Creation, Network Traffic: Network Traffic Flow |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1612](https://attack.mitre.org/techniques/T1612) |

# Build Image on Host (attack-pattern--800f9819-7007-4540-a520-40e655876800)

## Description
Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote <code>build</code> request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it.(Citation: Docker Build Image)

An adversary may take advantage of that <code>build</code> API to build a custom image on the host that includes malware downloaded from their C2 server, and then they may utilize [Deploy Container](https://attack.mitre.org/techniques/T1610) using that custom image.(Citation: Aqua Build Images on Hosts)(Citation: Aqua Security Cloud Native Threat Report June 2021) If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment. 

## Detection
Monitor for unexpected Docker image build requests to the Docker daemon on hosts in the environment. Additionally monitor for subsequent network communication with anomalous IPs that have never been seen before in the environment that indicate the download of malicious code.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1612)
- [Aqua Build Images on Hosts](https://blog.aquasec.com/malicious-container-image-docker-container-host)
- [Docker Build Image](https://docs.docker.com/engine/api/v1.41/#operation/ImageBuild)
- [Aqua Security Cloud Native Threat Report June 2021](https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation)
