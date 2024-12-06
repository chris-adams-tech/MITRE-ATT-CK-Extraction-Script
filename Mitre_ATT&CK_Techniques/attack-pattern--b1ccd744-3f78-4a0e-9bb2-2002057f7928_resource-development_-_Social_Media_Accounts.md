---
data_sources:
- 'Network Traffic: Network Traffic Content'
- 'Persona: Social Media'
id: attack-pattern--b1ccd744-3f78-4a0e-9bb2-2002057f7928
mitre_attack_url: https://attack.mitre.org/techniques/T1585/001
name: Social Media Accounts
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Social Media Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Network Traffic: Network Traffic Content, Persona: Social Media |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1585/001](https://attack.mitre.org/techniques/T1585/001) |

# Social Media Accounts (attack-pattern--b1ccd744-3f78-4a0e-9bb2-2002057f7928)

## Description
Adversaries may create and cultivate social media accounts that can be used during targeting. Adversaries can create social media accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage)

For operations incorporating social engineering, the utilization of a persona on social media may be important. These personas may be fictitious or impersonate real people. The persona may exist on a single social media site or across multiple sites (ex: Facebook, LinkedIn, Twitter, etc.). Establishing a persona  on social media may require development of additional documentation to make them seem real. This could include filling out profile information, developing social networks, or incorporating photos. 

Once a persona has been developed an adversary can use it to create connections to targets of interest. These connections may be direct or may include trying to connect through others.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage) These accounts may be leveraged during other phases of the adversary lifecycle, such as during Initial Access (ex: [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003)).

## Detection
Consider monitoring social media activity related to your organization. Suspicious activity may include personas claiming to work for your organization or recently created/modified accounts making numerous connection requests to accounts affiliated with your organization.

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access (ex: [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003)).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1585/001)
- [NEWSCASTER2014](https://www.securityweek.com/iranian-hackers-targeted-us-officials-elaborate-social-media-attack-operation)
- [BlackHatRobinSage](http://media.blackhat.com/bh-us-10/whitepapers/Ryan/BlackHat-USA-2010-Ryan-Getting-In-Bed-With-Robin-Sage-v1.0.pdf)
