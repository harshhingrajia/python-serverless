#Steps to launch

1. Install Minikube, Docker, Kubectl, Kubeless
2. Start Minikube
   `minikube start --driver=docker`
3. Check IP address for Minikube
   `minikube ip`
4. Create a Kubeless namespace for kubectl
   `kubectl create ns kubeless`
  * With RABC enabled
   ```kubectl
   kubectl create -f https://github.com/kubeless/kubeless/releases/download/{VERSION}/kubeless-{VERSION}.yaml
   ````
5. Deploy Kubeless function for list.py and delete.py
 * a. for list.py
   ``` kubeless
   kubeless function deploy cognito-list --runtime python3.6 --from-file lambda/list.py --handler list.list -d requirement.txt
   ```
 * b. for delete.py
   ``` kubeless
   kubeless function deploy cognito-delete --runtime python3.6 --from-file lambda/delete.py --handler delete.delete -d requirement.txt
   ```
6. Check the pods are running
   `kubectl get pods`
7. Check the Services
   `kubectl get svc`
8. Apply Ingress file
   `kubectl apply -f kubeless-list.yaml`
9. Check the host name in Ingress
   `kubectl get ing`
10. Open postman and run the hostname {hostname/list for list users and hostname/delete for delete users}
11. Select Body -> raw -> JSON(application/json)
12. For List Users {hostname/list}
    ```json
    {
    "SECRET_KEY" : "...",
    "ACCESS_KEY" : "...",
    "REGION" : "...",
    "USER_POOL_ID" : "..."
    }
    ```
13. For Delete Users {hostname/delete}
    ```json
    {
    "SECRET_KEY" : "...",
    "ACCESS_KEY" : "...",
    "REGION" : "...",
    "USER_POOL_ID" : "...",
    "Users" :[
       {
       ....
       ....
       "Username" : "....."
      },
      {
       ....
       ....
       "Username" : "....."
      }
     ]
    }
    ```
