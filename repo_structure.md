# 📁 Repository Structure

Complete directory layout for the Cisco ACI + ISE Integration Playbook

---

## Directory Tree

```
cisco-aci-ise-playbook/
│
├── README.md                          # Main landing page
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── CHANGELOG.md                       # Version history
├── .gitignore                         # Git ignore rules
│
├── .github/
│   ├── workflows/
│   │   ├── markdown-lint.yml         # Markdown validation
│   │   ├── link-checker.yml          # Check broken links
│   │   └── deploy-docs.yml           # Deploy to GitHub Pages
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md             # Bug report template
│   │   ├── feature_request.md        # Feature request template
│   │   └── documentation.md          # Documentation improvement
│   └── PULL_REQUEST_TEMPLATE.md      # PR template
│
├── docs/
│   ├── README.md                      # Documentation index
│   │
│   ├── architecture/
│   │   ├── README.md                  # Architecture overview
│   │   ├── aci-fabric-design.md       # ACI design patterns
│   │   ├── ise-captive-portal.md      # ISE portal architecture
│   │   ├── integration-flows.md       # pxGrid integration
│   │   ├── multi-site-design.md       # Multi-site topologies
│   │   └── diagrams/
│   │       ├── high-level-topology.png
│   │       ├── pxgrid-flow.png
│   │       ├── guest-workflow.mmd     # Mermaid source
│   │       └── visio-templates/
│   │
│   ├── security/
│   │   ├── README.md
│   │   ├── zero-trust-segmentation.md
│   │   ├── nac-posture-flow.md
│   │   ├── certificates-hardening.md
│   │   ├── compliance-guide.md        # GDPR, HIPAA, PCI-DSS
│   │   └── threat-mitigation.md
│   │
│   ├── deployment/
│   │   ├── README.md
│   │   ├── aci-configuration.md       # Step-by-step ACI setup
│   │   ├── ise-configuration.md       # Step-by-step ISE setup
│   │   ├── wlc-configuration.md       # WLC setup
│   │   ├── integration-steps.md       # End-to-end integration
│   │   ├── vmm-integration.md         # VMware/Hyper-V integration
│   │   └── checklists/
│   │       ├── pre-deployment-checklist.md
│   │       ├── deployment-checklist.md
│   │       ├── post-deployment-checklist.md
│   │       └── integration-checklist.md
│   │
│   └── operations/
│       ├── README.md
│       ├── testing-validation.md
│       ├── troubleshooting.md          # Complete troubleshooting guide
│       ├── monitoring.md               # Monitoring setup
│       ├── backup-restore.md           # Backup procedures
│       ├── maintenance.md              # Maintenance procedures
│       ├── log-analysis.md             # Log analysis guide
│       └── runbooks/
│           ├── guest-access-issue.md
│           ├── pxgrid-failure.md
│           ├── ise-psn-failure.md
│           └── aci-fabric-issue.md
│
├── scripts/
│   ├── README.md                       # Scripts documentation
│   │
│   ├── python/
│   │   ├── README.md
│   │   ├── requirements.txt            # Python dependencies
│   │   ├── ise-session-check.py        # ISE session validator
│   │   ├── aci-endpoint-report.py      # ACI endpoint reporter
│   │   ├── pxgrid-monitor.py           # pxGrid health checker
│   │   ├── guest-account-bulk.py       # Bulk guest creation
│   │   ├── policy-audit.py             # Policy compliance checker
│   │   └── lib/
│   │       ├── __init__.py
│   │       ├── ise_api.py              # ISE API wrapper
│   │       ├── aci_api.py              # ACI API wrapper
│   │       └── utils.py                # Common utilities
│   │
│   ├── ansible/
│   │   ├── README.md
│   │   ├── ansible.cfg                 # Ansible configuration
│   │   ├── inventory.yml.example       # Inventory template
│   │   ├── group_vars/
│   │   │   ├── all.yml.example
│   │   │   └── ise_servers.yml.example
│   │   ├── playbooks/
│   │   │   ├── ise-guest-portal-config.yml
│   │   │   ├── aci-tenant-deploy.yml
│   │   │   ├── integration-setup.yml
│   │   │   ├── backup-config.yml
│   │   │   └── health-check.yml
│   │   └── roles/
│   │       ├── ise-base/
│   │       │   ├── tasks/
│   │       │   ├── templates/
│   │       │   ├── vars/
│   │       │   └── defaults/
│   │       ├── aci-fabric/
│   │       └── pxgrid-integration/
│   │
│   ├── terraform/
│   │   ├── README.md
│   │   ├── versions.tf                 # Provider versions
│   │   ├── main.tf                     # Main configuration
│   │   ├── variables.tf                # Input variables
│   │   ├── outputs.tf                  # Output values
│   │   ├── terraform.tfvars.example    # Example variables
│   │   ├── aci/
│   │   │   ├── tenant.tf               # ACI tenant config
│   │   │   ├── networking.tf           # VRF, BD, EPG
│   │   │   ├── contracts.tf            # Policy contracts
│   │   │   └── modules/
│   │   │       ├── three-tier-app/
│   │   │       └── guest-access/
│   │   └── ise/
│   │       ├── guest-portal.tf
│   │       ├── policy-sets.tf
│   │       ├── authorization.tf
│   │       └── modules/
│   │           └── guest-access/
│   │
│   └── bash/
│       ├── README.md
│       ├── ise-backup.sh               # ISE backup script
│       ├── aci-config-export.sh        # Export ACI config
│       ├── log-collector.sh            # Collect logs
│       └── health-check.sh             # Quick health check
│
├── configs/
│   ├── README.md
│   │
│   ├── aci-templates/
│   │   ├── tenant-template.json
│   │   ├── three-tier-app.xml
│   │   ├── guest-access-epg.json
│   │   ├── contract-templates/
│   │   │   ├── web-to-app.json
│   │   │   ├── app-to-db.json
│   │   │   └── internet-access.json
│   │   └── vmm-domain.xml
│   │
│   ├── ise-templates/
│   │   ├── guest-portal-config.xml
│   │   ├── policy-set-guest.xml
│   │   ├── authorization-profile.xml
│   │   ├── sponsor-group.xml
│   │   └── network-device.xml
│   │
│   └── examples/
│       ├── README.md
│       ├── small-deployment/           # <100 users
│       │   ├── aci-config.json
│       │   └── ise-config.xml
│       ├── medium-deployment/          # 100-1000 users
│       │   ├── aci-config.json
│       │   └── ise-config.xml
│       └── enterprise-deployment/      # >1000 users
│           ├── aci-config.json
│           ├── ise-config.xml
│           └── topology-diagram.png
│
├── tests/
│   ├── README.md
│   │
│   ├── test-plans/
│   │   ├── test-plan-guest-access.md
│   │   ├── test-plan-pxgrid.md
│   │   ├── test-plan-failover.md
│   │   ├── test-plan-performance.md
│   │   └── test-plan-security.md
│   │
│   ├── validation-scripts/
│   │   ├── test-guest-workflow.py
│   │   ├── test-pxgrid-sync.py
│   │   ├── test-epg-assignment.py
│   │   ├── test-portal-redirect.py
│   │   └── load-test-guests.py
│   │
│   └── test-results/
│       ├── .gitkeep
│       └── template-test-report.md
│
├── templates/
│   ├── README.md
│   │
│   ├── design-documents/
│   │   ├── technical-design-template.md
│   │   ├── high-level-design-template.md
│   │   ├── low-level-design-template.md
│   │   └── solution-overview-template.pptx
│   │
│   ├── executive-summaries/
│   │   ├── executive-summary-template.md
│   │   ├── roi-analysis-template.xlsx
│   │   └── project-status-template.pptx
│   │
│   └── diagrams/
│       ├── visio-templates/
│       │   ├── aci-topology.vsdx
│       │   ├── ise-architecture.vsdx
│       │   └── integration-flow.vsdx
│       ├── lucidchart-templates/
│       │   └── README.md
│       └── draw-io-templates/
│           ├── aci-fabric.drawio
│           └── guest-workflow.drawio
│
├── tools/
│   ├── README.md
│   ├── certificate-checker/
│   │   ├── check-certs.py
│   │   └── README.md
│   ├── config-validator/
│   │   ├── validate-aci.py
│   │   ├── validate-ise.py
│   │   └── README.md
│   └── api-explorer/
│       ├── ise-api-examples.py
│       ├── aci-api-examples.py
│       └── README.md
│
├── wiki/                               # For GitHub Wiki
│   ├── Home.md
│   ├── Getting-Started.md
│   ├── FAQ.md
│   ├── Glossary.md
│   ├── Best-Practices.md
│   └── Troubleshooting-Quick-Reference.md
│
├── assets/
│   ├── images/
│   │   ├── logos/
│   │   │   ├── cisco-logo.png
│   │   │   └── aci-logo.png
│   │   ├── screenshots/
│   │   │   ├── apic-dashboard.png
│   │   │   ├── ise-portal.png
│   │   │   └── guest-flow/
│   │   └── diagrams/
│   │       └── (generated from docs/architecture/diagrams/)
│   │
│   └── files/
│       ├── certificates/
│       │   └── README.md               # Instructions only, no actual certs
│       └── sample-data/
│           ├── guest-users-sample.csv
│           └── endpoints-sample.json
│
└── examples/
    ├── README.md
    ├── use-cases/
    │   ├── healthcare-guest-access/
    │   │   ├── README.md
    │   │   ├── requirements.md
    │   │   ├── design.md
    │   │   └── configs/
    │   ├── university-campus/
    │   │   ├── README.md
    │   │   └── configs/
    │   ├── retail-guest-wifi/
    │   │   ├── README.md
    │   │   └── configs/
    │   └── enterprise-visitor-access/
    │       ├── README.md
    │       └── configs/
    │
    └── api-integration/
        ├── python-sdk-examples/
        │   ├── ise-guest-crud.py
        │   ├── aci-tenant-mgmt.py
        │   └── pxgrid-subscriber.py
        ├── rest-api-examples/
        │   ├── ise-api-collection.postman.json
        │   └── aci-api-collection.postman.json
        └── webhook-examples/
            ├── ise-webhook-listener.py
            └── teams-notification.py
```

---

## File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| `README.md` | Main landing page with overview, quick start, and navigation |
| `LICENSE` | MIT License for open source usage |
| `CONTRIBUTING.md` | Guidelines for contributing to the project |
| `CHANGELOG.md` | Version history and release notes |
| `.gitignore` | Git ignore rules (credentials, temp files, etc.) |

### `.github/` Directory

Contains GitHub-specific configurations:
- **Workflows:** CI/CD automation for linting, testing, deployment
- **Issue Templates:** Standardized bug reports and feature requests
- **PR Template:** Pull request checklist

### `docs/` Directory

Main documentation organized by category:
- **architecture/**: Design patterns and reference architectures
- **security/**: Security hardening and compliance guides
- **deployment/**: Step-by-step configuration guides
- **operations/**: Day-2 operations, troubleshooting, monitoring

### `scripts/` Directory

Automation scripts in multiple languages:
- **python/**: ISE/ACI API scripts, monitoring tools
- **ansible/**: Configuration management playbooks
- **terraform/**: Infrastructure as Code
- **bash/**: Shell scripts for quick tasks

### `configs/` Directory

Configuration templates and examples:
- **aci-templates/**: JSON/XML templates for ACI objects
- **ise-templates/**: XML templates for ISE configuration
- **examples/**: Complete deployment examples by size

### `tests/` Directory

Testing materials:
- **test-plans/**: Detailed test cases
- **validation-scripts/**: Automated test scripts
- **test-results/**: Test execution results (gitignored)

### `templates/` Directory

Document templates:
- **design-documents/**: Technical and high-level design templates
- **executive-summaries/**: Business stakeholder templates
- **diagrams/**: Visio, Lucidchart, draw.io templates

### `tools/` Directory

Helper utilities:
- **certificate-checker/**: Validate SSL certificates
- **config-validator/**: Syntax checking for configs
- **api-explorer/**: Interactive API testing

### `wiki/` Directory

Content for GitHub Wiki:
- Quick reference guides
- FAQ
- Glossary of terms

### `assets/` Directory

Binary files:
- **images/**: Screenshots, logos, diagrams
- **files/**: Sample data, documentation assets

### `examples/` Directory

Real-world use cases:
- Industry-specific implementations
- API integration examples
- Webhook integrations

---

## File Naming Conventions

### Markdown Files
- Use lowercase with hyphens: `aci-fabric-design.md`
- Be descriptive: `ise-guest-portal-config.md` not `config.md`

### Scripts
- Use lowercase with hyphens or underscores
- Python: `ise_session_check.py`
- Bash: `health-check.sh`

### Configuration Files
- Include technology prefix: `aci-tenant-template.json`
- Use version suffix if applicable: `ise-config-v3.1.xml`

### Diagrams
- Use descriptive names: `pxgrid-flow-diagram.png`
- Include source files: `pxgrid-flow.drawio`

---

## `.gitignore` Contents

```gitignore
# Credentials and secrets
*.key
*.pem
*password*
*secret*
.env
vault.yml

# Terraform
*.tfstate
*.tfstate.backup
.terraform/
terraform.tfvars

# Ansible
*.retry
group_vars/vault.yml

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
.pytest_cache/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Test results
test-results/*.xml
test-results/*.html

# Temporary files
tmp/
temp/
*.tmp

# Backup files
*.bak
*backup*
```

---

## GitHub Pages Structure

If deploying documentation to GitHub Pages:

```
docs/ (for GitHub Pages)
├── index.html
├── _config.yml              # Jekyll configuration
├── assets/
│   ├── css/
│   └── js/
└── [mirrors main docs/ structure]
```

**Or use MkDocs:**

```
mkdocs.yml                   # MkDocs configuration
docs/                        # Source markdown
site/                        # Generated static site (gitignored)
```

---

## Repository Size Optimization

**Keep Repository Lean:**
- Don't commit large binary files (use Git LFS if needed)
- Don't commit sensitive data
- Don't commit test result files
- Use `.gitignore` effectively

**Use Git LFS for:**
- Large Visio files (>5MB)
- Video tutorials
- Large sample datasets

---

## Maintenance

### Regular Updates
- Review and update documentation quarterly
- Keep script dependencies current
- Update configuration templates for new software versions
- Archive deprecated content

### Version Control
- Tag major releases: `v1.0.0`, `v1.1.0`, etc.
- Use semantic versioning
- Maintain CHANGELOG.md

---

## Quick Start for Contributors

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/yourusername/cisco-aci-ise-playbook.git
   cd cisco-aci-ise-playbook
   ```

3. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make changes** following the structure above

5. **Test your changes:**
   ```bash
   # Run markdown linter
   markdownlint docs/
   
   # Run Python tests
   pytest tests/
   ```

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "feat: add new ISE profiling guide"
   git push origin feature/your-feature-name
   ```

7. **Open Pull Request** on GitHub

---

*This structure is designed to be scalable, maintainable, and community-friendly.*

**Last updated:** October 10, 2025