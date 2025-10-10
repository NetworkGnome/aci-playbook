# Guest Access Validation Test Plan

**Document Version:** 1.0  
**Last Updated:** October 10, 2025  
**Test Environment:** Production/Staging  
**Status:** ✅ Ready for Execution

---

## 📋 Table of Contents

- [Test Overview](#test-overview)
- [Test Environment](#test-environment)
- [Pre-Test Requirements](#pre-test-requirements)
- [Functional Tests](#functional-tests)
- [Integration Tests](#integration-tests)
- [Performance Tests](#performance-tests)
- [Failover Tests](#failover-tests)
- [Security Tests](#security-tests)
- [Test Results Template](#test-results-template)

---

## 🎯 Test Overview

### Objectives

This test plan validates the complete guest wireless access solution integrating:
- Cisco ACI fabric
- Cisco ISE captive portal
- Cisco Wireless LAN Controllers (WLC)
- pxGrid integration for dynamic EPG assignment

### Success Criteria

✅ Guest users can successfully register and authenticate  
✅ Captive portal redirects properly  
✅ Network access granted after authentication  
✅ Dynamic EPG assignment via pxGrid functional  
✅ Session timeout enforced correctly  
✅ Sponsor approval workflow functional  
✅ All security policies enforced  
✅ System handles 1000+ concurrent guests (performance test)  
✅ Failover occurs within SLA (<30 seconds)

### Test Scope

**In Scope:**
- Guest self-registration
- Sponsored guest access
- Hotspot (AUP-only) access
- pxGrid session synchronization
- Multi-device support per guest
- Session expiration
- High availability failover

**Out of Scope:**
- BYOD device registration (separate test plan)
- 802.1X corporate access
- VPN integration
- MDM integration

---

## 🏗️ Test Environment

### Infrastructure

```
┌─────────────────────────────────────────────────────┐
│              Test Environment Topology              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [ISE-PSN-1]  [ISE-PSN-2]                          │
│       └──────────┬──────────┘                      │
│                  │                                  │
│            [Load Balancer]                          │
│              10.10.20.100                           │
│                  │                                  │
│                  │ pxGrid                           │
│                  ↓                                  │
│            [APIC Cluster]                           │
│                  │                                  │
│         [ACI Fabric Switches]                       │
│                  │                                  │
│         [WLC-1]  [WLC-2]                           │
│            │        │                               │
│         [AP-1]  [AP-2]  [AP-3]                     │
│            │        │       │                       │
│      [Test Clients: iOS, Android, Windows, Mac]    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Component Versions

| Component | Version | Role |
|-----------|---------|------|
| APIC | 5.2(4e) | Fabric controller |
| ISE | 3.1 Patch 5 | AAA & Guest portal |
| WLC | 17.9.4 (9800 series) | Wireless controller |
| ACI Switches | 15.2(4e) | Leaf/Spine switches |

### Test Devices

| Device Type | Quantity | OS Version |
|-------------|----------|------------|
| iPhone | 2 | iOS 17 |
| Android | 2 | Android 14 |
| Windows Laptop | 2 | Windows 11 |
| MacBook | 2 | macOS Sonoma |
| Linux Laptop | 1 | Ubuntu 22.04 |

---

## ✅ Pre-Test Requirements

### Configuration Checklist

- [ ] ISE guest portal configured and accessible
- [ ] Guest SSID "Guest-WiFi" created on WLC
- [ ] Pre-authentication ACL configured
- [ ] Post-authentication ACL configured
- [ ] RADIUS shared secret configured
- [ ] ACI tenant and EPGs created
- [ ] pxGrid integration configured
- [ ] Load balancer configured for ISE PSN nodes
- [ ] DNS records created for portal FQDN
- [ ] SSL certificates installed and trusted
- [ ] Email server configured for notifications
- [ ] SMS gateway configured (if applicable)
- [ ] Sponsor accounts created

### Test Account Preparation

**Sponsor Accounts:**
- sponsor1@company.com (IT Admin)
- sponsor2@company.com (Facilities)

**Pre-Created Guest Accounts:**
- testguest1@company.com (Valid for 24 hours)
- testguest2@company.com (Expired account - for negative testing)

**Self-Registration Test:**
- Use personal email addresses for testing

---

## 🧪 Functional Tests

### Test Case 1: Hotspot Access (AUP Only)

**Test ID:** FT-001  
**Priority:** High  
**Prerequisites:** Guest SSID configured for hotspot access

**Test Steps:**

1. Connect device to "Guest-WiFi" SSID
2. Open web browser
3. Navigate to http://www.cisco.com
4. Verify automatic redirect to ISE portal
5. Review Acceptable Use Policy
6. Click "Accept"
7. Verify internet access granted

**Expected Results:**
- ✅ Device receives IP address from guest VLAN
- ✅ Browser redirects to ISE portal within 5 seconds
- ✅ AUP displays correctly
- ✅ Internet access granted after acceptance
- ✅ Session logged in ISE

**Test Data:**

| Step | Input | Expected Output |
|------|-------|----------------|
| Connect | SSID: Guest-WiFi | IP: 10.200.1.x/24 |
| Browse | www.cisco.com | Redirect to https://guest.company.com:8443 |
| Accept | Click "Accept" | Full internet access |

**Pass/Fail:** [ ]  
**Tester:** _______________  
**Date:** _______________  
**Notes:** _______________

---

### Test Case 2: Self-Registration Flow

**Test ID:** FT-002  
**Priority:** High  
**Prerequisites:** Self-registration enabled on guest portal

**Test Steps:**

1. Connect device to "Guest-WiFi" SSID
2. Browser redirects to ISE portal
3. Click "Create Account"
4. Fill registration form:
   - First Name: John
   - Last Name: Doe
   - Email: john.doe@gmail.com
   - Phone: +1-555-0123
   - Company: Acme Corp
5. Select location: "Building A"
6. Submit registration
7. Check email for verification code
8. Enter verification code
9. Set password
10. Login with new credentials
11. Accept AUP
12. Verify internet access

**Expected Results:**
- ✅ Registration form displays all required fields
- ✅ Email verification code received within 2 minutes
- ✅ Password meets complexity requirements
- ✅ Account created successfully
- ✅ Login successful
- ✅ Internet access granted
- ✅ Session visible in ISE live logs

**Pass/Fail:** [ ]  
**Tester:** _______________  
**Date:** _______________

---

### Test Case 3: Sponsored Guest Flow

**Test ID:** FT-003  
**Priority:** High  
**Prerequisites:** Sponsor accounts configured

**Test Steps:**

1. As Guest: Connect to "Guest-WiFi" SSID
2. Portal redirects, click "Request Access"
3. Fill form:
   - Name: Jane Smith
   - Email: jane.smith@visitor.com
   - Sponsor: sponsor1@company.com
   - Reason: Customer meeting
4. Submit request
5. As Sponsor: Check email for approval request
6. Click link to sponsor portal
7. Login as sponsor1@company.com
8. Review guest request
9. Approve access with:
   - Duration: 8 hours
   - Max devices: 2
10. As Guest: Check email for credentials
11. Login with provided credentials
12. Verify internet access

**Expected Results:**
- ✅ Sponsor receives email within 2 minutes
- ✅ Sponsor can approve from email link
- ✅ Guest receives credentials via email
- ✅ Guest can login successfully
- ✅ Access expires after 8 hours
- ✅ Max 2 devices enforcedTest Case 4: Multi-Device Support

**Test ID:** FT-004  
**Priority:** Medium  
**Prerequisites:** Guest account allows 5 devices

**Test Steps:**

1. Login with guest account on Device 1 (iPhone)
2. Verify internet access on Device 1
3. Login with same account on Device 2 (Android)
4. Verify internet access on Device 2
5. Verify Device 1 still has access
6. Login on Devices 3, 4, 5 (Windows, Mac, Linux)
7. Attempt to login on Device 6
8. Verify Device 6 is denied or Device 1 disconnected

**Expected Results:**
- ✅ Up to 5 devices can use same account simultaneously
- ✅ 6th device triggers max device limit
- ✅ ISE logs show all device sessions
- ✅ All devices in same EPG on ACI

**Pass/Fail:** [ ]  
**Tester:** _______________

---

### Test Case 5: Session Expiration

**Test ID:** FT-005  
**Priority:** High  
**Prerequisites:** Guest account with 1-hour validity

**Test Steps:**

1. Create guest account with 1-hour duration
2. Login and verify access
3. Note start time
4. Wait 55 minutes
5. Verify access still working
6. Wait until 65 minutes (5 min past expiration)
7. Try to access internet
8. Verify access denied
9. Check ISE for session termination

**Expected Results:**
- ✅ Access works before expiration
- ✅ Access denied after expiration
- ✅ ISE terminates session automatically
- ✅ User must re-authenticate

**Pass/Fail:** [ ]  
**Tester:** _______________

---

## 🔗 Integration Tests

### Test Case 6: pxGrid Session Sync

**Test ID:** IT-001  
**Priority:** Critical  
**Prerequisites:** pxGrid configured between ISE and APIC

**Test Steps:**

1. Login guest to portal
2. Check ISE Operations > pxGrid > Live Log
3. Verify session published to APIC
4. Check APIC: Tenants > EPG > Operational > Endpoints
5. Verify endpoint appears with correct attributes
6. Note SGT (Security Group Tag) if configured
7. Verify endpoint in correct dynamic EPG
8. Logout guest
9. Verify endpoint removed from APIC

**Expected Results:**
- ✅ Session appears in pxGrid log within 5 seconds
- ✅ Endpoint learned in APIC with ISE attributes
- ✅ Correct EPG assignment
- ✅ Endpoint removed after logout

**Pass/Fail:** [ ]  
**Tester:** _______________

---

### Test Case 7: Dynamic EPG Assignment

**Test ID:** IT-002  
**Priority:** Critical  
**Prerequisites:** Attribute-based EPG configured

**Test Steps:**

1. Login as guest with SGT=10
2. Verify placement in Guest-Dynamic-EPG
3. Verify contracts applied to Guest-Dynamic-EPG
4. Test connectivity to allowed resources (internet)
5. Test connectivity to denied resources (internal servers)
6. Verify blocked traffic shows in ACI contract stats

**Expected Results:**
- ✅ Guest assigned to Guest-Dynamic-EPG
- ✅ Can access internet
- ✅ Cannot access internal corporate network
- ✅ Policy enforcement visible in ACI

**Pass/Fail:** [ ]  
**Tester:** _______________

---

## ⚡ Performance Tests

### Test Case 8: Concurrent Guest Load

**Test ID:** PT-001  
**Priority:** High  
**Prerequisites:** Load testing tool (JMeter, Locust)

**Test Steps:**

1. Prepare 1000 test guest accounts
2. Configure load test:
   - Ramp up: 100 users per minute
   - Target: 1000 concurrent users
   - Duration: 30 minutes
3. Start load test
4. Monitor ISE CPU/memory
5. Monitor APIC performance
6. Monitor WLC client count
7. Record authentication response times
8. Check for any failures

**Expected Results:**
- ✅ System handles 1000 concurrent guests
- ✅ ISE CPU < 80%
- ✅ ISE memory < 80%
- ✅ Authentication time < 3 seconds average
- ✅ Zero authentication failures
- ✅ Portal remains responsive

**Metrics to Collect:**

| Metric | Target | Actual |
|--------|--------|--------|
| Concurrent Users | 1000 | ___ |
| Auth Success Rate | >99% | ___% |
| Avg Auth Time | <3s | ___s |
| ISE CPU | <80% | ___% |
| ISE Memory | <80% | ___% |

**Pass/Fail:** [ ]  
**Tester:** _______________

---

## 🔄 Failover Tests

### Test Case 9: ISE PSN Failover

**Test ID:** FO-001  
**Priority:** Critical  
**Prerequisites:** 2 ISE PSN nodes with load balancer

**Test Steps:**

1. Verify 50 active guest sessions
2. Identify which PSN is handling sessions
3. Shutdown primary PSN (simulate failure)
4. Verify load balancer detects failure
5. Existing users: test internet connectivity
6. New user: attempt registration
7. Monitor failover time
8. Verify all sessions moved to secondary PSN
9. Bring primary PSN back online
10. Verify sessions rebalance

**Expected Results:**
- ✅ Existing sessions: minimal disruption (<30s)
- ✅ New sessions: immediate redirect to healthy PSN
- ✅ Zero session data loss
- ✅ Automatic recovery when PSN restored

**Pass/Fail:** [ ]  
**Tester:** _______________

---

### Test Case 10: WLC Failover

**Test ID:** FO-002  
**Priority:** Critical  
**Prerequisites:** Redundant WLC deployment

**Test Steps:**

1. Connect 20 guests to AP managed by WLC-1
2. Note client associations
3. Shutdown WLC-1
4. Monitor client behavior
5. Verify clients re-associate to WLC-2
6. Verify sessions maintained in ISE
7. Test internet connectivity
8. Measure failover time

**Expected Results:**
- ✅ Clients re-associate within 10 seconds
- ✅ ISE sessions maintained
- ✅ Internet access restored automatically
- ✅ No re-authentication required

**Pass/Fail:** [ ]  
**Tester:** _______________

---

## 🔐 Security Tests

### Test Case 11: Unauthorized Access Attempts

**Test ID:** ST-001  
**Priority:** High  
**Prerequisites:** Security policies configured

**Test Steps:**

1. As guest, attempt to access internal server (10.1.1.10)
2. Verify connection blocked
3. Attempt to access corporate AD server
4. Verify connection blocked
5. Attempt SQL injection on portal login form
6. Verify input sanitized
7. Attempt XSS attack on registration form
8. Verify script tags escaped
9. Review ISE logs for security events

**Expected Results:**
- ✅ All internal resources blocked
- ✅ SQL injection attempts logged and blocked
- ✅ XSS attempts neutralized
- ✅ Security events logged

**Pass/Fail:** [ ]  
**Tester:** _______________

---

### Test Case 12: Certificate Validation

**Test ID:** ST-002  
**Priority:** High  
**Prerequisites:** Valid SSL certificate installed

**Test Steps:**

1. Access guest portal via HTTPS
2. Verify browser shows secure connection
3. Check certificate details:
   - Issuer: Trusted CA
   - Subject: guest.company.com
   - Validity: Current date within range
   - Key length: 2048-bit or higher
4. Test with expired certificate (lab environment)
5. Verify browser warning appears

**Expected Results:**
- ✅ Valid certificate from trusted CA
- ✅ No browser security warnings
- ✅ Certificate matches portal FQDN
- ✅ Strong encryption (TLS 1.2+)

**Pass/Fail:** [ ]  
**Tester:** _______________

---

## 📊 Test Results Template

### Summary Report

**Test Execution Date:** _______________  
**Environment:** Production / Staging  
**Test Lead:** _______________

**Overall Results:**

| Category | Total Tests | Passed | Failed | Blocked | Pass Rate |
|----------|-------------|--------|--------|---------|-----------|
| Functional | 5 | ___ | ___ | ___ | ___% |
| Integration | 2 | ___ | ___ | ___ | ___% |
| Performance | 1 | ___ | ___ | ___ | ___% |
| Failover | 2 | ___ | ___ | ___ | ___% |
| Security | 2 | ___ | ___ | ___ | ___% |
| **TOTAL** | **12** | ___ | ___ | ___ | ___% |

**Defects Found:**

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| DEF-001 | High | Portal redirect fails on iOS 16 | Open |
| DEF-002 | Medium | Email delay >5 minutes | Investigating |

**Sign-Off:**

**Tested By:** _______________ **Date:** _______________  
**Reviewed By:** _______________ **Date:** _______________  
**Approved By:** _______________ **Date:** _______________

---

*Last updated: October 10, 2025*