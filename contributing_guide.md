# Contributing to Cisco ACI + ISE Integration Playbook

First off, thank you for considering contributing to this playbook! 🎉

The following is a set of guidelines for contributing to this project. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Documentation Standards](#documentation-standards)

---

## 📜 Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow:

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Be professional** in all interactions
- **Focus on what is best** for the community

---

## 🤝 How Can I Contribute?

### Reporting Bugs

**Before submitting a bug report:**
- Check the [existing issues](https://github.com/yourusername/cisco-aci-ise-playbook/issues)
- Verify the issue with latest documentation
- Collect relevant logs and configurations (sanitized)

**When submitting a bug report, include:**
- Clear, descriptive title
- Steps to reproduce
- Expected vs. actual behavior
- Software versions (APIC, ISE, WLC)
- Screenshots or logs (sanitized)

### Suggesting Enhancements

We welcome feature requests and documentation improvements!

**Enhancement suggestions should include:**
- Clear use case or problem statement
- Proposed solution or approach
- Relevant examples or references

### Contributing Documentation

Documentation contributions are highly valued:

**Types of documentation contributions:**
- New architecture patterns
- Configuration guides
- Troubleshooting procedures
- Automation scripts
- Diagrams and visual aids
- Real-world case studies

### Contributing Code

**Types of code contributions:**
- Python automation scripts
- Ansible playbooks
- Terraform modules
- Testing scripts
- API integrations

---

## 🎨 Style Guidelines

### Markdown Style Guide

**File Naming:**
- Use lowercase with hyphens: `aci-fabric-design.md`
- Be descriptive: `ise-guest-portal-config.md` not `config.md`

**Document Structure:**
```markdown
# Main Title (H1 - Only one per document)

Brief introduction paragraph.

## Section Title (H2)

Content here.

### Subsection (H3)

More specific content.

#### Sub-subsection (H4)

Use sparingly.
```

**Formatting Standards:**
- Use **bold** for UI elements: Click **Tenants** → **Add Tenant**
- Use `code blocks` for commands, variables, or code
- Use > blockquotes for important notes or warnings
- Use tables for structured data comparison

**Code Blocks:**
````markdown
```bash
# Always specify language for syntax highlighting
apic1# show controller
```

```python
# Python example with comments
def example():
    pass
```
````

**Links:**
- Use relative links for internal docs: `[ACI Design](../architecture/aci-fabric-design.md)`
- Use full URLs for external references
- Check all links before submitting

**Images and Diagrams:**
- Store in `docs/<section>/images/` directory
- Use descriptive filenames: `pxgrid-flow-diagram.png`
- Include alt text: `![pxGrid Integration Flow](images/pxgrid-flow.png)`
- Keep file sizes reasonable (<500KB)

### Python Style Guide

Follow **PEP 8** standards:

```python
#!/usr/bin/env python3
"""
Module docstring explaining purpose.
"""

import os
import sys
from typing import Dict, List

# Constants in CAPS
ISE_BASE_URL = "https://ise.example.com:9060"

class ISEClient:
    """Class docstring."""
    
    def __init__(self, server: str, username: str, password: str):
        """Constructor docstring."""
        self.server = server
        self.username = username
        self.password = password
    
    def get_sessions(self) -> List[Dict]:
        """
        Retrieve active sessions from ISE.
        
        Returns:
            List of session dictionaries
        """
        pass

# Type hints for function parameters
def main() -> None:
    """Main function."""
    pass

if __name__ == "__main__":
    main()
```

**Requirements:**
- Include docstrings for all functions/classes
- Use type hints
- Handle exceptions appropriately
- Include example usage in docstring or comments
- Add requirements.txt or poetry dependencies

### Ansible Style Guide

```yaml
---
# Playbook description
- name: Configure ISE Guest Portal
  hosts: ise_nodes
  gather_facts: no
  
  vars:
    ise_username: "{{ vault_ise_username }}"
    ise_password: "{{ vault_ise_password }}"
  
  tasks:
    - name: Create guest portal configuration
      cisco.ise.guest_portal:
        state: present
        name: "Corporate_Guest"
        settings:
          portal_type: "SPONSORED_GUEST"
      register: portal_result
      
    - name: Display result
      ansible.builtin.debug:
        var: portal_result
```

**Standards:**
- Use descriptive task names
- Employ `register` for output capture
- Use `tags` for selective execution
- Vault-encrypt sensitive variables
- Include example inventory files

### Terraform Style Guide

```hcl
# ISE Policy Set Configuration

terraform {
  required_version = ">= 1.3.0"
  
  required_providers {
    ise = {
      source  = "CiscoISE/ise"
      version = "~> 0.7"
    }
  }
}

variable "ise_username" {
  description = "ISE Admin Username"
  type        = string
  sensitive   = true
}

resource "ise_network_access_policy_set" "guest_access" {
  name        = "Guest_Access_Policy"
  description = "Policy set for guest wireless access"
  rank        = 0
  
  condition {
    attribute_name  = "Wireless_SSID"
    operator        = "equals"
    attribute_value = "Guest-WiFi"
  }
}

output "policy_set_id" {
  description = "Created policy set ID"
  value       = ise_network_access_policy_set.guest_access.id
}
```

**Standards:**
- Use meaningful resource names
- Include descriptions for all variables
- Mark sensitive variables
- Provide example `terraform.tfvars`
- Document outputs

---

## 💬 Commit Messages

Follow the **Conventional Commits** specification:

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature or documentation section
- **fix**: Bug fix or correction
- **docs**: Documentation only changes
- **style**: Formatting, missing semicolons, etc.
- **refactor**: Code/doc restructuring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples
```bash
feat(deployment): add ISE distributed deployment guide

- Added step-by-step instructions for ISE deployment
- Included HA configuration checklist
- Added diagrams for deployment topology

Closes #42

---

fix(scripts): correct ISE API authentication error

The authentication header was malformed causing 401 errors.
Updated to use base64 encoding for basic auth.

Fixes #58

---

docs(architecture): update ACI multi-site design patterns

- Added stretched L3Out examples
- Clarified IPN requirements
- Updated diagrams to reflect APIC 5.2 changes
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Test your changes:**
   - Scripts: Run in lab environment
   - Documentation: Verify all links work
   - Code: Run linters (pylint, yamllint, markdownlint)

2. **Update documentation:**
   - Add/update relevant docs
   - Update CHANGELOG.md
   - Add yourself to contributors if first PR

3. **Check formatting:**
   - Run markdown linter: `markdownlint docs/`
   - Format code: `black scripts/python/`
   - Check YAML: `yamllint scripts/ansible/`

### Submitting Pull Request

1. **Fork and create branch:**
   ```bash
   git checkout -b feature/ise-profiling-guide
   ```

2. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "feat(deployment): add ISE profiling guide"
   ```

3. **Push to your fork:**
   ```bash
   git push origin feature/ise-profiling-guide
   ```

4. **Open Pull Request:**
   - Use descriptive title
   - Reference related issues
   - Fill out PR template completely
   - Add appropriate labels

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New documentation
- [ ] Bug fix
- [ ] New automation script
- [ ] Enhancement to existing content

## Testing
Describe how you tested your changes

## Checklist
- [ ] I have tested these changes
- [ ] I have updated documentation
- [ ] I have added comments to complex code
- [ ] All links are working
- [ ] I have run linters
- [ ] CHANGELOG.md is updated

## Related Issues
Closes #XX
```

### Review Process

1. **Automated checks** must pass (linters, link checkers)
2. **Peer review** by at least one maintainer
3. **Testing verification** in lab environment (for scripts)
4. **Documentation review** for clarity and completeness

### After Approval

- Maintainer will merge using **squash and merge**
- PR will be linked in release notes
- Contributors will be credited

---

## 📚 Documentation Standards

### Document Templates

Use provided templates in `templates/` directory:
- Technical design documents
- Configuration guides
- Troubleshooting procedures
- Test plans

### Required Sections

**Configuration Guides Must Include:**
1. **Overview** - What this configures
2. **Prerequisites** - Required setup
3. **Step-by-Step Instructions** - CLI and GUI
4. **Verification** - How to confirm success
5. **Troubleshooting** - Common issues
6. **References** - Related documentation

**Architecture Documents Must Include:**
1. **Design Overview** - High-level description
2. **Requirements** - Functional and non-functional
3. **Architecture Diagram** - Visual representation
4. **Component Details** - Deep dive per component
5. **Traffic Flows** - How data moves through system
6. **Scaling Considerations** - Growth planning
7. **Security Considerations** - Security implications

### Diagrams

**Diagram Standards:**
- Use **draw.io**, **Lucidchart**, or **Mermaid** (preferred)
- Export as PNG and source file
- Store in `docs/<section>/diagrams/`
- Include diagram in markdown as image
- Provide source file for editing

**Mermaid Example:**
```markdown
## Integration Flow

\`\`\`mermaid
sequenceDiagram
    participant Client
    participant WLC
    participant ISE
    participant ACI
    
    Client->>WLC: 802.1X Authentication
    WLC->>ISE: RADIUS Access-Request
    ISE->>WLC: Access-Accept + VLAN
    ISE->>ACI: pxGrid Session
    ACI->>ACI: Assign EPG
\`\`\`
```

### Code Examples

**All code examples must include:**
- Language specification in code block
- Comments explaining logic
- Error handling
- Sample output
- Usage instructions

### Versioning

**Document versioning:**
- Note software versions tested
- Include date of last update
- Mark deprecated content clearly
- Update changelog for major revisions

---

## 🎯 What We're Looking For

**High Priority Contributions:**
- Real-world deployment examples
- Troubleshooting procedures with solutions
- Automation scripts (Python, Ansible, Terraform)
- Performance tuning guides
- Security hardening procedures
- Integration with other systems (DNA-C, SecureX, etc.)

**Always Welcome:**
- Typo corrections
- Broken link fixes
- Diagram improvements
- Additional test cases
- Translation improvements

---

## 📞 Getting Help

**Questions about contributing?**
- Open a [GitHub Discussion](https://github.com/yourusername/cisco-aci-ise-playbook/discussions)
- Check the [Wiki](https://github.com/yourusername/cisco-aci-ise-playbook/wiki)
- Tag maintainers in issues: @maintainer1 @maintainer2

**Need technical help with Cisco products?**
- Cisco TAC for support contracts
- Cisco Community Forums
- Cisco DevNet

---

## 🏆 Recognition

Contributors will be recognized in:
- Project README.md
- Release notes
- Annual contributor spotlight

**Top contributors may receive:**
- Maintainer access
- Featured blog posts
- Conference presentation opportunities

---

## 📅 Release Cycle

- **Minor updates:** Weekly (typos, small fixes)
- **Feature releases:** Monthly (new guides, scripts)
- **Major releases:** Quarterly (significant content additions)

---

**Thank you for contributing to making network automation more accessible!** 🚀

*Last updated: October 10, 2025*