# 🐳 Containerized Development Environment

Professional development environment for the Tournament Organizer Documentation System using containerization to ensure consistency across all platforms and environments.

## 🎯 Why Containerization?

The issues we experienced with environment differences between local development (Windows/PowerShell) and CI/CD (Ubuntu/Linux) are exactly why professional teams use containers:

- **Environment Consistency**: Same environment everywhere
- **Dependency Management**: All tools and versions locked
- **Onboarding**: New developers get identical setup
- **CI/CD Reliability**: Same container in development and production
- **Security**: Isolated, rootless execution

## 🚀 Quick Start

### Prerequisites

Choose your container runtime:

**Podman (Recommended for Enterprise)**

```bash
# Installation varies by OS - see https://podman.io/getting-started/installation
# Ubuntu/Debian
sudo apt-get install podman podman-compose

# macOS
brew install podman podman-compose

# Windows
winget install RedHat.Podman
```

**Docker (Alternative)**

```bash
# See https://docs.docker.com/get-docker/
```

### Setup

1. **Run the setup script:**

   ```bash
   # Linux/macOS
   ./setup-dev-env.sh
   
   # Windows
   .\setup-dev-env.bat
   ```

2. **Source the environment:**

   ```bash
   # Linux/macOS
   source .env.local
   
   # Windows PowerShell
   . .\.env.local
   ```

## 📖 Available Commands

### Development

```bash
# Enter development shell
docs-dev

# Start development server (auto-reload)
docs-serve
# Access at: http://localhost:8001

# Run comprehensive quality checks
docs-qa

# Run specific linting
docs-lint

# Build documentation
docs-build

# Domain-specific linting
docs-domain-lint foundation
```

### Manual Commands

If you prefer manual control:

```bash
cd documents

# Development shell
podman compose run --rm docs-dev

# Serve documentation
podman compose up docs-serve

# Quality assurance
podman compose run --rm docs-qa

# Production server
podman compose up docs-production
```

## 🏗️ Container Architecture

### Multi-Stage Build

1. **Base Stage**: Python 3.13 + Node.js + System tools
2. **Development Stage**: All dev dependencies + source code
3. **Production Stage**: Built documentation + validation
4. **Serve Stage**: Nginx serving final documentation

### Services

- **docs-dev**: Interactive development environment
- **docs-serve**: Development server with auto-reload
- **docs-production**: Production-ready Nginx server
- **docs-qa**: Quality assurance automation

## 🔧 Environment Features

### Consistent Toolchain

- Python 3.13 with uv dependency management
- Node.js 18 with markdownlint-cli2
- Git for version control operations
- All system dependencies pre-installed

### Security

- Non-root user execution
- Isolated container environment
- Volume mounts with proper permissions
- Health checks for production services

### Performance

- Cached dependency layers
- Persistent volumes for caches
- Optimized build process
- Minimal production image

## 🚦 CI/CD Integration

The containerized environment is designed for CI/CD:

```yaml
# Example workflow step
- name: Run Quality Checks
  run: |
    cd documents
    docker compose run --rm docs-qa
```

### Benefits for CI/CD

- **Identical Environment**: Same container locally and in CI
- **Faster Builds**: Cached layers reduce build time
- **Reliability**: No environment-specific issues
- **Scalability**: Easy to parallelize across runners

## 🛠️ Development Workflow

### Daily Development

1. **Start Environment**:

   ```bash
   docs-dev
   ```

2. **Edit Documentation**: Use your preferred editor outside the container

3. **Live Preview**:

   ```bash
   docs-serve
   ```

4. **Quality Check**:

   ```bash
   docs-qa
   ```

5. **Build & Test**:

   ```bash
   docs-build
   ```

### Domain-Specific Work

```bash
# Check specific domain
docs-domain-lint identity

# Fix specific domain
docs-dev
uv run python scripts/linting/domain_linter.py identity --fix --auto-stage
```

## 🔍 Troubleshooting

### Common Issues

**Container won't start:**

```bash
# Check container runtime
podman --version
# or
docker --version

# Rebuild container
podman compose build --no-cache docs-dev
```

**Permission issues:**

```bash
# SELinux context (Fedora/RHEL)
podman compose run --rm docs-dev
```

**Port conflicts:**

```bash
# Check what's using the port
netstat -tulpn | grep :8000

# Use different port
podman compose run --rm -p 8002:8000 docs-serve
```

### Debug Mode

```bash
# Run with verbose output
podman compose run --rm docs-dev bash -x
```

## 🏢 Enterprise Considerations

### Security Benefits

- **Rootless Containers**: Podman runs without root privileges
- **Isolation**: Complete environment isolation
- **Audit Trail**: All operations within defined container
- **Compliance**: Easier security audits and compliance

### Scalability

- **Horizontal Scaling**: Easy to run multiple instances
- **Resource Management**: Container resource limits
- **Monitoring**: Container metrics and logging

### Integration

- **CI/CD Pipelines**: Seamless integration with any CI system
- **Development Teams**: Consistent environment for all developers
- **Production Deployment**: Same container artifact deployment

## 📚 Further Reading

- [Podman Documentation](https://docs.podman.io/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Container Best Practices](https://developers.redhat.com/blog/2016/02/24/10-things-to-avoid-in-docker-containers)

## 🎉 Migration Benefits

This containerized approach eliminates:

- ❌ Environment-specific bugs (Windows .cmd vs Linux executables)
- ❌ "Works on my machine" issues
- ❌ Complex local environment setup
- ❌ Dependency version conflicts
- ❌ CI/CD environment drift

And provides:

- ✅ Identical development environment for all team members
- ✅ Predictable CI/CD behavior
- ✅ Fast onboarding for new developers
- ✅ Professional enterprise-grade development workflow
- ✅ Easy scaling and deployment
