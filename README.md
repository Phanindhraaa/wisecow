# Wisecow: Kubernetes Deployment with Zero-Trust Security & DevSecOps

> Enterprise-grade Kubernetes deployment showcasing production-ready DevSecOps practices, zero-trust security architecture, and infrastructure automation.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.x+-green.svg)](https://kubernetes.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

## Overview

Wisecow is a comprehensive Kubernetes deployment project that demonstrates enterprise-level security practices, infrastructure automation, and DevSecOps principles. The project implements zero-trust security models, TLS/SSL encryption, and production-grade operational workflows.

### Key Features

🔐 **Security-First Architecture**
- Zero-trust network policies enforcing least-privilege access
- TLS/SSL certificate-based secure communication
- Secrets management with encrypted credentials
- Pod-to-pod communication controls

☸️ **Kubernetes Infrastructure**
- Production-ready deployment manifests (YAML)
- Service discovery and load balancing
- Ingress controller configuration for traffic routing
- Network policies for defense-in-depth
- Resource quotas and limits

🛡️ **Container Security**
- Optimized Docker images with minimal attack surface
- Security scanning and vulnerability assessments
- Non-root user execution policies
- Read-only root filesystem configurations

🔧 **Operational Excellence**
- Automated backup and recovery scripts (Python)
- Real-time health checks and monitoring
- System metrics collection
- Graceful shutdown procedures

## Project Structure

```
wisecow/
├── Dockerfile                    # Container image definition
├── backup.py                     # Automated backup script
├── monitor.py                    # Health monitoring script
├── wisecow.sh                    # Deployment automation script
├── tls.crt                       # TLS certificate
├── tls.key                       # TLS private key (encrypted)
├── wisecow-deployment.yaml       # Kubernetes deployment manifest
├── wisecow-service.yaml          # Kubernetes service definition
├── wisecow-ingress.yaml          # Ingress controller configuration
└── wisecow-zero-trust-policy.yaml # Network policy for zero-trust
```

## Security Architecture

### Zero-Trust Model

The project implements a zero-trust security architecture where:
- All network traffic is encrypted using TLS 1.2+
- Pod-to-pod communication is restricted via network policies
- Service accounts are created with minimal permissions
- RBAC (Role-Based Access Control) restricts API access

### Network Policies

Network policies enforce:
- Ingress rules: Only allow traffic from authorized sources
- Egress rules: Restrict outbound connections to trusted services
- Label-based filtering: Fine-grained traffic control
- Default-deny posture: Block all traffic not explicitly allowed

### Secrets Management

- Sensitive data (API keys, passwords) stored as Kubernetes Secrets
- TLS certificates managed securely
- Encryption at rest and in transit
- Regular rotation policies

## Deployment Guide

### Prerequisites

- Kubernetes cluster (v1.20+)
- kubectl configured with cluster access
- Docker (for building custom images)
- Python 3.x (for operational scripts)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Phanindhraaa/wisecow.git
   cd wisecow
   ```

2. **Create TLS certificates** (if not already present)
   ```bash
   # Using self-signed certificates for development
   # For production, use proper certificate authority
   bash wisecow.sh generate-certs
   ```

3. **Deploy to Kubernetes**
   ```bash
   # Create namespace
   kubectl create namespace wisecow

   # Apply Kubernetes manifests
   kubectl apply -f wisecow-deployment.yaml
   kubectl apply -f wisecow-service.yaml
   kubectl apply -f wisecow-ingress.yaml
   kubectl apply -f wisecow-zero-trust-policy.yaml
   ```

4. **Verify deployment**
   ```bash
   kubectl get pods -n wisecow
   kubectl get svc -n wisecow
   kubectl get networkpolicies -n wisecow
   ```

### Running Operational Scripts

**Health Monitoring**
```bash
python monitor.py --namespace wisecow --interval 30
```

**Automated Backups**
```bash
python backup.py --source /data --destination /backup --compress
```

## Configuration

### Environment Variables

- `NAMESPACE`: Kubernetes namespace (default: wisecow)
- `REPLICAS`: Number of pod replicas (default: 3)
- `LOG_LEVEL`: Logging verbosity (default: info)
- `TLS_ENABLED`: Enable TLS encryption (default: true)

### Kubernetes Resources

**Deployment**: Manages application pods with:
- Resource requests and limits
- Health checks (liveness and readiness probes)
- Graceful shutdown (terminationGracePeriodSeconds)
- Security context with non-root user

**Service**: Exposes the application with:
- ClusterIP for internal communication
- NodePort for external access (optional)
- Session affinity for stateful workloads

**NetworkPolicy**: Implements zero-trust with:
- Pod-to-pod communication rules
- Egress restrictions
- Default-deny ingress/egress

## Monitoring & Observability

### Health Checks

- **Liveness Probe**: Ensures pod is running (TCP connection)
- **Readiness Probe**: Indicates pod is ready for traffic
- **Startup Probe**: Waits for application initialization

### Metrics Collection

Monitor the following metrics:
- Pod CPU and memory usage
- Network I/O statistics
- Application-specific metrics
- Disk space utilization

### Log Aggregation

Logs are collected from:
- Container stdout/stderr
- Kubernetes events
- Application logs
- System logs

## Best Practices Demonstrated

✅ **Infrastructure as Code (IaC)**
- All infrastructure defined in version-controlled YAML files
- Reproducible deployments across environments
- GitOps-friendly configuration

✅ **Security-First Approach**
- Defense-in-depth security layers
- Least-privilege access principles
- Regular security audits and scanning

✅ **High Availability**
- Multi-replica deployments
- Automated health checks
- Graceful failure handling

✅ **Production Readiness**
- Comprehensive monitoring and alerting
- Automated backup and recovery
- Proper resource management
- Rolling update strategies

## Troubleshooting

### Pod not starting
```bash
kubectl logs -n wisecow <pod-name>
kubectl describe pod -n wisecow <pod-name>
```

### Network connectivity issues
```bash
kubectl get networkpolicies -n wisecow
kubectl describe networkpolicy wisecow-zero-trust-policy
```

### TLS certificate errors
```bash
kubectl get secret -n wisecow
kubectl describe secret wisecow-tls-secret
```

## Performance Considerations

- **CPU/Memory**: Configure based on workload requirements
- **Network Policies**: Overhead minimal but monitor performance
- **TLS**: Enable hardware acceleration when available
- **Storage**: Use persistent volumes for stateful data

## Security Compliance

This project aligns with:
- NIST Cybersecurity Framework
- CIS Kubernetes Benchmarks
- Zero Trust Architecture principles
- Defense Information Systems Agency (DISA) guidelines

## Learning Outcomes

This project demonstrates proficiency in:
- ✓ Kubernetes cluster architecture and management
- ✓ Zero-trust security design patterns
- ✓ Container orchestration and deployment
- ✓ Infrastructure automation and IaC
- ✓ DevSecOps practices and tooling
- ✓ Networking and security policies
- ✓ Production-grade operations

## Technologies Used

- **Container Orchestration**: Kubernetes 1.20+
- **Containerization**: Docker
- **Security**: TLS 1.2+, RBAC, Network Policies
- **Scripting**: Python 3.x, Bash
- **Configuration**: YAML, Kubernetes manifests
- **Monitoring**: kubectl, custom Python scripts

## Contributing

Contributions are welcome! Please follow these guidelines:
1. Create a feature branch
2. Make your changes with clear commit messages
3. Test thoroughly before submitting a pull request
4. Update documentation as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Phanindhra Sura**
- GitHub: [@Phanindhraaa](https://github.com/Phanindhraaa)
- LinkedIn: [Phanindhra Sura](https://linkedin.com/in/phanindhra-sura-895bb4250)

## Acknowledgments

This project showcases best practices from:
- Kubernetes official documentation
- NIST zero-trust architecture guidelines
- Cloud Security Alliance standards
- Community DevSecOps practices

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section

---

**Last Updated**: December 2025
**Version**: 1.0.0
