---
contributors:
- Philip Winther
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
- 'File: File Creation'
id: attack-pattern--2e34237d-8574-43f6-aace-ae2915de8597
mitre_attack_url: https://attack.mitre.org/techniques/T1566/001
name: Spearphishing Attachment
platforms:
- macOS
- Windows
- Linux
tactics:
- initial-access
title: initial-access - Spearphishing Attachment
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | macOS, Windows, Linux |
| **Data Sources** | Network Traffic: Network Traffic Content, Network Traffic: Network Traffic Flow, Application Log: Application Log Content, File: File Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1566/001](https://attack.mitre.org/techniques/T1566/001) |

# Spearphishing Attachment (attack-pattern--2e34237d-8574-43f6-aace-ae2915de8597)

## Description
Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T1204) to gain execution.(Citation: Unit 42 DarkHydrus July 2018) Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

There are many options for the attachment such as Microsoft Office documents, executables, PDFs, or archived files. Upon opening the attachment (and potentially clicking past protections), the adversary's payload exploits a vulnerability or directly executes on the user's system. The text of the spearphishing email usually tries to give a plausible reason why the file should be opened, and may explain how to bypass system protections in order to do so. The email may also contain instructions on how to decrypt an attachment, such as a zip file password, in order to evade email boundary defenses. Adversaries frequently manipulate file extensions and icons in order to make attached executables appear to be document files, or files exploiting one application appear to be a file for a different one. 

## Detection
Network intrusion detection systems and email gateways can be used to detect spearphishing with malicious attachments in transit. Detonation chambers may also be used to identify malicious attachments. Solutions can be signature and behavior based, but adversaries may construct attachments in a way to avoid these systems.

Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed.(Citation: Microsoft Anti Spoofing)(Citation: ACSC Email Spoofing)

Anti-virus can potentially detect malicious documents and attachments as they're scanned to be stored on the email server or on the user's computer. Endpoint sensing or network sensing can potentially detect malicious events once the attachment is opened (such as a Microsoft Word document or PDF reaching out to the internet or spawning Powershell.exe) for techniques such as [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203) or usage of malicious scripts.

Monitor for suspicious descendant process spawning from Microsoft Office and other productivity software.(Citation: Elastic - Koadiac Detection with EQL)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1566/001)
- [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)
- [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Elastic - Koadiac Detection with EQL](https://www.elastic.co/blog/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
