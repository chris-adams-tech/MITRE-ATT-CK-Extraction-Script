---
data_sources:
- 'File: File Access'
id: attack-pattern--394220d9-8efc-4252-9040-664f7b115be6
mitre_attack_url: https://attack.mitre.org/techniques/T1558/005
name: Ccache Files
platforms:
- Linux
- macOS
tactics:
- credential-access
title: credential-access - Ccache Files
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Linux, macOS |
| **Data Sources** | File: File Access |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1558/005](https://attack.mitre.org/techniques/T1558/005) |

# Ccache Files (attack-pattern--394220d9-8efc-4252-9040-664f7b115be6)

## Description

Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. 

The <code>/etc/krb5.conf</code> configuration file and the <code>KRB5CCNAME</code> environment variable are used to set the storage location for ccache entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically, users interact with ticket storage using <code>kinit</code>, which obtains a Ticket-Granting-Ticket (TGT) for the principal; <code>klist</code>, which lists obtained tickets currently held in the credentials cache; and other built-in binaries.(Citation: Kerberos GNU/Linux)(Citation: Binary Defense Kerberos Linux)

Adversaries can collect tickets from ccache files stored on disk and authenticate as the current user without their password to perform [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003) attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform [Privilege Escalation](https://attack.mitre.org/tactics/TA0004). Tools like Kekeo can also be used by adversaries to convert ccache files to Windows format for further [Lateral Movement](https://attack.mitre.org/tactics/TA0008). On macOS, adversaries may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets via lower-level APIs.(Citation: SpectorOps Bifrost Kerberos macOS 2019)(Citation: Linux Kerberos Tickets)(Citation: Brining MimiKatz to Unix)(Citation: Kekeo) 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1558/005)
- [Binary Defense Kerberos Linux](https://www.binarydefense.com/resources/blog/shining-a-light-in-the-dark-how-binary-defense-uncovered-an-apt-lurking-in-shadows-of-it/)
- [Kerberos GNU/Linux](https://adepts.of0x.cc/kerberos-thievery-linux/)
- [Kekeo](https://github.com/gentilkiwi/kekeo)
- [SpectorOps Bifrost Kerberos macOS 2019](https://posts.specterops.io/when-kirbi-walks-the-bifrost-4c727807744f)
- [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
- [Linux Kerberos Tickets](https://www.fireeye.com/blog/threat-research/2020/04/kerberos-tickets-on-linux-red-teams.html)
