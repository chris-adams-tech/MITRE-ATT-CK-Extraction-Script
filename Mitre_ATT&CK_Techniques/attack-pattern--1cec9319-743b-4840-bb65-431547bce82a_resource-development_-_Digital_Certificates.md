---
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--1cec9319-743b-4840-bb65-431547bce82a
mitre_attack_url: https://attack.mitre.org/techniques/T1587/003
name: Digital Certificates
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Digital Certificates
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1587/003](https://attack.mitre.org/techniques/T1587/003) |

# Digital Certificates (attack-pattern--1cec9319-743b-4840-bb65-431547bce82a)

## Description
Adversaries may create self-signed SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner. In the case of self-signing, digital certificates will lack the element of trust associated with the signature of a third-party certificate authority (CA).

Adversaries may create self-signed SSL/TLS certificates that can be used to further their operations, such as encrypting C2 traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)) or even enabling [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) if added to the root of trust (i.e. [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004)).

After creating a digital certificate, an adversary may then install that certificate (see [Install Digital Certificate](https://attack.mitre.org/techniques/T1608/003)) on infrastructure under their control.

## Detection
Consider use of services that may aid in the tracking of certificates in use on sites across the Internet. In some cases it may be possible to pivot on known pieces of certificate information to uncover other adversary infrastructure.(Citation: Splunk Kovar Certificates 2017)

Detection efforts may be focused on related behaviors, such as [Web Protocols](https://attack.mitre.org/techniques/T1071/001), [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002), and/or [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1587/003)
- [Splunk Kovar Certificates 2017](https://www.splunk.com/en_us/blog/security/tall-tales-of-hunting-with-tls-ssl-certificates.html)
