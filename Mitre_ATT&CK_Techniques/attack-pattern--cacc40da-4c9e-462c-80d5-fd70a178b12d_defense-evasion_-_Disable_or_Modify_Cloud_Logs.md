---
contributors:
- Syed Ummar Farooqh, McAfee
- Prasad Somasamudram, McAfee
- Sekhar Sarukkai, McAfee
- Ibrahim Ali Khan
- Alex Soler, AttackIQ
- Janantha Marasinghe
- Matt Snyder, VMware
- Joe Gumke, U.S. Bank
- Arun Seelagan, CISA
data_sources:
- 'Cloud Service: Cloud Service Modification'
- 'User Account: User Account Modification'
- 'Cloud Service: Cloud Service Disable'
id: attack-pattern--cacc40da-4c9e-462c-80d5-fd70a178b12d
mitre_attack_url: https://attack.mitre.org/techniques/T1562/008
name: Disable or Modify Cloud Logs
platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
tactics:
- defense-evasion
title: defense-evasion - Disable or Modify Cloud Logs
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | IaaS, SaaS, Office Suite, Identity Provider |
| **Data Sources** | Cloud Service: Cloud Service Modification, User Account: User Account Modification, Cloud Service: Cloud Service Disable |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1562/008](https://attack.mitre.org/techniques/T1562/008) |

# Disable or Modify Cloud Logs (attack-pattern--cacc40da-4c9e-462c-80d5-fd70a178b12d)

## Description
An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the environment. If an adversary has sufficient permissions, they can disable or modify logging to avoid detection of their activities.

For example, in AWS an adversary may disable CloudWatch/CloudTrail integrations prior to conducting further malicious activity.(Citation: Following the CloudTrail: Generating strong AWS security signals with Sumo Logic) They may alternatively tamper with logging functionality – for example, by removing any associated SNS topics, disabling multi-region logging, or disabling settings that validate and/or encrypt log files.(Citation: AWS Update Trail)(Citation: Pacu Detection Disruption Module) In Office 365, an adversary may disable logging on mail collection activities for specific users by using the `Set-MailboxAuditBypassAssociation` cmdlet, by disabling M365 Advanced Auditing for the user, or by downgrading the user’s license from an Enterprise E5 to an Enterprise E3 license.(Citation: Dark Reading Microsoft 365 Attacks 2021)

## Detection
Monitor logs for API calls to disable logging. In AWS, monitor for: <code>StopLogging</code> and <code>DeleteTrail</code>.(Citation: Stopping CloudTrail from Sending Events to CloudWatch Logs) In GCP, monitor for: <code>google.logging.v2.ConfigServiceV2.UpdateSink</code>.(Citation: Configuring Data Access audit logs)  In Azure, monitor for <code>az monitor diagnostic-settings delete</code>.(Citation: az monitor diagnostic-settings) Additionally, a sudden loss of a log source may indicate that it has been disabled. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1562/008)
- [Stopping CloudTrail from Sending Events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/stop-cloudtrail-from-sending-events-to-cloudwatch-logs.html)
- [AWS Update Trail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html)
- [Following the CloudTrail: Generating strong AWS security signals with Sumo Logic](https://expel.io/blog/following-cloudtrail-generating-aws-security-signals-sumo-logic/)
- [Configuring Data Access audit logs](https://cloud.google.com/logging/docs/audit/configure-data-access)
- [Dark Reading Microsoft 365 Attacks 2021](https://www.darkreading.com/threat-intelligence/incident-responders-explore-microsoft-365-attacks-in-the-wild/d/d-id/1341591)
- [az monitor diagnostic-settings](https://docs.microsoft.com/en-us/cli/azure/monitor/diagnostic-settings?view=azure-cli-latest#az_monitor_diagnostic_settings_delete)
- [Pacu Detection Disruption Module](https://github.com/RhinoSecurityLabs/pacu/blob/master/pacu/modules/detection__disruption/main.py)
