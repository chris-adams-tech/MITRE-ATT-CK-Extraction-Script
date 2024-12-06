---
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--130d4494-b2d6-4040-bcea-6e59f05222fe
mitre_attack_url: https://attack.mitre.org/techniques/T1496/003
name: SMS Pumping
platforms:
- SaaS
tactics:
- impact
title: impact - SMS Pumping
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | SaaS |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1496/003](https://attack.mitre.org/techniques/T1496/003) |

# SMS Pumping (attack-pattern--130d4494-b2d6-4040-bcea-6e59f05222fe)

## Description
Adversaries may leverage messaging services for SMS pumping, which may impact system and/or hosted service availability.(Citation: Twilio SMS Pumping) SMS pumping is a type of telecommunications fraud whereby a threat actor first obtains a set of phone numbers from a telecommunications provider, then leverages a victim’s messaging infrastructure to send large amounts of SMS messages to numbers in that set. By generating SMS traffic to their phone number set, a threat actor may earn payments from the telecommunications provider.(Citation: Twilio SMS Pumping Fraud)

Threat actors often use publicly available web forms, such as one-time password (OTP) or account verification fields, in order to generate SMS traffic. These fields may leverage services such as Twilio, AWS SNS, and Amazon Cognito in the background.(Citation: Twilio SMS Pumping)(Citation: AWS RE:Inforce Threat Detection 2024) In response to the large quantity of requests, SMS costs may increase and communication channels may become overwhelmed.(Citation: Twilio SMS Pumping)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1496/003)
- [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)
- [Twilio SMS Pumping](https://www.twilio.com/en-us/blog/sms-pumping-fraud-solutions)
- [Twilio SMS Pumping Fraud](https://www.twilio.com/docs/glossary/what-is-sms-pumping-fraud)
