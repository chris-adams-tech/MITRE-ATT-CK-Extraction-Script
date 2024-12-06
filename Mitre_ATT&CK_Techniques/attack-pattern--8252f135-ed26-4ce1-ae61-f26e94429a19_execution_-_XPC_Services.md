---
contributors:
- Csaba Fitzl @theevilbit of Kandji
data_sources:
- 'Process: Process Access'
id: attack-pattern--8252f135-ed26-4ce1-ae61-f26e94429a19
mitre_attack_url: https://attack.mitre.org/techniques/T1559/003
name: XPC Services
platforms:
- macOS
tactics:
- execution
title: execution - XPC Services
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1559/003](https://attack.mitre.org/techniques/T1559/003) |

# XPC Services (attack-pattern--8252f135-ed26-4ce1-ae61-f26e94429a19)

## Description
Adversaries can provide malicious content to an XPC service daemon for local code execution. macOS uses XPC services for basic inter-process communication between various processes, such as between the XPC Service daemon and third-party application privileged helper tools. Applications can send messages to the XPC Service daemon, which runs as root, using the low-level XPC Service <code>C API</code> or the high level <code>NSXPCConnection API</code> in order to handle tasks that require elevated privileges (such as network connections). Applications are responsible for providing the protocol definition which serves as a blueprint of the XPC services. Developers typically use XPC Services to provide applications stability and privilege separation between the application client and the daemon.(Citation: creatingXPCservices)(Citation: Designing Daemons Apple Dev)

Adversaries can abuse XPC services to execute malicious content. Requests for malicious execution can be passed through the application's XPC Services handler.(Citation: CVMServer Vuln)(Citation: Learn XPC Exploitation) This may also include identifying and abusing improper XPC client validation and/or poor sanitization of input parameters to conduct [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1559/003)
- [creatingXPCservices](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6-SW1)
- [Designing Daemons Apple Dev](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/DesigningDaemons.html)
- [CVMServer Vuln](https://www.trendmicro.com/en_us/research/21/f/CVE-2021-30724_CVMServer_Vulnerability_in_macOS_and_iOS.html)
- [Learn XPC Exploitation](https://wojciechregula.blog/post/learn-xpc-exploitation-part-3-code-injections/)
