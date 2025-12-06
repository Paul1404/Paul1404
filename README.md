# Hi, I'm Paul

**2005 • Bavaria, Germany • Always trying to run things enterprise**

## Systems Engineer | Linux & HCI Infrastructure

I'm a Systems Engineer specializing in virtualized infrastructure with a strong focus on enterprise environments. 

I enjoy designing and automating complex systems, and I run a sophisticated homelab that mirrors enterprise-grade infrastructure
a rewarding hands-on playground for learning resilience, troubleshooting, and real-world infrastructure challenges.

![](https://raw.githubusercontent.com/Paul1404/github-stats/master/generated/overview.svg#gh-dark-mode-only)
![](https://raw.githubusercontent.com/Paul1404/github-stats/master/generated/overview.svg#gh-light-mode-only)
![](https://raw.githubusercontent.com/Paul1404/github-stats/master/generated/languages.svg#gh-dark-mode-only)
![](https://raw.githubusercontent.com/Paul1404/github-stats/master/generated/languages.svg#gh-light-mode-only)

---

## Homelab Infrastructure

### Core Hardware
**vSphere Cluster:**
- 4× Dell PowerEdge R340
- 1× Dell PowerEdge R440
- **Compute + Storage:** ~150 GHz Intel Xeon Gold, 700 GB RAM, 6 TB vSAN ESA all-flash storage
- **Standby:** 3× Huawei Fusion Server 1288H
- **Management:** Dell iDRAC9 & OpenManage Enterprise

### Virtualization & OS
- **VMware vSphere** with vSAN ESA (hyper-converged storage)
- **10+ Red Hat Enterprise Linux 9.6/10 VMs**
- **Red Hat Satellite 6** for lifecycle and configuration management
- **Cloud-init with vSphere** for automated, repeatable VM deployments
- **Aria Operations for Logs** for ESXi and vCenter logging
- **Aria Operations** for VM rightsizing and predictive DRS

### Networking & Security
- **PA-820** Next-Gen Firewall with default-deny policy
  - Network segmented into 4 VLANs with inter-zone traffic controlled via Palo Alto App-IDs
- **Arista Fabric:**
  - **DCS-7010T:** 48× 1GbE access (servers, mgmt) + 4× 10G uplinks
  - **DCS-7150S:** 48× 10GbE with 2× 10G LAG per ESXi + 40G breakout to 4× 10G uplinks
- **MikroTik SwOS** (CSS326 & CSS610) managed switches
- **PHPipam** for IP address management

### Containerization & Orchestration
- **50+ containers** across 20 Docker Compose stacks
- **Portainer EE** for container management
- **Traefik** as ingress controller and reverse proxy
- **HashiCorp Vault** for private PKI (all HTTPS traffic signed)

### Monitoring & Observability
- **Checkmk** for infrastructure monitoring
- **Prometheus, Grafana, Jaeger** for metrics, dashboards, and distributed tracing

### Self-Hosted Services
- **Technitium DNS Server** (primary & secondary)
- **Vaultwarden** (self-hosted Bitwarden)
- **GitLab EE** (containerized for code & CI/CD)

---

## Contributions

**Technitium DNS Server** – Improved installation script and ICU package edge-case handling  
[TechnitiumSoftware/DnsServer#1248](https://github.com/TechnitiumSoftware/DnsServer/pull/1248)

---

## Technologies & Tools

<div align="left">
  <a href="https://www.redhat.com/en" target="_blank" rel="noreferrer">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redhat/redhat-original.svg" height="40" alt="redhat logo" />
  </a>
  <img width="12" />
  <a href="https://www.opensuse.org/" target="_blank" rel="noreferrer">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opensuse/opensuse-original.svg" height="40" alt="opensuse logo" />
  </a>
  <img width="12" />
  <a href="https://kubernetes.io/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=kubernetes" height="40" alt="kubernetes logo" />
  </a>
  <img width="12" />
  <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=bash" height="40" alt="bash logo" />
  </a>
  <img width="12" />
  <a href="https://aws.amazon.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=aws" height="40" alt="amazonwebservices logo" />
  </a>
  <img width="12" />
  <a href="https://www.cloudflare.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=cloudflare" height="40" alt="cloudflare logo" />
  </a>
  <img width="12" />
  <a href="https://astro.build/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=astro" height="40" alt="astro logo" />
  </a>
  <img width="12" />
  <a href="https://about.gitlab.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=gitlab" height="40" alt="gitlab logo" />
  </a>
  <img width="12" />
  <a href="https://workers.cloudflare.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=workers" height="40" alt="cloudflare workers logo" />
  </a>
  <img width="12" />
  <a href="https://www.ansible.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=ansible" height="40" alt="ansible logo" />
  </a>
  <img width="12" />
  <a href="https://www.linux.org/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=linux" height="40" alt="linux logo" />
  </a>
  <img width="12" />
  <a href="https://www.docker.com/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=docker" height="40" alt="docker logo" />
  </a>
  <img width="12" />
  <a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo" />
  </a>
</div>

---

## Certifications

[Red Hat Certified System Administrator | EX200](https://www.credly.com/badges/d59d68a6-4688-4178-8d9e-002abb5d39e0)

---

## Get in Touch

Email: [paul.dresch@untereuerheim.com](mailto:paul.dresch@untereuerheim.com)  
Portfolio: [https://pd-portfolio.net](https://pd-portfolio.net)

---

*Thanks for stopping by!*
