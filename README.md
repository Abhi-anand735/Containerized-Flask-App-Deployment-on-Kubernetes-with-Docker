# Containerized-Flask-App-Deployment-on-Kubernetes-with-Docker

Project Overview:

This project demonstrates how to build containerize and deploy a Python Flask web application using Docker and Kubernetes. The application is packaged into a Docker image, pushed to Docker Hub, and deployed on a local Kubernetes cluster using Minikube. The project also demonstrates Kubernetes concepts such as Deployments, Services, ConfigMaps, Namespaces, and Horizontal Pod Autoscaling (HPA),rolling update deployment, rollback.

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

 - Clone Repository:
   git clone https://github.com/Abhi-anand735/Containerized-Flask-App-Deployment-on-Kubernetes-with-            Docker.git

 - Build Docker Image:
    docker build -t flask-k8s .

 - Run Docker Container:
    docker run -d -p 5000:5000 flask-k8s

 - Docker Image tag:
    docker tag flask-k8s:latest abhianand77/flask-k8s:v1.0

 - push docker image:
    docker push abhianand77/flask-k8s:v1.0

 - Kubernetes Deployment:
    minikube start

 - Create Namespace:
    kubectl apply -f kubernetes/namespace.yaml 

 - create deployment:
    kubectl apply -f kubernetes/deployment.yaml -n flask-app
   
 - create service:
    kubectl apply -f kubernetes/service.yaml -n flask-app

 - verify deployment: 
    kubectl get deployments -n flask-app

 - scale deployment:
    kubectl scale deployment/flask-deployment --replicas=5 -n flask-app
   
 - Access Application:
    minikube service flask-service -n flask-app


