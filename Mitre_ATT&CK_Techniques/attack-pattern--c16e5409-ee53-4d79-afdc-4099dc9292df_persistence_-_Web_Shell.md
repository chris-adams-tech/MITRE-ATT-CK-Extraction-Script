---
id: attack-pattern--c16e5409-ee53-4d79-afdc-4099dc9292df
mitre_attack_url: https://attack.mitre.org/techniques/T1100
name: Web Shell
platforms:
- Linux
- Windows
- macOS
tactics:
- persistence
- privilege-escalation
title: persistence - Web Shell
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux, Windows, macOS |
| **System Requirements** | Adversary access to Web server with vulnerability or account to upload and serve the Web shell file. |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1100](https://attack.mitre.org/techniques/T1100) |

# Web Shell (attack-pattern--c16e5409-ee53-4d79-afdc-4099dc9292df)

## Description
A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to use the Web server as a gateway into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts the Web server. In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server (see, for example, China Chopper Web shell client). (Citation: Lee 2013)

Web shells may serve as [Redundant Access](https://attack.mitre.org/techniques/T1108) or as a persistence mechanism in case an adversary's primary access methods are detected and removed.

## Detection
Web shells can be difficult to detect. Unlike other forms of persistent remote access, they do not initiate connections. The portion of the Web shell that is on the server may be small and innocuous looking. The PHP version of the China Chopper Web shell, for example, is the following short payload: (Citation: Lee 2013)

<code><?php @eval($_POST['password']);></code>

Nevertheless, detection mechanisms exist. Process monitoring may be used to detect Web servers that perform suspicious actions such as running [cmd](https://attack.mitre.org/software/S0106) or accessing files that are not in the Web directory. File monitoring may be used to detect changes to files in the Web directory of a Web server that do not match with updates to the Web server's content and may indicate implantation of a Web shell script. Log authentication attempts to the server and any unusual traffic patterns to or from the server and internal network. (Citation: US-CERT Alert TA15-314A Web Shells)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1100)
- [capec](https://capec.mitre.org/data/definitions/650.html)
- [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
- [US-CERT Alert TA15-314A Web Shells](https://www.us-cert.gov/ncas/alerts/TA15-314A)
