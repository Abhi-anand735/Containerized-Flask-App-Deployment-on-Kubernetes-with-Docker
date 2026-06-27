# Containerized-Flask-App-Deployment-on-Kubernetes-with-Docker

Project Overview:

This project demonstrates how to build containerize and deploy a Python Flask web application using Docker and Kubernetes. The application is packaged into a Docker image, pushed to Docker Hub, and deployed on a local Kubernetes cluster using Minikube. The project also demonstrates Kubernetes concepts such as Deployments, Services, ConfigMaps, Namespaces, and Horizontal Pod Autoscaling (HPA),rolling update deployment, rollback.

Core Features:

- Supported rolling updates for zero or minimal downtime during deployments
- Configured multiple Pod replicas for high availability
- Implemented Horizontal Pod Autoscaler (HPA) for automatic scaling based on CPU utilization


Project Architecture:

![image alt](https://github.com/Abhi-anand735/Containerized-Flask-App-Deployment-on-Kubernetes-with-Docker/blob/526ebae5851c3574e5e75f79c88cec03b43fde4d/architecture.png)

Tech stack used in this project:

- Python (Backend Application)
- Flask (Web Framework)
- Docker	Containerization)
- Docker Hub	(Image Registry)
- Kubernetes	(Container Orchestration)
- Minikube	(Local Kubernetes Cluster)
- kubectl	(Kubernetes CLI)
- Git	(Version Control)
- GitHub	(Source Code Repository)
- YAML (Kubernetes Configuration)

Prerequisites:

- Python 3.12+
- Docker Desktop
- Docker Hub Account
- Minikube
- kubectl
- Git

Installation:

 - Verify Git installation
   ```bash
   git --version 
   ```

 - Verify Python version
   ```bash
    python --version
   ```

 - Install Docker
   ```bash 
   sudo apt install docker.io
   ```

 - Install kubectl
   ```bash
   kubectl version --client
   ```

 - Install Minikube
   ```bash
   minikube version
   ```

 - Start Minikube
   ```bash
   minikube start --driver=docker
   ```

 - Verify Kubernetes Cluster
    ```bash
    kubectl get nodes 
    ```

 - Enable Metrics Server (Required for HPA)
   ```bash
   minikube addons enable metrics-server  
   ```
   
 - Clone the Repository
   ```bash
   
   ```
Challenges faced:

- Fixing port conflicts when port 5000 was already in use
- Troubleshooting Pod failures such as CrashLoopBackOff and ImagePullBackOff
- Managing Docker image tags and versioning.
  
 
   
    


