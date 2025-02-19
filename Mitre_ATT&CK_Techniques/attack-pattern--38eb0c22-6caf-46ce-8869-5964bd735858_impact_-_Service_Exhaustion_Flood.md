---
data_sources:
- 'Application Log: Application Log Content'
- 'Sensor Health: Host Status'
- 'Network Traffic: Network Traffic Flow'
- 'Network Traffic: Network Traffic Content'
id: attack-pattern--38eb0c22-6caf-46ce-8869-5964bd735858
mitre_attack_url: https://attack.mitre.org/techniques/T1499/002
name: Service Exhaustion Flood
platforms:
- Windows
- IaaS
- Linux
- macOS
tactics:
- impact
title: impact - Service Exhaustion Flood
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | impact |
| **Platforms** | Windows, IaaS, Linux, macOS |
| **Data Sources** | Application Log: Application Log Content, Sensor Health: Host Status, Network Traffic: Network Traffic Flow, Network Traffic: Network Traffic Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1499/002](https://attack.mitre.org/techniques/T1499/002) |

# Service Exhaustion Flood (attack-pattern--38eb0c22-6caf-46ce-8869-5964bd735858)

## Description
Adversaries may target the different network services provided by systems to conduct a denial of service (DoS). Adversaries often target the availability of DNS and web services, however others have been targeted as well.(Citation: Arbor AnnualDoSreport Jan 2018) Web server software can be attacked through a variety of means, some of which apply generally while others are specific to the software being used to provide the service.

One example of this type of attack is known as a simple HTTP flood, where an adversary sends a large number of HTTP requests to a web server to overwhelm it and/or an application that runs on top of it. This flood relies on raw volume to accomplish the objective, exhausting any of the various resources required by the victim software to provide the service.(Citation: Cloudflare HTTPflood)

Another variation, known as a SSL renegotiation attack, takes advantage of a protocol feature in SSL/TLS. The SSL/TLS protocol suite includes mechanisms for the client and server to agree on an encryption algorithm to use for subsequent secure connections. If SSL renegotiation is enabled, a request can be made for renegotiation of the crypto algorithm. In a renegotiation attack, the adversary establishes a SSL/TLS connection and then proceeds to make a series of renegotiation requests. Because the cryptographic renegotiation has a meaningful cost in computation cycles, this can cause an impact to the availability of the service when done in volume.(Citation: Arbor SSLDoS April 2012)

## Detection
Detection of Endpoint DoS can sometimes be achieved before the effect is sufficient to cause significant impact to the availability of the service, but such response time typically requires very aggressive monitoring and responsiveness. Typical network throughput monitoring tools such as netflow, SNMP, and custom scripts can be used to detect sudden increases in circuit utilization.(Citation: Cisco DoSdetectNetflow) Real-time, automated, and qualitative study of the network traffic can identify a sudden surge in one type of protocol can be used to detect an attack as it starts.

In addition to network level detections, endpoint logging and instrumentation can be useful for detection. Attacks targeting web applications may generate logs in the web server, application server, and/or database server that can be used to identify the type of attack, possibly before the impact is felt.

Externally monitor the availability of services that may be targeted by an Endpoint DoS.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1499/002)
- [Arbor SSLDoS April 2012](https://www.netscout.com/blog/asert/ddos-attacks-ssl-something-old-something-new)
- [Cisco DoSdetectNetflow](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/netflow/configuration/15-mt/nf-15-mt-book/nf-detct-analy-thrts.pdf)
- [Cloudflare HTTPflood](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)
- [Arbor AnnualDoSreport Jan 2018](https://pages.arbornetworks.com/rs/082-KNA-087/images/13th_Worldwide_Infrastructure_Security_Report.pdf)
