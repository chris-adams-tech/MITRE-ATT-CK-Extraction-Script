---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--f6ad61ee-65f3-4bd0-a3f5-2f0accb36317
mitre_attack_url: https://attack.mitre.org/techniques/T1566/003
name: Spearphishing via Service
platforms:
- Linux
- macOS
- Windows
tactics:
- initial-access
title: initial-access - Spearphishing via Service
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Application Log: Application Log Content, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1566/003](https://attack.mitre.org/techniques/T1566/003) |

# Spearphishing via Service (attack-pattern--f6ad61ee-65f3-4bd0-a3f5-2f0accb36317)

## Description
Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than directly via enterprise email channels. 

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services.(Citation: Lookout Dark Caracal Jan 2018) These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries will create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and software that's running in an environment. The adversary can then send malicious links or attachments through these services.

A common example is to build rapport with a target via social media, then send content to a personal webmail service that the target uses on their work computer. This allows an adversary to bypass some email restrictions on the work account, and the target is more likely to open the file since it's something they were expecting. If the payload doesn't work as expected, the adversary can continue normal communications and troubleshoot with the target on how to get it working.

## Detection
Because most common third-party services used for spearphishing via service leverage TLS encryption, SSL/TLS inspection is generally required to detect the initial communication/delivery. With SSL/TLS inspection intrusion detection signatures or other security gateway appliances may be able to detect malware. 

Anti-virus can potentially detect malicious documents and files that are downloaded on the user's computer. Endpoint sensing or network sensing can potentially detect malicious events once the file is opened (such as a Microsoft Word document or PDF reaching out to the internet or spawning Powershell.exe) for techniques such as [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203) or usage of malicious scripts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1566/003)
- [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)
