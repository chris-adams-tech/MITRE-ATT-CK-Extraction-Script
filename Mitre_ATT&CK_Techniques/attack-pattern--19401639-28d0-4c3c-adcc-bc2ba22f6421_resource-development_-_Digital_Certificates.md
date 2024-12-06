---
data_sources:
- 'Certificate: Certificate Registration'
- 'Internet Scan: Response Content'
id: attack-pattern--19401639-28d0-4c3c-adcc-bc2ba22f6421
mitre_attack_url: https://attack.mitre.org/techniques/T1588/004
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
| **Data Sources** | Certificate: Certificate Registration, Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1588/004](https://attack.mitre.org/techniques/T1588/004) |

# Digital Certificates (attack-pattern--19401639-28d0-4c3c-adcc-bc2ba22f6421)

## Description
Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner.

Adversaries may purchase or steal SSL/TLS certificates to further their operations, such as encrypting C2 traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)) or even enabling [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) if the certificate is trusted or otherwise added to the root of trust (i.e. [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004)). The purchase of digital certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal certificate materials directly from a compromised third-party, including from certificate authorities.(Citation: DiginotarCompromise) Adversaries may register or hijack domains that they will later purchase an SSL/TLS certificate for.

Certificate authorities exist that allow adversaries to acquire SSL/TLS certificates, such as domain validation certificates, for free.(Citation: Let's Encrypt FAQ)

After obtaining a digital certificate, an adversary may then install that certificate (see [Install Digital Certificate](https://attack.mitre.org/techniques/T1608/003)) on infrastructure under their control.

## Detection
Consider use of services that may aid in the tracking of newly issued certificates and/or certificates in use on sites across the Internet. In some cases it may be possible to pivot on known pieces of certificate information to uncover other adversary infrastructure.(Citation: Splunk Kovar Certificates 2017) Some server-side components of adversary tools may have default values set for SSL/TLS certificates.(Citation: Recorded Future Beacon Certificates)

Detection efforts may be focused on related behaviors, such as [Web Protocols](https://attack.mitre.org/techniques/T1071/001), [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002), and/or [Install Root Certificate](https://attack.mitre.org/techniques/T1553/004).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1588/004)
- [DiginotarCompromise](https://threatpost.com/final-report-diginotar-hack-shows-total-compromise-ca-servers-103112/77170/)
- [Recorded Future Beacon Certificates](https://www.recordedfuture.com/research/cobalt-strike-servers)
- [Splunk Kovar Certificates 2017](https://www.splunk.com/en_us/blog/security/tall-tales-of-hunting-with-tls-ssl-certificates.html)
- [Let's Encrypt FAQ](https://letsencrypt.org/docs/faq/)
