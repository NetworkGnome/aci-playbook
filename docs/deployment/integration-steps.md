# 🚀 Quick Start Guide

Get your Cisco ACI + ISE Integration Playbook up and running in minutes!

---

## 📋 What You'll Build

By following this guide, you'll have:
- ✅ Complete GitHub repository with all documentation
- ✅ Automation scripts ready to use
- ✅ Test plans and validation procedures
- ✅ Troubleshooting runbooks
- ✅ GitHub Pages documentation site (optional)

---

## ⚡ 5-Minute Setup

### Step 1: Create Repository

```bash
# Create new repository on GitHub.com
# Repository name: cisco-aci-ise-playbook
# Description: Enterprise playbook for ACI + ISE integration
# Visibility: Public (or Private for internal use)
# Initialize with: README (skip this, we'll add ours)

# Clone the empty repository
git clone https://github.com/yourusername/cisco-aci-ise-playbook.git
cd cisco-aci-ise-playbook
```

### Step 2: Create Base Structure

```bash
# Create all directories
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE
mkdir -p docs/{architecture,security,deployment,operations}
mkdir -p docs/architecture/diagrams
mkdir -p docs/deployment/checklists
mkdir -p docs/operations/runbooks
mkdir -p scripts/{python,ansible,terraform,bash}
mkdir -p scripts/ansible/{playbooks,roles}
mkdir -p scripts/terraform/{aci,ise}
mkdir -p configs/{aci-templates,ise-templates,examples}
mkdir -p tests/{test-plans,validation-scripts,test-results}
mkdir -p templates/{design-documents,executive-summaries,diagrams}
mkdir -p tools/{certificate-checker,config-validator,api-explorer}
mkdir -p wiki
mkdir -p assets/{images,files}
mkdir -p examples/{use-cases,api-integration}

# Create placeholder README files
touch docs/README.md
touch scripts/README.md
touch configs/README.md
touch tests/README.md
touch templates/README.md
touch tools/README.md
touch examples/README.md

echo "Directory structure created! ✅"
```

### Step 3: Add Core Files

**Create `.gitignore`:**

```bash
cat > .gitignore << 'EOF'
# Credentials and secrets
*.key
*.pem
*password*
*secret*
.env
vault.yml
credentials.yml

# Terraform
*.tfstate
*.tfstate.backup
.terraform/
terraform.tfvars
.terraform.lock.hcl

# Ansible
*.retry
group_vars/vault.yml
host_vars/vault.yml

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
env/
.pytest_cache/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.project
.classpath

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/
*.out

# Test results
test-results/*.xml
test-results/*.html
coverage/
.coverage

# Temporary files
tmp/
temp/
*.tmp
*.bak
*backup*

# Build artifacts
dist/
build/
site/
EOF
```

**Create LICENSE (MIT):**

```bash
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
```

### Step 4: Add Documentation Files

**Copy the artifacts I created into the appropriate locations:**

1. **README.md** → Root directory
2. **CONTRIBUTING.md** → Root directory
3. **docs/architecture/integration-flows.md**
4. **docs/architecture/aci-fabric-design.md**
5. **docs/architecture/ise-captive-portal.md**
6. **docs/deployment/aci-configuration.md**
7. **docs/operations/troubleshooting.md**
8. **tests/test-plans/test-plan-guest-access.md**
9. **scripts/python/ise-session-check.py**
10. **scripts/ansible/playbooks/ise-guest-portal-config.yml**

### Step 5: Initial Commit

```bash
# Stage all files
git add .

# Create initial commit
git commit -m "feat: initial playbook structure with core documentation"

# Push to GitHub
git push origin main
```

---

## 🎨 Optional: Setup GitHub Pages

### Method 1: Using MkDocs (Recommended)

**Install MkDocs:**

```bash
pip install mkdocs mkdocs-material
```

**Create `mkdocs.yml`:**

```yaml
site_name: Cisco ACI + ISE Integration Playbook
site_description: Enterprise playbook for ACI and ISE integration
site_author: Your Name
repo_url: https://github.com/yourusername/cisco-aci-ise-playbook
repo_name: cisco-aci-ise-playbook

theme:
  name: material
  palette:
    primary: blue
    accent: orange
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy

nav:
  - Home: index.md
  - Architecture:
    - Overview: architecture/README.md
    - ACI Fabric Design: architecture/aci-fabric-design.md
    - ISE Captive Portal: architecture/ise-captive-portal.md
    - Integration Flows: architecture/integration-flows.md
  - Deployment:
    - ACI Configuration: deployment/aci-configuration.md
    - ISE Configuration: deployment/ise-configuration.md
    - Integration Steps: deployment/integration-steps.md
  - Operations:
    - Troubleshooting: operations/troubleshooting.md
    - Testing: operations/testing-validation.md
    - Monitoring: operations/monitoring.md
  - Scripts:
    - Python: scripts/python/README.md
    - Ansible: scripts/ansible/README.md
    - Terraform: scripts/terraform/README.md

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.tabbed
  - admonition
  - codehilite
  - toc:
      permalink: true

plugins:
  - search
  - mermaid2
```

**Build and deploy:**

```bash
# Build site
mkdocs build

# Test locally
mkdocs serve
# Visit http://127.0.0.1:8000

# Deploy to GitHub Pages
mkdocs gh-deploy
```

### Method 2: GitHub Actions Auto-Deploy

**Create `.github/workflows/deploy-docs.yml`:**

```yaml
name: Deploy Documentation

on:
  push:
    branches:
      - main
    paths:
      - 'docs/**'
      - 'mkdocs.yml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x
      
      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material
      
      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
```

**Enable GitHub Pages:**
1. Go to repository Settings
2. Navigate to Pages
3. Source: Deploy from a branch
4. Branch: gh-pages
5. Folder: / (root)
6. Save

**Your docs will be available at:**
`https://yourusername.github.io/cisco-aci-ise-playbook/`

---

## 🔧 Setup Development Environment

### Python Environment

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r scripts/python/requirements.txt
```

**Create `scripts/python/requirements.txt`:**

```
requests>=2.28.0
urllib3>=1.26.0
python-dotenv>=0.20.0
PyYAML>=6.0
jinja2>=3.1.0
```

### Ansible Environment

```bash
# Install Ansible
pip install ansible

# Install Cisco ISE collection
ansible-galaxy collection install cisco.ise

# Install ACI collection
ansible-galaxy collection install cisco.aci
```

### Terraform Environment

```bash
# Install Terraform
# Visit: https://www.terraform.io/downloads

# Initialize Terraform (from scripts/terraform/)
cd scripts/terraform
terraform init
```

---

## 📝 Create Your First Content

### Add a New Documentation Page

```bash
# Create new document
cat > docs/deployment/wlc-configuration.md << 'EOF'
# Wireless LAN Controller Configuration

**Document Version:** 1.0  
**Last Updated:** October 10, 2025

## Overview

This guide covers WLC configuration for guest access...

## Prerequisites

- [ ] WLC deployed and accessible
- [ ] Management IP configured
- [ ] ISE IP address known

## Configuration Steps

### Step 1: Add RADIUS Server

...
EOF

# Add to git
git add docs/deployment/wlc-configuration.md
git commit -m "docs: add WLC configuration guide"
git push
```

### Add a New Script

```bash
# Create new Python script
cat > scripts/python/check_ise_health.py << 'EOF'
#!/usr/bin/env python3
"""
ISE Health Checker
Validates ISE services and connectivity
"""

import requests

def check_ise_health(server):
    # Implementation
    pass

if __name__ == "__main__":
    check_ise_health("ise.company.com")
EOF

# Make executable
chmod +x scripts/python/check_ise_health.py

# Add to git
git add scripts/python/check_ise_health.py
git commit -m "feat: add ISE health checker script"
git push
```

---

## 🤝 Enable Collaboration

### Setup Issue Templates

**Create `.github/ISSUE_TEMPLATE/bug_report.md`:**

```markdown
---
name: Bug Report
about: Report a bug or issue
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run command '...'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
- ACI Version: [e.g. 5.2(4e)]
- ISE Version: [e.g. 3.1 P5]
- Script/Tool: [e.g. ise-session-check.py]

**Additional context**
Add any other context, logs, or screenshots.
```

### Setup Branch Protection

1. Go to repository Settings → Branches
2. Add rule for `main` branch:
   - ✅ Require pull request reviews
   - ✅ Require status checks to pass
   - ✅ Require conversation resolution
   - ✅ Include administrators

---

## 📊 Monitor Your Repository

### Add Badges to README

```markdown
![Documentation](https://img.shields.io/badge/docs-latest-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![GitHub Stars](https://img.shields.io/github/stars/yourusername/cisco-aci-ise-playbook)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/cisco-aci-ise-playbook)
![Issues](https://img.shields.io/github/issues/yourusername/cisco-aci-ise-playbook)
```

### Setup GitHub Actions for Linting

**Create `.github/workflows/markdown-lint.yml`:**

```yaml
name: Markdown Lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Lint Markdown files
        uses: articulate/actions-markdownlint@v1
        with:
          config: .markdownlint.json
          files: 'docs/**/*.md'
```

---

## ✅ Verification Checklist

After setup, verify:

- [ ] Repository created on GitHub
- [ ] All directories created locally
- [ ] Core documentation files added
- [ ] Scripts directory populated
- [ ] Initial commit pushed
- [ ] GitHub Pages enabled (optional)
- [ ] Issue templates created
- [ ] Branch protection enabled
- [ ] README badges working
- [ ] Documentation renders correctly

---

## 🎉 Next Steps

**You're ready to go! Here's what to do next:**

1. **Customize Content**
   - Update company-specific information
   - Add your topology diagrams
   - Include your configuration examples

2. **Invite Collaborators**
   - Add team members to repository
   - Assign roles (maintainers, contributors)
   - Create first issues for improvements

3. **Start Using**
   - Reference docs during deployments
   - Use scripts for automation
   - Run test plans for validation

4. **Share**
   - Announce to your team
   - Post to internal wiki
   - Share on LinkedIn/Twitter (if public)

---

## 🆘 Need Help?

- **Documentation Issues:** Open an issue on GitHub
- **Questions:** Use GitHub Discussions
- **Cisco TAC:** For product support
- **Community:** r/Cisco, r/networking

---

**Congratulations! Your Cisco ACI + ISE Integration Playbook is live!** 🚀

---

*Last updated: October 10, 2025*