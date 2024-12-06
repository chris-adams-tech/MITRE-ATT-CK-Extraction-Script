---
contributors:
- Teodor Cimpoesu
- Sudhanshu Chauhan, @Sudhanshu_C
data_sources:
- 'File: File Access'
- 'Network Traffic: Network Traffic Flow'
- 'File: File Modification'
- 'File: File Creation'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--b77cf5f3-6060-475d-bd60-40ccbf28fdc2
mitre_attack_url: https://attack.mitre.org/techniques/T1187
name: Forced Authentication
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Forced Authentication
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | File: File Access, Network Traffic: Network Traffic Flow, File: File Modification, File: File Creation, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1187](https://attack.mitre.org/techniques/T1187) |

# Forced Authentication (attack-pattern--b77cf5f3-6060-475d-bd60-40ccbf28fdc2)

## Description
Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept.

The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system. (Citation: Wikipedia Server Message Block) This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources.

Web Distributed Authoring and Versioning (WebDAV) is also typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443. (Citation: Didier Stevens WebDAV Traffic) (Citation: Microsoft Managing WebDAV Security)

Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB/WebDAV authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary (i.e. [Template Injection](https://attack.mitre.org/techniques/T1221)), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource it will attempt authentication and send information, including the user's hashed credentials, over SMB to the adversary controlled server. (Citation: GitHub Hashjacking) With access to the credential hash, an adversary can perform off-line [Brute Force](https://attack.mitre.org/techniques/T1110) cracking to gain access to plaintext credentials. (Citation: Cylance Redirect to SMB)

There are several different ways this can occur. (Citation: Osanda Stealing NetNTLM Hashes) Some specifics from in-the-wild use include:

* A spearphishing attachment containing a document with a resource that is automatically loaded when the document is opened (i.e. [Template Injection](https://attack.mitre.org/techniques/T1221)). The document can include, for example, a request similar to <code>file[:]//[remote address]/Normal.dotm</code> to trigger the SMB request. (Citation: US-CERT APT Energy Oct 2017)
* A modified .LNK or .SCF file with the icon filename pointing to an external reference such as <code>\\[remote address]\pic.png</code> that will force the system to load the resource when the icon is rendered to repeatedly gather credentials. (Citation: US-CERT APT Energy Oct 2017)

## Detection
Monitor for SMB traffic on TCP ports 139, 445 and UDP port 137 and WebDAV traffic attempting to exit the network to unknown external systems. If attempts are detected, then investigate endpoint data sources to find the root cause. For internal traffic, monitor the workstation-to-workstation unusual (vs. baseline) SMB traffic. For many networks there should not be any, but it depends on how systems on the network are configured and where resources are located.

Monitor creation and modification of .LNK, .SCF, or any other files on systems and within virtual environments that contain resources that point to external network resources as these could be used to gather credentials when the files are rendered. (Citation: US-CERT APT Energy Oct 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1187)
- [Cylance Redirect to SMB](https://www.cylance.com/content/dam/cylance/pdfs/white_papers/RedirectToSMB.pdf)
- [GitHub Hashjacking](https://github.com/hob0/hashjacking)
- [Microsoft Managing WebDAV Security](https://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/4beddb35-0cba-424c-8b9b-a5832ad8e208.mspx)
- [Osanda Stealing NetNTLM Hashes](https://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/)
- [Didier Stevens WebDAV Traffic](https://blog.didierstevens.com/2017/11/13/webdav-traffic-to-malicious-sites/)
- [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)
- [Wikipedia Server Message Block](https://en.wikipedia.org/wiki/Server_Message_Block)
