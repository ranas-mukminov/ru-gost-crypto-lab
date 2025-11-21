# 🔐 ru-gost-crypto-lab

[![CI](https://github.com/ranas-mukminov/ru-gost-crypto-lab/workflows/CI/badge.svg)](https://github.com/ranas-mukminov/ru-gost-crypto-lab/actions)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

🇬🇧 English | 🇷🇺 [Русская версия](README.ru.md)

**Laboratory stand for testing infrastructure with Russian GOST cryptography (TLS, S/MIME, VPN).**

Author: [Ranas Mukminov](https://github.com/ranas-mukminov) | Website: [run-as-daemon.ru](https://run-as-daemon.ru)

---

## Overview

**ru-gost-crypto-lab** is a comprehensive laboratory environment and toolset for testing, validating, and benchmarking infrastructure components that use Russian GOST cryptographic standards. This project provides Infrastructure-as-Code (IaC) templates, compatibility testing tools, and performance benchmarking scripts to help DevOps engineers, system administrators, and security specialists evaluate GOST-based solutions before production deployment.

This is a **testing and education platform**, not a production backup tool. For production-grade encrypted backups with GOST support, see [gost-backup-vault](https://github.com/ranas-mukminov/gost-backup-vault).

The project targets organizations that need to comply with Russian regulatory requirements (FSTEC, FSB) or want to experiment with GOST cryptography in web servers, mail systems, and VPN configurations.

## Key Features

- **Ready-to-use IaC scenarios**: Docker Compose and Ansible templates for deploying Web (Nginx/HAProxy with GOST TLS), Mail (Postfix/Dovecot with S/MIME), and VPN services
- **Compatibility testing suite**: Automated checks to verify which browsers, mail clients, and VPN clients can successfully connect to GOST-enabled services
- **Performance benchmarking**: Scripts to measure TLS handshake times, connection throughput, and VPN performance with GOST ciphersuites
- **Modular Python toolkit**: Clean, type-hinted Python 3.11+ modules for configuration loading, scenario generation, and report building
- **AI-powered insights**: Extensible AI provider interface for automated analysis of test results and recommendations
- **Multi-language reporting**: Generate detailed compatibility and performance reports in English or Russian
- **CI/CD ready**: GitHub Actions workflows for linting, security scanning (Bandit), and automated testing
- **No proprietary binaries**: Only open configurations and synthetic test data—users install their own licensed SKZI/cryptographic providers
- **Educational focus**: Clear documentation, examples, and test scenarios designed for learning and experimentation

## Architecture / Components

The project consists of several layers:

- **User Interface**: CLI tools for scenario generation and report builders (Markdown, JSON)
- **Testing & Analysis Layer**: Compatibility checks (TLS, S/MIME, VPN) and performance benchmarks (handshake, throughput)
- **Configuration Layer**: YAML scenario parser and config validation
- **Infrastructure Layer (IaC)**: Docker Compose and Ansible templates for Web, Mail, VPN stacks
- **Lab Scenarios**: YAML definitions for different deployment scenarios

**Key components:**
- Nginx/HAProxy with GOST TLS ciphersuites
- Postfix/Dovecot with S/MIME support (planned)
- strongSwan/OpenVPN with GOST algorithms (planned)
- Python tools for compatibility checking, performance benchmarks, and report generation

## Requirements

### Operating System

- **Ubuntu 20.04+** or **Debian 11+** (primary support)
- **RHEL 8+**, **Rocky Linux 8+**, **AlmaLinux 8+** (compatible)
- **macOS** (for development; Docker Desktop required)

### Software Dependencies

- **Docker**: 20.10+ and Docker Compose 1.29+ (or Docker Compose V2)
- **Python**: 3.11 or higher
- **pip**: Latest version recommended
- **Git**: For repository cloning

### Hardware Recommendations

- **CPU**: 2+ cores (4+ recommended for performance testing)
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk**: 10 GB free space for Docker images and logs

### Network Requirements

- **Internet access**: To pull Docker images and install Python packages
- **Open ports**: 443 (HTTPS), 25/587/993 (mail, if testing), 500/4500 (VPN, if testing)

### Optional Dependencies

- **GOST cryptographic provider**: CryptoPro CSP, ViPNet, or other licensed SKZI (NOT included; user must install separately)
- **Ansible**: 2.12+ (only if using Ansible IaC templates)
- **openssl with GOST engine**: For manual certificate generation and testing

> [!IMPORTANT]
> This repository does NOT include proprietary SKZI binaries. You must obtain and install cryptographic providers according to your licenses and local regulations.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ranas-mukminov/ru-gost-crypto-lab.git
cd ru-gost-crypto-lab
```

### 2. Install Python Dependencies

```bash
pip install --upgrade pip
pip install .
```

For development:

```bash
pip install .[dev]
```

### 3. Start the Lab Environment

```bash
docker-compose -f iac/docker-compose/docker-compose.web.yml up -d
```

This starts Nginx on port 443 (HTTPS) and a backend application on port 8080.

### 4. Run Compatibility Tests

```bash
python3 -m tools.compatibility.check_tls_clients --target localhost:443
```

### 5. Stop the Lab

```bash
docker-compose -f iac/docker-compose/docker-compose.web.yml down
```

## Installation

### Ubuntu / Debian

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose -y

# Install Python 3.11+
sudo apt install python3.11 python3-pip -y

# Clone and install project
git clone https://github.com/ranas-mukminov/ru-gost-crypto-lab.git
cd ru-gost-crypto-lab
pip install .
```

### RHEL / Rocky / AlmaLinux

```bash
# Update system
sudo dnf update -y

# Add Docker repository and install
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Docker Compose
sudo dnf install docker-compose-plugin -y

# Install Python 3.11
sudo dnf install python3.11 python3.11-pip -y

# Clone and install
git clone https://github.com/ranas-mukminov/ru-gost-crypto-lab.git
cd ru-gost-crypto-lab
python3.11 -m pip install .
```

## Configuration

### Docker Compose Example

Located in `iac/docker-compose/docker-compose.web.yml`. Mount your GOST certificates:

```yaml
volumes:
  - /path/to/gost-cert.pem:/etc/nginx/ssl/cert.pem:ro
  - /path/to/gost-key.pem:/etc/nginx/ssl/key.pem:ro
```

### Scenario Definition

Example in `lab_scenarios/web_portal_gov/scenario.yaml`:

```yaml
name: web_portal_gov
type: web_tls
topology:
  services:
    - nginx_gost
    - backend_app
test_plan:
  compatibility: true
  performance: true
```

### Environment Variables

Create a `.env` file:

```bash
COMPOSE_PROJECT_NAME=gost_lab
TEST_TARGET_HOST=localhost
TEST_TARGET_PORT=443
REPORT_LANGUAGE=en  # or 'ru'
```

## Usage

### Start/Stop Services

```bash
# Start
docker-compose -f iac/docker-compose/docker-compose.web.yml up -d

# Stop
docker-compose -f iac/docker-compose/docker-compose.web.yml down

# View logs
docker-compose -f iac/docker-compose/docker-compose.web.yml logs -f
```

### Run Tests

```bash
# TLS compatibility
python3 -m tools.compatibility.check_tls_clients --target <SERVER_IP>:443

# TLS handshake time
python3 -m tools.perf.bench_tls_handshake --target <SERVER_IP>:443

# TLS throughput
python3 -m tools.perf.bench_tls_throughput --target <SERVER_IP>:443
```

### Generate Reports

```bash
python3 -m tools.reports.report_builder --output report.md --language en
```

## Update / Upgrade

```bash
cd ru-gost-crypto-lab
git pull origin main
pip install --upgrade .
docker-compose pull
docker-compose up -d
```

Check [CHANGELOG.md](CHANGELOG.md) for breaking changes.

## Troubleshooting

### Common Issues

**Service not starting:**
```bash
docker-compose logs <service_name>
```

**Port already in use:**
```bash
sudo lsof -i :443
sudo systemctl stop nginx
```

**Permission denied (Docker):**
```bash
sudo usermod -aG docker $USER
# Logout and login again
```

**TLS handshake failures:**
```bash
openssl s_client -connect localhost:443
openssl engine gost
```

**Module not found:**
```bash
pip install .
# Or for development
pip install -e .
```

## Security Notes

> [!CAUTION]
> This is a **laboratory environment**. Do not expose it directly to the public Internet without additional hardening.

- **Change default passwords** if any services have default credentials
- **Restrict access** using firewall rules or VPN
- **Do not use production keys** - all certificates and keys should be test-only
- **Keep Docker images updated**: `docker-compose pull`
- **Use HTTPS/VPN for remote access**
- **No real user data** in the lab environment

See [LEGAL.md](LEGAL.md) for detailed legal disclaimers and compliance notes.

## Project Structure

```
ru-gost-crypto-lab/
├── .github/workflows/      # CI/CD pipelines (lint, test, security scan)
├── iac/                    # Infrastructure-as-Code templates
│   ├── ansible/            # Ansible roles
│   └── docker-compose/     # Docker Compose files
├── lab_scenarios/          # YAML scenario definitions
├── scripts/                # Helper scripts (lint, test, security scan)
├── tests/                  # Test suite (pytest)
│   ├── integration/
│   └── unit/
├── tools/                  # Python modules
│   ├── ai/                 # AI provider interface
│   ├── compatibility/      # TLS, S/MIME, VPN checks
│   ├── perf/               # Performance benchmarks
│   └── reports/            # Report generation
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LEGAL.md
├── LICENSE
├── README.md
├── README.ru.md
└── pyproject.toml
```

## Roadmap

### Current Status (v0.1.0)

- ✅ Basic project structure
- ✅ Docker Compose template for Web TLS
- ✅ Python modules for config/scenario loading
- ✅ Stub implementations for compatibility and performance testing
- ✅ CI/CD with GitHub Actions
- ✅ Bilingual documentation (EN/RU)

### Planned

- Additional scenarios (Mail, VPN)
- Real compatibility checks with actual SSL/TLS connections
- Performance metrics with Prometheus
- AI-powered analysis and recommendations
- Grafana dashboards
- Ansible playbooks for multi-host deployments
- Certificate automation scripts

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and commit: `git commit -m "Add feature"`
4. Push to your fork: `git push origin feature/my-feature`
5. Open a Pull Request

### Requirements

All PRs must pass:
- Linting: `./scripts/lint.sh`
- Tests: `./scripts/dev_run_all_tests.sh`
- Security scan: `./scripts/security_scan.sh`
- Codex Code Review: Add comment `@codex review`

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

Apache License 2.0. See [LICENSE](LICENSE) for full text.

## Author and Commercial Support

**Author:** [Ranas Mukminov](https://github.com/ranas-mukminov)

**Website:** [run-as-daemon.ru](https://run-as-daemon.ru)

### Commercial Services

For production deployments, custom lab scenarios, and professional support:

- Lab deployment and configuration for your infrastructure
- Compatibility audits and comprehensive reports
- Performance analysis and optimization
- SKZI selection and integration consulting
- Training and workshops for DevOps/security teams
- Ongoing support and maintenance

Contact via [run-as-daemon.ru](https://run-as-daemon.ru) or [GitHub profile](https://github.com/ranas-mukminov).

---

**Disclaimer:** This project is provided "as is" without warranty. Users are responsible for compliance with all applicable laws and regulations regarding cryptography.
