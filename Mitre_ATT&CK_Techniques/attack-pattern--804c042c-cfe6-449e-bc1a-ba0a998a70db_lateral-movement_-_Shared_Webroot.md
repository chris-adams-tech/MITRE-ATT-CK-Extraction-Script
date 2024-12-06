---
id: attack-pattern--804c042c-cfe6-449e-bc1a-ba0a998a70db
mitre_attack_url: https://attack.mitre.org/techniques/T1051
name: Shared Webroot
platforms:
- Windows
tactics:
- lateral-movement
title: lateral-movement - Shared Webroot
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | lateral-movement |
| **Platforms** | Windows |
| **System Requirements** | Shared webroot directory on remote system |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1051](https://attack.mitre.org/techniques/T1051) |

# Shared Webroot (attack-pattern--804c042c-cfe6-449e-bc1a-ba0a998a70db)

## Description
**This technique has been deprecated and should no longer be used.**

Adversaries may add malicious content to an internally accessible website through an open network file share that contains the website's webroot or Web content directory (Citation: Microsoft Web Root OCT 2016) (Citation: Apache Server 2018) and then browse to that content with a Web browser to cause the server to execute the malicious content. The malicious content will typically run under the context and permissions of the Web server process, often resulting in local system or administrative privileges, depending on how the Web server is configured.

This mechanism of shared access and remote execution could be used for lateral movement to the system running the Web server. For example, a Web server running PHP with an open network share could allow an adversary to upload a remote access tool and PHP script to execute the RAT on the system running the Web server when a specific page is visited. (Citation: Webroot PHP 2011)

## Detection
Use file and process monitoring to detect when files are written to a Web server by a process that is not the normal Web server process or when files are written outside of normal administrative time periods. Use process monitoring to identify normal processes that run on the Web server and detect processes that are not typically executed.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1051)
- [Apache Server 2018](http://httpd.apache.org/docs/2.4/getting-started.html#content)
- [Webroot PHP 2011](https://www.webroot.com/blog/2011/02/22/malicious-php-scripts-on-the-rise/)
- [capec](https://capec.mitre.org/data/definitions/563.html)
