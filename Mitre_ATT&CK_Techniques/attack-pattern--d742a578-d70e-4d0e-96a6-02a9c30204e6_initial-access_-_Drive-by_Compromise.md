---
contributors:
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
data_sources:
- 'Application Log: Application Log Content'
- 'Network Traffic: Network Traffic Content'
- 'Process: Process Creation'
- 'File: File Creation'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--d742a578-d70e-4d0e-96a6-02a9c30204e6
mitre_attack_url: https://attack.mitre.org/techniques/T1189
name: Drive-by Compromise
platforms:
- Windows
- Linux
- macOS
- Identity Provider
tactics:
- initial-access
title: initial-access - Drive-by Compromise
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | initial-access |
| **Platforms** | Windows, Linux, macOS, Identity Provider |
| **Data Sources** | Application Log: Application Log Content, Network Traffic: Network Traffic Content, Process: Process Creation, File: File Creation, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1189](https://attack.mitre.org/techniques/T1189) |

# Drive-by Compromise (attack-pattern--d742a578-d70e-4d0e-96a6-02a9c30204e6)

## Description
Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is typically targeted for exploitation, but adversaries may also use compromised websites for non-exploitation behavior such as acquiring [Application Access Token](https://attack.mitre.org/techniques/T1550/001).

Multiple ways of delivering exploit code to a browser exist (i.e., [Drive-by Target](https://attack.mitre.org/techniques/T1608/004)), including:

* A legitimate website is compromised where adversaries have injected some form of malicious code such as JavaScript, iFrames, and cross-site scripting
* Script files served to a legitimate website from a publicly writeable cloud storage bucket are modified by an adversary
* Malicious ads are paid for and served through legitimate ad providers (i.e., [Malvertising](https://attack.mitre.org/techniques/T1583/008))
* Built-in web application interfaces are leveraged for the insertion of any other kind of object that can be used to display web content or contain a script that executes on the visiting client (e.g. forum posts, comments, and other user controllable web content).

Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.(Citation: Shadowserver Strategic Web Compromise)

Typical drive-by compromise process:

1. A user visits a website that is used to host the adversary controlled content.
2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. 
    * The user may be required to assist in this process by enabling scripting or active website components and ignoring warning dialog boxes.
3. Upon finding a vulnerable version, exploit code is delivered to the browser.
4. If exploitation is successful, then it will give the adversary code execution on the user's system unless other protections are in place.
    * In some cases a second visit to the website after the initial scan is required before exploit code is delivered.

Unlike [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190), the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.

Adversaries may also use compromised websites to deliver a user to a malicious application designed to [Steal Application Access Token](https://attack.mitre.org/techniques/T1528)s, like OAuth tokens, to gain access to protected applications and information. These malicious applications have been delivered through popups on legitimate websites.(Citation: Volexity OceanLotus Nov 2017)

## Detection
Firewalls and proxies can inspect URLs for potentially known-bad domains or parameters. They can also do reputation-based analytics on websites and their requested resources such as how old a domain is, who it's registered to, if it's on a known bad list, or how many other users have connected to it before.

Network intrusion detection systems, sometimes with SSL/TLS inspection, can be used to look for known malicious scripts (recon, heap spray, and browser identification scripts have been frequently reused), common script obfuscation, and exploit code.

Detecting compromise based on the drive-by exploit from a legitimate website may be difficult. Also look for behavior on the endpoint system that might indicate successful compromise, such as abnormal behavior of browser processes. This could include suspicious files written to disk, evidence of [Process Injection](https://attack.mitre.org/techniques/T1055) for attempts to hide execution, evidence of Discovery, or other unusual network traffic that may indicate additional tools transferred to the system.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1189)
- [Shadowserver Strategic Web Compromise](http://blog.shadowserver.org/2012/05/15/cyber-espionage-strategic-web-compromises-trusted-websites-serving-dangerous-results/)
- [Volexity OceanLotus Nov 2017](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)
