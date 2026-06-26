- Clone Repository
   ```bash
   'git clone https://github.com/Abhi-anand735/Containerized-Flask-App-Deployment-on-Kubernetes-with-            Docker.git
   ```

 - Build Docker Image
   ```bash
   docker build -t flask-k8s .
   ```

 - Run Docker Container
   ```bash 
   docker run -d -p 5000:5000 flask-k8s
   ```

 - Docker Image tag
   ```bash
   docker tag flask-k8s:latest abhianand77/flask-k8s:v1.0
   ```

 - push docker image
   ```bash
   docker push abhianand77/flask-k8s:v1.0
   ```

 - Kubernetes cluster
   ```bash
   minikube start
   ```
   ```bash
   minikube status
   ```

 - Create Namespace
   ```bash
   kubectl apply -f kubernetes/namespace.yaml
    ```

 - create deployment
   ```bash
   kubectl apply -f kubernetes/deployment.yaml -n flask-app
   ```
   
 - create service
   ```bash
   kubectl apply -f kubernetes/service.yaml -n flask-app
   ```

 - verify deployment
   ```bash
    kubectl get deployments -n flask-app
   ```

 - scale deployment
   ```bash
   kubectl scale deployment/flask-deployment --replicas=5 -n flask-app
   ```
 - Rolling update
   ```bash
   docker build -t flask-app:v2 .
   ```
  ```bash
  docker tag flask-app:v2 abhiananad77/flask-app:v3
  ```
  ```bash
  docker push abhianand77/flask-app:v3
  ```
  ```bash
  kubectl set image deployment/flask-deployment \ flask-container=abhianand77/flask-app:v3 \ -  n flask-      app
  ```  
 - Access Application
   ```bash
    minikube service flask-service -n flask-app
   ```
