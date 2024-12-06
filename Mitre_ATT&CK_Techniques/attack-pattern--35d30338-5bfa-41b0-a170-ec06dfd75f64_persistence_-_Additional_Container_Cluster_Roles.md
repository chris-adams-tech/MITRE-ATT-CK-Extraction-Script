---
data_sources:
- 'User Account: User Account Modification'
id: attack-pattern--35d30338-5bfa-41b0-a170-ec06dfd75f64
mitre_attack_url: https://attack.mitre.org/techniques/T1098/006
name: Additional Container Cluster Roles
platforms:
- Containers
tactics:
- persistence
- privilege-escalation
title: persistence - Additional Container Cluster Roles
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Containers |
| **Data Sources** | User Account: User Account Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/006](https://attack.mitre.org/techniques/T1098/006) |

# Additional Container Cluster Roles (attack-pattern--35d30338-5bfa-41b0-a170-ec06dfd75f64)

## Description
An adversary may add additional roles or permissions to an adversary-controlled user or service account to maintain persistent access to a container orchestration system. For example, an adversary with sufficient permissions may create a RoleBinding or a ClusterRoleBinding to bind a Role or ClusterRole to a Kubernetes account.(Citation: Kubernetes RBAC)(Citation: Aquasec Kubernetes Attack 2023) Where attribute-based access control (ABAC) is in use, an adversary with sufficient permissions may modify a Kubernetes ABAC policy to give the target account additional permissions.(Citation: Kuberentes ABAC)
 
This account modification may immediately follow [Create Account](https://attack.mitre.org/techniques/T1136) or other malicious account activity. Adversaries may also modify existing [Valid Accounts](https://attack.mitre.org/techniques/T1078) that they have compromised.  

Note that where container orchestration systems are deployed in cloud environments, as with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Azure Kubernetes Service, cloud-based  role-based access control (RBAC) assignments or ABAC policies can often be used in place of or in addition to local permission assignments.(Citation: Google Cloud Kubernetes IAM)(Citation: AWS EKS IAM Roles for Service Accounts)(Citation: Microsoft Azure Kubernetes Service Service Accounts) In these cases, this technique may be used in conjunction with [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003).

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/006)
- [AWS EKS IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)
- [Google Cloud Kubernetes IAM](https://cloud.google.com/kubernetes-engine/docs/how-to/iam)
- [Kuberentes ABAC](https://kubernetes.io/docs/reference/access-authn-authz/abac/)
- [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
- [Aquasec Kubernetes Attack 2023](https://blog.aquasec.com/leveraging-kubernetes-rbac-to-backdoor-clusters)
- [Microsoft Azure Kubernetes Service Service Accounts](https://learn.microsoft.com/en-us/azure/aks/concepts-identity)
