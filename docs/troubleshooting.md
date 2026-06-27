- Minikube Does Not Start
  
  * Error:
  Exiting due to DRIVER_NOT_FOUND.
  * Cause:
  Docker Desktop is not running.
  Minikube driver is not configured.
  * debug:
    ```bash
    minikube start --driver=docker
    ```
- Pods in Pending State
  
  * Cause:
    Insufficient CPU or memory.
    Node scheduling issue.
  * debug:
    ```bash
    kubectl describe pod flask-deployment-74c49c48d6-c9g87 -n flask-app
    ```
- CrashLoopBackOff
  
  * Cause:
    Missing environment variables.
    Missing dependencies.
  * Solution:
    ```bash
    kubectl logs flask-deployment-74c49c48d6-c9g87 -n flask-app
     ```
- ImagePullBackOff
  
  * Cause:
    Docker image not pushed.
    Incorrect image name.
    Wrong image tag.
  * debug:
    ```bash
    kubectl describe pod flask-deployment-74c49c48d6-c9g87 -n flask-app
    ```
- Service Not Accessible
  
  * debug:
    ```bash
    Verify Service
    kubectl get endpoints
    ```
