---
contributors:
- Shane Tully, @securitygypsy
- Joe Gumke, U.S. Bank
- Tamir Yehuda
data_sources:
- 'Process: Process Creation'
- 'Application Log: Application Log Content'
id: attack-pattern--92a78814-b191-47ca-909c-1ccfe3777414
mitre_attack_url: https://attack.mitre.org/techniques/T1072
name: Software Deployment Tools
platforms:
- Linux
- macOS
- Windows
- Network
- SaaS
tactics:
- execution
- lateral-movement
title: execution - Software Deployment Tools
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution, lateral-movement |
| **Platforms** | Linux, macOS, Windows, Network, SaaS |
| **Data Sources** | Process: Process Creation, Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1072](https://attack.mitre.org/techniques/T1072) |

# Software Deployment Tools (attack-pattern--92a78814-b191-47ca-909c-1ccfe3777414)

## Description
Adversaries may gain access to and use centralized software suites installed within an enterprise to execute commands and move laterally through the network. Configuration management and software deployment applications may be used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune, Azure Arc, and GCP Deployment Manager.  

Access to network-wide or enterprise-wide endpoint management software may enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

SaaS-based configuration management services may allow for broad [Cloud Administration Command](https://attack.mitre.org/techniques/T1651) on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to Entra ID.(Citation: SpecterOps Lateral Movement from Azure to On-Prem AD 2020) Such services may also utilize [Web Protocols](https://attack.mitre.org/techniques/T1071/001) to communicate back to adversary owned infrastructure.(Citation: Mitiga Security Advisory: SSM Agent as Remote Access Trojan)

Network infrastructure devices may also have configuration management tools that can be similarly abused by adversaries.(Citation: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation)

The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the third-party system, or specific domain credentials may be required. However, the system may require an administrative account to log in or to access specific functionality.

## Detection
Detection methods will vary depending on the type of third-party software or system and how it is typically used. 

The same investigation process can be applied here as with other potentially malicious activities where the distribution vector is initially unknown but the resulting activity follows a discernible pattern. Analyze the process execution trees, historical activities from the third-party application (such as what types of files are usually pushed), and the resulting activities or events from the file/binary/script pushed to systems. 

Often these third-party applications will have logs of their own that can be collected and correlated with other data from the environment. Ensure that third-party application logs are on-boarded to the enterprise logging system and the logs are regularly reviewed. Audit software deployment logs and look for suspicious or unauthorized activity. A system not typically used to push software to clients that suddenly is used for such a task outside of a known admin function may be suspicious. Monitor account login activity on these applications to detect suspicious/abnormal usage.

Perform application deployment at regular times so that irregular deployment activity stands out. Monitor process activity that does not correlate to known good software. Monitor account login activity on the deployment system.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1072)
- [Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [SpecterOps Lateral Movement from Azure to On-Prem AD 2020](https://posts.specterops.io/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d)
- [Mitiga Security Advisory: SSM Agent as Remote Access Trojan](https://www.mitiga.io/blog/mitiga-security-advisory-abusing-the-ssm-agent-as-a-remote-access-trojan)
