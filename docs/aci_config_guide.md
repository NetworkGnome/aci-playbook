# Cisco ACI Configuration Guide

**Document Version:** 1.0  
**Last Updated:** October 10, 2025  
**Status:** ✅ Production Ready

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Initial Fabric Setup](#initial-fabric-setup)
- [Tenant Configuration](#tenant-configuration)
- [Network Configuration](#network-configuration)
- [ISE Integration](#ise-integration)
- [Application Deployment](#application-deployment)
- [Verification](#verification)

---

## ✅ Prerequisites

### Hardware Requirements
- [ ] 3x APIC controllers (production) or 1x APIC (lab)
- [ ] 2+ Spine switches
- [ ] 2+ Leaf switches
- [ ] Console access to all devices
- [ ] Management network connectivity

### Software Requirements
- [ ] APIC version 5.2(4e) or later
- [ ] Matching ACI firmware on all switches
- [ ] NTP server accessible
- [ ] DNS server accessible

### Network Requirements
- [ ] Management IP addresses allocated
- [ ] Out-of-band management network
- [ ] TEP (Tunnel Endpoint) IP pool
- [ ] Infrastructure VLAN determined

### Access Requirements
- [ ] Admin credentials prepared
- [ ] SSH keys generated (optional)
- [ ] Certificate for HTTPS (optional)

---

## 🚀 Initial Fabric Setup

### Step 1: APIC Initial Configuration

**Connect via console cable:**

```bash
# APIC boots to setup wizard
Cluster Configuration ............................... [y/n]: y
Enter the fabric name [ACI Fabric1]: PROD-ACI-FABRIC
Enter the fabric ID (1-128) [1]: 1
Enter the number of controllers in the fabric (1-9) [3]: 3
Enter the POD ID (1-9) [1]: 1
Enter the controller ID (1-3) [1]: 1
Enter the controller name [apic1]: APIC1-PROD
Enter the TEP address pool [10.0.0.0/16]: 10.1.0.0/16
Enter address pool for BD multicast addresses [225.0.0.0/15]: 225.0.0.0/15
Enter the VLAN ID for infra network (1-4094): 4093

# Out-of-band Management Configuration
Configure the out-of-band management IP address? [y/n]: y
Enter the out-of-band management IP address [192.168.10.1/24]: 10.10.10.11/24
Enter the out-of-band default gateway [192.168.10.254]: 10.10.10.1
Enter the interface speed/duplex mode [auto]: auto

# Admin Configuration
Enter the admin password: ********
Confirm the admin password: ********

# Cluster Configuration (for multi-APIC)
Enter the management IP address of another controller: 10.10.10.12
```

### Step 2: Access APIC GUI

**Navigate to:** `https://10.10.10.11`

**Login:**
- Username: `admin`
- Password: (password set during setup)

### Step 3: Fabric Discovery

**GUI Path:** `Fabric > Inventory > Fabric Membership`

**Discover Spine Switches:**
1. Wait for spines to appear in "Discovered" state
2. Click each spine node
3. Set Node ID (e.g., 101, 102)
4. Set Node Name (e.g., SPINE-1, SPINE-2)
5. Click "Save"

**Discover Leaf Switches:**
1. Wait for leafs to appear
2. Assign Node ID (e.g., 201, 202, 203)
3. Assign Node Name (e.g., LEAF-1, LEAF-2, LEAF-3)
4. Click "Save"

**Verification:**
```bash
# SSH to APIC
apic1# show controller
ID  Role        Name         IP Address      Status
1   Active      APIC1-PROD   10.10.10.11     Healthy
2   Standby     APIC2-PROD   10.10.10.12     Healthy
3   Standby     APIC3-PROD   10.10.10.13     Healthy

apic1# show switch
Pod ID  Node ID  Node Name     Model          Serial          IP Address      Role    State
1       101      SPINE-1       N9K-C9364C     ABC12345678     10.1.0.101      spine   active
1       102      SPINE-2       N9K-C9364C     ABC12345679     10.1.0.102      spine   active
1       201      LEAF-1        N9K-C93180YC   DEF12345678     10.1.0.201      leaf    active
1       202      LEAF-2        N9K-C93180YC   DEF12345679     10.1.0.202      leaf    active
```

### Step 4: NTP Configuration

**GUI Path:** `Fabric > Fabric Policies > Policies > Pod > Date and Time > default`

**Configure NTP:**
```
Management EPG: out-of-band
NTP Servers:
  - 10.10.1.100 (prefer)
  - 10.10.1.101
  - pool.ntp.org (public fallback)
```

**CLI Verification:**
```bash
apic1# ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*10.10.1.100     .GPS.            1 u   64 1024  377    0.234   -0.052   0.015
+10.10.1.101     .GPS.            1 u  128 1024  377    0.456    0.023   0.021
```

### Step 5: DNS Configuration

**GUI Path:** `Fabric > Fabric Policies > Policies > Global > DNS Profiles`

**Create DNS Profile:**
```
Name: Default-DNS
Management EPG: out-of-band
Providers:
  - 10.10.1.10 (prefer)
  - 10.10.1.11
  - 8.8.8.8 (public fallback)
Domains:
  - company.com
  - company.local
```

---

## 🏢 Tenant Configuration

### Step 1: Create Tenant

**GUI Path:** `Tenants > Add Tenant`

**Configuration:**
```
Name: Production
Description: Production tenant for business applications
```

**CLI Alternative:**
```python
# Using Python ACI SDK
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.model.fv import Tenant

# Login
session = LoginSession('https://10.10.10.11', 'admin', 'password')
moDir = MoDirectory(session)
moDir.login()

# Create tenant
uniMo = moDir.lookupByDn('uni')
tenant = Tenant(uniMo, 'Production')
moDir.commit(tenant)
```

### Step 2: Create VRF

**GUI Path:** `Tenants > Production > Networking > VRFs > Create VRF`

**Configuration:**
```
Name: Production-VRF
Policy Control Enforcement: Enforced
```

**Advanced Settings:**
- IP Data Plane Learning: Enabled
- Preferred Group: Disabled (enable for micro-segmentation)

### Step 3: Create Bridge Domain

**GUI Path:** `Tenants > Production > Networking > Bridge Domains > Create Bridge Domain`

**Configuration:**
```
Name: Web-Tier-BD
VRF: Production-VRF
L2 Unknown Unicast: Hardware Proxy
Unicast Routing: Enabled
ARP Flooding: Disabled
```

**Add Subnet:**
```
Gateway IP: 10.100.10.1/24
Scope: Public (advertised externally)
```

**Repeat for additional tiers:**
- App-Tier-BD: 10.100.20.1/24
- DB-Tier-BD: 10.100.30.1/24

### Step 4: Create Application Profile

**GUI Path:** `Tenants > Production > Application Profiles > Create Application Profile`

**Configuration:**
```
Name: Three-Tier-App
```

### Step 5: Create Endpoint Groups (EPGs)

**Create Web-EPG:**

**GUI Path:** `Tenants > Production > Application Profiles > Three-Tier-App > Application EPGs > Create Application EPG`

**Configuration:**
```
Name: Web-EPG
Bridge Domain: Web-Tier-BD
```

**Associate to Domain:**
```
Domains (VMs and Bare-Metal):
- Physical Domain: PhysDom
- VMM Domain: vCenter-VMM
```

**Repeat for other EPGs:**
- App-EPG → App-Tier-BD
- DB-EPG → DB-Tier-BD

---

## 🔌 Network Configuration

### Step 1: Create Physical Domain

**GUI Path:** `Fabric > Access Policies > Physical and External Domains > Physical Domains > Create Physical Domain`

**Configuration:**
```
Name: PhysDom
VLAN Pool: Production-VLAN-Pool (create if not exists)
```

### Step 2: Create VLAN Pool

**GUI Path:** `Fabric > Access Policies > Pools > VLAN > Create VLAN Pool`

**Configuration:**
```
Name: Production-VLAN-Pool
Allocation Mode: Static Allocation
VLAN Ranges:
  - From: 100, To: 199, Allocation Mode: Static
```

### Step 3: Create Interface Policy Group

**GUI Path:** `Fabric > Access Policies > Interfaces > Leaf Interfaces > Policy Groups > Create Interface Policy Group`

**Configuration:**
```
Name: Server-Access-PolGrp
Link Level Policy: 1G-Auto (or 10G-Auto)
CDP Policy: CDP-Enabled
LLDP Policy: LLDP-Enabled
Attached Entity Profile: Server-AEP
```

### Step 4: Create Attachable Entity Profile (AEP)

**GUI Path:** `Fabric > Access Policies > Policies > Global > Attachable Access Entity Profiles > Create Attachable Access Entity Profile`

**Configuration:**
```
Name: Server-AEP
Domains:
  - PhysDom
```

### Step 5: Create Interface Profile

**GUI Path:** `Fabric > Access Policies > Interfaces > Leaf Interfaces > Profiles > Create Leaf Interface Profile`

**Configuration:**
```
Name: LEAF-201-IntProf
Interface Selectors:
  - Name: Eth1-1-to-48
  - Port Blocks: 1/1-48
  - Policy Group: Server-Access-PolGrp
```

### Step 6: Create Switch Profile

**GUI Path:** `Fabric > Access Policies > Switches > Leaf Switches > Profiles > Create Leaf Switch Profile`

**Configuration:**
```
Name: LEAF-201-SwProf
Leaf Selectors:
  - Name: LEAF-201
  - Blocks: Node 201
Associate Interface Profile: LEAF-201-IntProf
```

### Step 7: Static Path Binding (for physical servers)

**GUI Path:** `Tenants > Production > Application Profiles > Three-Tier-App > Application EPGs > Web-EPG > Static Ports`

**Configuration:**
```
Path Type: Port
Pod: 1
Node: 201 (LEAF-1)
Path: eth1/10
VLAN: 100
Mode: Regular (trunk) or Untagged (access)
```

---

## 🔗 ISE Integration

### Step 1: Enable pxGrid on ISE

**ISE GUI:** `Administration > pxGrid Services`

**Configuration:**
```
✅ Enable pxGrid
Certificate Management: Generate self-signed (or use CA)
```

### Step 2: Configure ISE Domain on APIC

**GUI Path:** `Tenants > common > Security Policies > External Networks > Create L3 External Network`

**Wait, correction - Use ISE integration directly:**

**GUI Path:** `Tenants > Production > Security Policies > ISE Configuration`

**Add ISE Node:**
```
ISE IP Address: 10.10.20.10
Username: pxgrid-admin
Password: ********
Subscriber ID: APIC-Subscriber
```

**Import Certificate:**
1. Download ISE pxGrid certificate
2. Upload to APIC
3. Trust certificate chain

### Step 3: Configure External EPG for ISE

**GUI Path:** `Tenants > Production > Networking > External Routed Networks > Create L3Out`

**Configuration:**
```
Name: ISE-L3Out
VRF: Production-VRF
L3 Domain: External-L3Dom
```

**Add External EPG:**
```
Name: ISE-Ext-EPG
Subnets: 10.10.20.0/24 (ISE subnet)
Contract: Permit ISE traffic
```

### Step 4: Configure Attribute-Based EPG

**GUI Path:** `Tenants > Production > Application Profiles > Three-Tier-App > Application EPGs > Create Application EPG`

**Configuration:**
```
Name: Guest-Dynamic-EPG
Type: Attribute-based EPG
Classification:
  - IP Address Attribute
  - VM Attribute (for VMM integration)
  - ISE Attribute (for pxGrid)
```

**ISE Attribute Mapping:**
```
Attribute: Security Group Tag (SGT)
Value: Guest-SGT (configured in ISE)
Action: Associate to Guest-Dynamic-EPG
```

---

## 📱 Application Deployment

### Example: Three-Tier Web Application

**Architecture:**
```
Internet → Web-EPG (10.100.10.0/24) 
            ↓ (Contract: Web-to-App)
          App-EPG (10.100.20.0/24)
            ↓ (Contract: App-to-DB)
          DB-EPG (10.100.30.0/24)
```

### Step 1: Create Contracts

**Web-to-App Contract:**

**GUI Path:** `Tenants > Production > Security Policies > Contracts > Create Contract`

**Configuration:**
```
Name: Web-to-App
Subjects:
  - Name: HTTP-HTTPS
    Filters:
      - HTTP (tcp/80)
      - HTTPS (tcp/443)
```

**Create Filters:**

**GUI Path:** `Tenants > Production > Security Policies > Filters > Create Filter`

**HTTP Filter:**
```
Name: HTTP
Entries:
  - Name: tcp-80
    Ether Type: IP
    IP Protocol: tcp
    Destination Port: 80
```

**HTTPS Filter:**
```
Name: HTTPS
Entries:
  - Name: tcp-443
    Ether Type: IP
    IP Protocol: tcp
    Destination Port: 443
```

### Step 2: Apply Contracts to EPGs

**Web-EPG (Consumer):**

**GUI Path:** `Tenants > Production > Application Profiles > Three-Tier-App > Web-EPG > Contracts`

```
Consumed Contracts:
  - Web-to-App
```

**App-EPG (Provider & Consumer):**
```
Provided Contracts:
  - Web-to-App
Consumed Contracts:
  - App-to-DB
```

**DB-EPG (Provider):**
```
Provided Contracts:
  - App-to-DB
```

### Step 3: Deploy Application Servers

**Physical Servers:**
1. Connect to leaf switch ports (e.g., LEAF-201, eth1/10-12)
2. Configure static path binding (see Network Configuration)
3. Configure server NIC with VLAN 100 (or untagged)
4. Assign IP from subnet (e.g., 10.100.10.10/24)
5. Default gateway: 10.100.10.1 (BD subnet gateway)

**Virtual Servers (VMware):**
1. Ensure VMM domain integration configured
2. Create port group in vCenter (automatically created by APIC)
3. Assign VMs to port group
4. VMs automatically associated to EPG

---

## ✅ Verification

### Fabric Health

**GUI:** `Operations > Fabric > Inventory > Pod 1`

**Check:**
- [ ] All nodes show "Active" status
- [ ] All interfaces "Up"
- [ ] No critical faults

**CLI:**
```bash
apic1# show switch
apic1# show controller
apic1# acidiag fnvread
```

### Tenant Verification

**GUI:** `Tenants > Production`

**Verify:**
- [ ] VRF created
- [ ] Bridge Domains created with subnets
- [ ] EPGs created and associated to BDs
- [ ] Contracts created and applied

**CLI:**
```bash
# From leaf switch
leaf-201# show vrf Production:Production-VRF
leaf-201# show ip route vrf Production:Production-VRF
leaf-201# show endpoint vrf Production:Production-VRF
```

### Endpoint Learning

**GUI:** `Tenants > Production > Application Profiles > Three-Tier-App > Application EPGs > Web-EPG > Operational > Client End-Points`

**Check:**
- [ ] Endpoints learned with correct IP/MAC
- [ ] Encapsulation (VLAN) correct
- [ ] Leaf and interface shown

**CLI:**
```bash
leaf-201# show endpoint
```

### Contract Verification

**GUI:** `Tenants > Production > Security Policies > Contracts > Web-to-App > Operational > Contract Usage`

**Verify:**
- [ ] Provider EPG: App-EPG
- [ ] Consumer EPG: Web-EPG
- [ ] Filter rules applied

**CLI:**
```bash
leaf-201# show zoning-rule
```

### Traffic Flow Test

**From Web Server:**
```bash
# Test connectivity to App tier
ping 10.100.20.10
curl http://10.100.20.10:8080/api/test

# Test blocked connectivity to DB tier (should fail)
curl http://10.100.30.10:3306
```

### ISE Integration Verification

**GUI:** `Tenants > Production > Security Policies > ISE Configuration > pxGrid Status`

**Check:**
- [ ] pxGrid connection: Connected
- [ ] Sessions synced
- [ ] Attributes received

**ISE GUI:** `Operations > pxGrid > Live Log`

**Verify:**
- [ ] APIC subscription active
- [ ] Session publishes successful

---

## 🐛 Common Issues

### Issue: Endpoints not learning

**Symptoms:** No endpoints in EPG operational tab

**Troubleshooting:**
```bash
# Check interface status
leaf-201# show interface ethernet 1/10

# Check VLAN encapsulation
leaf-201# show vlan

# Check endpoint database
leaf-201# show endpoint ip 10.100.10.10
```

**Resolution:**
- Verify static path binding configured
- Verify VLAN matches server configuration
- Verify physical connectivity

### Issue: Traffic blocked between EPGs

**Symptoms:** Ping/connectivity fails between tiers

**Troubleshooting:**
```bash
# Check contract status
leaf-201# show zoning-rule | grep Web-to-App

# Check endpoint classification
leaf-201# show endpoint detail
```

**Resolution:**
- Verify contracts applied (provider/consumer)
- Verify filter rules allow required traffic
- Check for deny rules in contract

### Issue: pxGrid connection failing

**Symptoms:** ISE integration shows "Disconnected"

**Troubleshooting:**
- Verify ISE IP reachable from APIC
- Verify certificate trust
- Check ISE pxGrid service running
- Review ISE pxGrid logs

**Resolution:**
- Re-import certificates
- Verify firewall rules allow TCP/8910 (pxGrid)
- Restart pxGrid service on ISE

---

## 📚 Next Steps

- [ ] [Configure ISE Captive Portal](ise-configuration.md)
- [ ] [Complete Integration Steps](integration-steps.md)
- [ ] [Setup Monitoring](../operations/monitoring.md)
- [ ] [Review Troubleshooting Guide](../operations/troubleshooting.md)

---

*Last updated: October 10, 2025* 