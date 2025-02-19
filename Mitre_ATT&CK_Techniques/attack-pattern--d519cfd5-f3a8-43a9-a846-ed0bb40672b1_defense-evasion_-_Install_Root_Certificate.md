---
contributors:
- Itzik Kotler, SafeBreach
- Travis Smith, Tripwire
- Red Canary
- Matt Graeber, @mattifestation, SpecterOps
id: attack-pattern--d519cfd5-f3a8-43a9-a846-ed0bb40672b1
mitre_attack_url: https://attack.mitre.org/techniques/T1130
name: Install Root Certificate
platforms:
- Linux
- Windows
- macOS
tactics:
- defense-evasion
title: defense-evasion - Install Root Certificate
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Linux, Windows, macOS |
| **Permissions Required** | Administrator, User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1130](https://attack.mitre.org/techniques/T1130) |

# Install Root Certificate (attack-pattern--d519cfd5-f3a8-43a9-a846-ed0bb40672b1)

## Description
Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or application will trust certificates in the root's chain of trust that have been signed by the root certificate. (Citation: Wikipedia Root Certificate) Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website.

Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that system. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials. (Citation: Operation Emmental)

Atypical root certificates have also been pre-installed on systems by the manufacturer or in the software supply chain and were used in conjunction with malware/adware to provide a man-in-the-middle capability for intercepting information transmitted over secure TLS/SSL communications. (Citation: Kaspersky Superfish)

Root certificates (and their associated chains) can also be cloned and reinstalled. Cloned certificate chains will carry many of the same metadata characteristics of the source and can be used to sign malicious code that may then bypass signature validation tools (ex: Sysinternals, antivirus, etc.) used to block execution and/or uncover artifacts of Persistence. (Citation: SpectorOps Code Signing Dec 2017)

In macOS, the Ay MaMi malware uses <code>/usr/bin/security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /path/to/malicious/cert</code> to install a malicious certificate as a trusted root certificate into the system keychain. (Citation: objective-see ay mami 2018)

## Detection
A system's root certificates are unlikely to change frequently. Monitor new certificates installed on a system that could be due to malicious activity. (Citation: SpectorOps Code Signing Dec 2017) Check pre-installed certificates on new systems to ensure unnecessary or suspicious certificates are not present. Microsoft provides a list of trustworthy root certificates online and through authroot.stl. (Citation: SpectorOps Code Signing Dec 2017) The Sysinternals Sigcheck utility can also be used (<code>sigcheck[64].exe -tuv</code>) to dump the contents of the certificate store and list valid certificates not rooted to the Microsoft Certificate Trust List. (Citation: Microsoft Sigcheck May 2017)

Installed root certificates are located in the Registry under <code>HKLM\SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\</code> and <code>[HKLM or HKCU]\Software[\Policies\]\Microsoft\SystemCertificates\Root\Certificates\</code>. There are a subset of root certificates that are consistent across Windows systems and can be used for comparison: (Citation: Tripwire AppUNBlocker)

* 18F7C1FCC3090203FD5BAA2F861A754976C8DD25
* 245C97DF7514E7CF2DF8BE72AE957B9E04741E85
* 3B1EFD3A66EA28B16697394703A72CA340A05BD5
* 7F88CD7223F3C813818C994614A89C99FA3B5247
* 8F43288AD272F3103B6FB1428485EA3014C0BCFE
* A43489159A520F0D93D032CCAF37E7FE20A8B419
* BE36A4562FB2EE05DBB3D32323ADF445084ED656
* CDD4EEAE6000AC7F40C3802C171E30148030C072

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1130)
- [capec](https://capec.mitre.org/data/definitions/479.html)
- [Wikipedia Root Certificate](https://en.wikipedia.org/wiki/Root_certificate)
- [Operation Emmental](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-finding-holes-operation-emmental.pdf)
- [Kaspersky Superfish](https://www.kaspersky.com/blog/lenovo-pc-with-adware-superfish-preinstalled/7712/)
- [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)
- [objective-see ay mami 2018](https://objective-see.com/blog/blog_0x26.html)
- [Microsoft Sigcheck May 2017](https://docs.microsoft.com/sysinternals/downloads/sigcheck)
- [Tripwire AppUNBlocker](https://www.tripwire.com/state-of-security/off-topic/appunblocker-bypassing-applocker/)
