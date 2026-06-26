# Containerized-Flask-App-Deployment-on-Kubernetes-with-Docker

Project Overview:

This project demonstrates how to build containerize and deploy a Python Flask web application using Docker and Kubernetes. The application is packaged into a Docker image, pushed to Docker Hub, and deployed on a local Kubernetes cluster using Minikube. The project also demonstrates Kubernetes concepts such as Deployments, Services, ConfigMaps, Secrets, Namespaces, and Horizontal Pod Autoscaling (HPA).

Project Architecture:

![image alt](https://github.com/Abhi-anand735/Containerized-Flask-App-Deployment-on-Kubernetes-with-Docker/blob/526ebae5851c3574e5e75f79c88cec03b43fde4d/architecture.png)

Tech stack used in this project:

.Python (Backend Application)
.Flask (Web Framework)
.Docker	Containerization)
.Docker Hub	(Image Registry)
.Kubernetes	(Container Orchestration)
.Minikube	(Local Kubernetes Cluster)
.kubectl	(Kubernetes CLI)
.Git	(Version Control)
.GitHub	(Source Code Repository)
.YAML (Kubernetes Configuration)

Prerequisites:

Python 3.12+
Docker Desktop
Docker Hub Account
Minikube
kubectl
Git

Installation:

Clone Repository


 Build Docker Image


 Run Docker Container


 Push Docker Image


 Kubernetes Deployment
 minikube start

 Create Namespace
kubectl apply -f kubernetes/namespace.yaml


