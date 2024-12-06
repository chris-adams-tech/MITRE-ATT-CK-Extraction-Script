---
contributors:
- Matt Kelly, @breakersall
id: attack-pattern--1ce03c65-5946-4ac9-9d4d-66db87e024bd
mitre_attack_url: https://attack.mitre.org/techniques/T1172
name: Domain Fronting
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Domain Fronting
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1172](https://attack.mitre.org/techniques/T1172) |

# Domain Fronting (attack-pattern--1ce03c65-5946-4ac9-9d4d-66db87e024bd)

## Description
Domain fronting takes advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2015) The technique involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).

For example, if domain-x and domain-y are customers of the same CDN, it is possible to place domain-x in the TLS header and domain-y in the HTTP header. Traffic will appear to be going to domain-x, however the CDN may route it to domain-y.

## Detection
If SSL inspection is in place or the traffic is not encrypted, the Host field of the HTTP header can be checked if it matches the HTTPS SNI or against a blacklist or whitelist of domain names. (Citation: Fifield Blocking Resistent Communication through domain fronting 2015)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1172)
- [Fifield Blocking Resistent Communication through domain fronting 2015](http://www.icir.org/vern/papers/meek-PETS-2015.pdf)
