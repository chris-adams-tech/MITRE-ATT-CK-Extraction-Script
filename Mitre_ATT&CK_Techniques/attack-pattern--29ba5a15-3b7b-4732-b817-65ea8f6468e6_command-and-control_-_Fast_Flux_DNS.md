---
data_sources:
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Connection Creation'
id: attack-pattern--29ba5a15-3b7b-4732-b817-65ea8f6468e6
mitre_attack_url: https://attack.mitre.org/techniques/T1568/001
name: Fast Flux DNS
platforms:
- Linux
- macOS
- Windows
tactics:
- command-and-control
title: command-and-control - Fast Flux DNS
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | command-and-control |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Network Traffic: Network Traffic Flow, Network Traffic: Network Connection Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1568/001](https://attack.mitre.org/techniques/T1568/001) |

# Fast Flux DNS (attack-pattern--29ba5a15-3b7b-4732-b817-65ea8f6468e6)

## Description
Adversaries may use Fast Flux DNS to hide a command and control channel behind an array of rapidly changing IP addresses linked to a single domain resolution. This technique uses a fully qualified domain name, with multiple IP addresses assigned to it which are swapped with high frequency, using a combination of round robin IP addressing and short Time-To-Live (TTL) for a DNS resource record.(Citation: MehtaFastFluxPt1)(Citation: MehtaFastFluxPt2)(Citation: Fast Flux - Welivesecurity)

The simplest, "single-flux" method, involves registering and de-registering an addresses as part of the DNS A (address) record list for a single DNS name. These registrations have a five-minute average lifespan, resulting in a constant shuffle of IP address resolution.(Citation: Fast Flux - Welivesecurity)

In contrast, the "double-flux" method registers and de-registers an address as part of the DNS Name Server record list for the DNS zone, providing additional resilience for the connection. With double-flux additional hosts can act as a proxy to the C2 host, further insulating the true source of the C2 channel.

## Detection
In general, detecting usage of fast flux DNS is difficult due to web traffic load balancing that services client requests quickly. In single flux cases only IP addresses change for static domain names. In double flux cases, nothing is static. Defenders such as domain registrars and service providers are likely in the best position for detection.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1568/001)
- [MehtaFastFluxPt1](https://resources.infosecinstitute.com/fast-flux-networks-working-detection-part-1/#gref)
- [MehtaFastFluxPt2](https://resources.infosecinstitute.com/fast-flux-networks-working-detection-part-2/#gref)
- [Fast Flux - Welivesecurity](https://www.welivesecurity.com/2017/01/12/fast-flux-networks-work/)
