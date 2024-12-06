---
contributors:
- Wes Hurd
- Vinayak Wadhwa, Lucideus
- Deloitte Threat Library Team
- Oleg Kolesnikov, Securonix
- Menachem Goldstein
- Nikola Kovac
data_sources:
- 'Domain Name: Passive DNS'
- 'Domain Name: Domain Registration'
- 'Domain Name: Active DNS'
id: attack-pattern--40f5caa0-4cb7-4117-89fc-d421bb493df3
mitre_attack_url: https://attack.mitre.org/techniques/T1583/001
name: Domains
platforms:
- PRE
tactics:
- resource-development
title: resource-development - Domains
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Domain Name: Passive DNS, Domain Name: Domain Registration, Domain Name: Active DNS |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1583/001](https://attack.mitre.org/techniques/T1583/001) |

# Domains (attack-pattern--40f5caa0-4cb7-4117-89fc-d421bb493df3)

## Description
Adversaries may acquire domains that can be used during targeting. Domain names are the human readable names used to represent one or more IP addresses. They can be purchased or, in some cases, acquired for free.

Adversaries may use acquired domains for a variety of purposes, including for [Phishing](https://attack.mitre.org/techniques/T1566), [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), and Command and Control.(Citation: CISA MSS Sep 2020) Adversaries may choose domains that are similar to legitimate domains, including through use of homoglyphs or use of a different top-level domain (TLD).(Citation: FireEye APT28)(Citation: PaypalScam) Typosquatting may be used to aid in delivery of payloads via [Drive-by Compromise](https://attack.mitre.org/techniques/T1189). Adversaries may also use internationalized domain names (IDNs) and different character sets (e.g. Cyrillic, Greek, etc.) to execute "IDN homograph attacks," creating visually similar lookalike domains used to deliver malware to victim machines.(Citation: CISA IDN ST05-016)(Citation: tt_httrack_fake_domains)(Citation: tt_obliqueRAT)(Citation: httrack_unhcr)(Citation: lazgroup_idn_phishing)

Different URIs/URLs may also be dynamically generated to uniquely serve malicious content to victims (including one-time, single use domain names).(Citation: iOS URL Scheme)(Citation: URI)(Citation: URI Use)(Citation: URI Unique)

Adversaries may also acquire and repurpose expired domains, which may be potentially already allowlisted/trusted by defenders based on an existing reputation/history.(Citation: Categorisation_not_boundary)(Citation: Domain_Steal_CC)(Citation: Redirectors_Domain_Fronting)(Citation: bypass_webproxy_filtering)

Domain registrars each maintain a publicly viewable database that displays contact information for every registered domain. Private WHOIS services display alternative information, such as their own company data, rather than the owner of the domain. Adversaries may use such private WHOIS services to obscure information about who owns a purchased domain. Adversaries may further interrupt efforts to track their infrastructure by using varied registration information and purchasing domains with different domain registrars.(Citation: Mandiant APT1)

In addition to legitimately purchasing a domain, an adversary may register a new domain in a compromised environment. For example, in AWS environments, adversaries may leverage the Route53 domain service to register a domain and create hosted zones pointing to resources of the threat actor’s choosing.(Citation: Invictus IR DangerDev 2024)

## Detection
Domain registration information is, by design, captured in public registration logs. Consider use of services that may aid in tracking of newly acquired domains, such as WHOIS databases and/or passive DNS. In some cases it may be possible to pivot on known pieces of domain registration information to uncover other infrastructure purchased by the adversary. Consider monitoring for domains created with a similar structure to your own, including under a different TLD. Though various tools and services exist to track, query, and monitor domain name registration information, tracking across multiple DNS infrastructures can require multiple tools/services or more advanced analytics.(Citation: ThreatConnect Infrastructure Dec 2020)

Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access and Command and Control.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1583/001)
- [URI Unique](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)
- [PaypalScam](https://www.zdnet.com/article/paypal-alert-beware-the-paypai-scam-5000109103/)
- [CISA IDN ST05-016](https://us-cert.cisa.gov/ncas/tips/ST05-016)
- [CISA MSS Sep 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-258a)
- [bypass_webproxy_filtering](https://www.blackhillsinfosec.com/bypass-web-proxy-filtering/)
- [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Invictus IR DangerDev 2024](https://www.invictus-ir.com/news/the-curious-case-of-dangerdev-protonmail-me)
- [Domain_Steal_CC](https://krebsonsecurity.com/2018/11/that-domain-you-forgot-to-renew-yeah-its-now-stealing-credit-cards/)
- [tt_obliqueRAT](https://blog.talosintelligence.com/2021/05/transparent-tribe-infra-and-targeting.html)
- [tt_httrack_fake_domains](https://blog.talosintelligence.com/2022/03/transparent-tribe-new-campaign.html)
- [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Categorisation_not_boundary](https://www.mdsec.co.uk/2017/07/categorisation-is-not-a-security-boundary/)
- [URI](https://www.techtarget.com/searchsecurity/tip/Preparing-for-uniform-resource-identifier-URI-exploits)
- [Redirectors_Domain_Fronting](https://www.cobaltstrike.com/blog/high-reputation-redirectors-and-domain-fronting/)
- [URI Use](https://www.blackhat.com/presentations/bh-dc-08/McFeters-Rios-Carter/Presentation/bh-dc-08-mcfeters-rios-carter.pdf)
- [iOS URL Scheme](https://docs.ostorlab.co/kb/IPA_URL_SCHEME_HIJACKING/index.html)
- [lazgroup_idn_phishing](https://web.archive.org/web/20171223000420/https://www.riskiq.com/blog/labs/lazarus-group-cryptocurrency/)
- [httrack_unhcr](https://web.archive.org/web/20220527112908/https://www.riskiq.com/blog/labs/ukraine-malware-infrastructure/)
- [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
