---
# Ansible Playbook: Configure ISE Guest Portal
# Description: Automates ISE guest portal configuration
# Author: Network Automation Team
# Version: 1.0
# Date: October 10, 2025
#
# Requirements:
#   - Ansible 2.12+
#   - cisco.ise collection
#   - ISE ERS API enabled
#
# Usage:
#   ansible-playbook ise-guest-portal-config.yml -i inventory.yml

- name: Configure Cisco ISE Guest Portal
  hosts: ise_servers
  gather_facts: no
  connection: local
  
  vars:
    # ISE Connection Parameters (override in inventory or vault)
    ise_hostname: "{{ inventory_hostname }}"
    ise_username: "{{ lookup('env', 'ISE_USERNAME') | default('admin') }}"
    ise_password: "{{ lookup('env', 'ISE_PASSWORD') | default('changeme') }}"
    ise_verify: false
    ise_debug: false
    
    # Portal Configuration
    portal_name: "Corporate_Guest_Portal"
    portal_description: "Self-service guest access portal"
    portal_type: "SELF_REGISTERED_GUEST"
    
    # Guest User Settings
    guest_ssid: "Guest-WiFi"
    guest_location: "Corporate Headquarters"
    max_devices_per_guest: 5
    session_duration_hours: 8
    
    # Sponsor Settings
    sponsor_group: "IT_Sponsors"
    sponsor_email