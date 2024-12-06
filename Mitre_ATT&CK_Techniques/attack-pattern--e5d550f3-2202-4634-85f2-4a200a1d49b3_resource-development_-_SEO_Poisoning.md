---
contributors:
- Menachem Goldstein
- Vijay Lalwani
- Will Thomas, Equinix Threat Analysis Center (ETAC)
- Will Jolliffe
- Hiroki Nagahama, NEC Corporation
- Manikantan Srinivasan, NEC Corporation India
- Pooja Natarajan, NEC Corporation India
data_sources:
- 'Internet Scan: Response Content'
id: attack-pattern--e5d550f3-2202-4634-85f2-4a200a1d49b3
mitre_attack_url: https://attack.mitre.org/techniques/T1608/006
name: SEO Poisoning
platforms:
- PRE
tactics:
- resource-development
title: resource-development - SEO Poisoning
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | resource-development |
| **Platforms** | PRE |
| **Data Sources** | Internet Scan: Response Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1608/006](https://attack.mitre.org/techniques/T1608/006) |

# SEO Poisoning (attack-pattern--e5d550f3-2202-4634-85f2-4a200a1d49b3)

## Description
Adversaries may poison mechanisms that influence search engine optimization (SEO) to further lure staged capabilities towards potential victims. Search engines typically display results to users based on purchased ads as well as the site’s ranking/score/reputation calculated by their web crawlers and algorithms.(Citation: Atlas SEO)(Citation: MalwareBytes SEO)

To help facilitate [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), adversaries may stage content that explicitly manipulates SEO rankings in order to promote sites hosting their malicious payloads (such as [Drive-by Target](https://attack.mitre.org/techniques/T1608/004)) within search engines. Poisoning SEO rankings may involve various tricks, such as stuffing keywords (including in the form of hidden text) into compromised sites. These keywords could be related to the interests/browsing habits of the intended victim(s) as well as more broad, seasonably popular topics (e.g. elections, trending news).(Citation: ZScaler SEO)(Citation: Atlas SEO)

In addition to internet search engines (such as Google), adversaries may also aim to manipulate specific in-site searches for developer platforms (such as GitHub) to deceive users towards [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) lures. In-site searches will rank search results according to their own algorithms and metrics such as popularity(Citation: Chexmarx-seo) which may be targeted and gamed by malicious actors.(Citation: Checkmarx-oss-seo)

Adversaries may also purchase or plant incoming links to staged capabilities in order to boost the site’s calculated relevance and reputation.(Citation: MalwareBytes SEO)(Citation: DFIR Report Gootloader)

SEO poisoning may also be combined with evasive redirects and other cloaking mechanisms (such as measuring mouse movements or serving content based on browser user agents, user language/localization settings, or HTTP headers) in order to feed SEO inputs while avoiding scrutiny from defenders.(Citation: ZScaler SEO)(Citation: Sophos Gootloader)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1608/006)
- [MalwareBytes SEO](https://www.malwarebytes.com/blog/news/2018/05/seo-poisoning-is-it-worth-it)
- [Atlas SEO](https://atlas-cybersecurity.com/cyber-threats/threat-actors-use-search-engine-optimization-tactics-to-redirect-traffic-and-install-malware/)
- [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
- [DFIR Report Gootloader](https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/)
- [ZScaler SEO](https://www.zscaler.com/blogs/security-research/ubiquitous-seo-poisoning-urls-0)
- [Chexmarx-seo](https://zero.checkmarx.com/the-github-black-market-gaming-the-star-ranking-game-fc42f5913fb7)
- [Checkmarx-oss-seo](https://checkmarx.com/blog/new-technique-to-trick-developers-detected-in-an-open-source-supply-chain-attack/)
