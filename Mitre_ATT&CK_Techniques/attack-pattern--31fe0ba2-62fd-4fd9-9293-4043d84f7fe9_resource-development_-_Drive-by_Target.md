---
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--31fe0ba2-62fd-4fd9-9293-4043d84f7fe9
mitre_attack_url: https://attack.mitre.org/techniques/T1608/004
name: Drive-by Target
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Drive-by Target
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1608/004](https://attack.mitre.org/techniques/T1608/004) |

# Drive-by Target (attack-pattern--31fe0ba2-62fd-4fd9-9293-4043d84f7fe9)

## Description
Adversaries may prepare an operational environment to infect systems that visit a website over the normal course of browsing. Endpoint systems may be compromised through browsing to adversary controlled sites, as in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189). In such cases, the user's web browser is typically targeted for exploitation (often not requiring any extra user interaction once landing on the site), but adversaries may also set up websites for non-exploitation behavior such as [Application Access Token](https://attack.mitre.org/techniques/T1550/001). Prior to [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), adversaries must stage resources needed to deliver that exploit to users who browse to an adversary controlled site. Drive-by content can be staged on adversary controlled infrastructure that has been acquired ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or previously compromised ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).

Adversaries may upload or inject malicious web content, such as [JavaScript](https://attack.mitre.org/techniques/T1059/007), into websites.(Citation: FireEye CFR Watering Hole 2012)(Citation: Gallagher 2015) This may be done in a number of ways, including:

* Inserting malicious scripts into web pages or other user controllable web content such as forum posts
* Modifying script files served to websites from publicly writeable cloud storage buckets
* Crafting malicious web advertisements and purchasing ad space on a website through legitimate ad providers (i.e., [Malvertising](https://attack.mitre.org/techniques/T1583/008))

In addition to staging content to exploit a user's web browser, adversaries may also stage scripting content to profile the user's browser (as in [Gather Victim Host Information](https://attack.mitre.org/techniques/T1592)) to ensure it is vulnerable prior to attempting exploitation.(Citation: ATT ScanBox)

Websites compromised by an adversary and used to stage a drive-by may be ones visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is referred to a strategic web compromise or watering hole attack.

Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure ([Domains](https://attack.mitre.org/techniques/T1583/001)) to help facilitate [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).

## Detection
If infrastructure or patterns in the malicious web content utilized to deliver a [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) have been previously identified, internet scanning may uncover when an adversary has staged web content for use in a strategic web compromise.

Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on other phases of the adversary lifecycle, such as [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) or [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1608/004)
- [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
- [Gallagher 2015](http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/)
- [FireEye CFR Watering Hole 2012](https://www.fireeye.com/blog/threat-research/2012/12/council-foreign-relations-water-hole-attack-details.html)
