---
contributors:
- Regina Elwell
- Praetorian
- Isif Ibrahima, Mandiant
data_sources:
- 'Instance: Instance Enumeration'
- 'Cloud Storage: Cloud Storage Enumeration'
- 'Volume: Volume Enumeration'
- 'Snapshot: Snapshot Enumeration'
id: attack-pattern--57a3d31a-d04f-4663-b2da-7df8ec3f8c9d
mitre_attack_url: https://attack.mitre.org/techniques/T1580
name: Cloud Infrastructure Discovery
platforms:
- IaaS
tactics:
- discovery
title: discovery - Cloud Infrastructure Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | IaaS |
| **Data Sources** | Instance: Instance Enumeration, Cloud Storage: Cloud Storage Enumeration, Volume: Volume Enumeration, Snapshot: Snapshot Enumeration |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1580](https://attack.mitre.org/techniques/T1580) |

# Cloud Infrastructure Discovery (attack-pattern--57a3d31a-d04f-4663-b2da-7df8ec3f8c9d)

## Description
An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services.

Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a <code>DescribeInstances</code> API within the Amazon EC2 API that can return information about one or more instances within an account, the <code>ListBuckets</code> API that returns a list of all buckets owned by the authenticated sender of the request, the <code>HeadBucket</code> API to determine a bucket’s existence along with access permissions of the request sender, or the <code>GetPublicAccessBlock</code> API to retrieve access block configuration for a bucket.(Citation: Amazon Describe Instance)(Citation: Amazon Describe Instances API)(Citation: AWS Get Public Access Block)(Citation: AWS Head Bucket) Similarly, GCP's Cloud SDK CLI provides the <code>gcloud compute instances list</code> command to list all Google Compute Engine instances in a project (Citation: Google Compute Instances), and Azure's CLI command <code>az vm list</code> lists details of virtual machines.(Citation: Microsoft AZ CLI) In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through [Wordlist Scanning](https://attack.mitre.org/techniques/T1595/003).(Citation: Malwarebytes OSINT Leaky Buckets - Hioureas)

An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user.(Citation: Expel IO Evil in AWS) The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence.(Citation: Mandiant M-Trends 2020)An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as <code>DescribeDBInstances</code> to determine size, owner, permissions, and network ACLs of database resources. (Citation: AWS Describe DB Instances) Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in [Cloud Service Discovery](https://attack.mitre.org/techniques/T1526), this technique focuses on the discovery of components of the provided services rather than the services themselves.

## Detection
Establish centralized logging for the activity of cloud infrastructure components. Monitor logs for actions that could be taken to gather information about cloud infrastructure, including the use of discovery API calls by new or unexpected users and enumerations from unknown or malicious IP addresses. To reduce false positives, valid change management procedures could introduce a known identifier that is logged with the change (e.g., tag or header) if supported by the cloud provider, to help distinguish valid, expected actions from malicious ones.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1580)
- [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)
- [AWS Head Bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
- [AWS Get Public Access Block](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [AWS Describe DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)
- [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
- [Amazon Describe Instances API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)
- [Google Compute Instances](https://cloud.google.com/sdk/gcloud/reference/compute/instances/list)
- [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [Microsoft AZ CLI](https://docs.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)
- [Malwarebytes OSINT Leaky Buckets - Hioureas](https://blog.malwarebytes.com/researchers-corner/2019/09/hacking-with-aws-incorporating-leaky-buckets-osint-workflow/)
