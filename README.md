# Deploy Python app with MySQL db on AWS EKS Cluster

## Overview
The project is a DevOps project aimed at automating the deployment pipeline for a Python application backed by a MySQL database on AWS infrastructure. The process involves using Terraform for infrastructure provisioning, Ansible for configuration management, and Jenkins for CI/CD automation. The project leverages AWS services such as VPC, EC2, ECR, and EKS (Elastic Kubernetes Service) for hosting the application and its dependencies.

![](https://github.com/starboyhassan/Deploy-Python-App-on-EKS/blob/main/digram/python-app-digram.png)

## Tools

- **GitHub**: Hosts the repositories containing application code .
- **Terraform**: Used for provisioning AWS infrastructure components like VPC, EC2 instances, ECR repositories, and EKS clusters.
- **Ansible**: Utilized for installing and configuring Jenkins, Docker, AWS CLI, and kubectl on the EC2.
- **Jenkins**:Used for orchestrating the CI/CD pipeline. It triggers builds upon code commits to the GitHub repository, builds Docker images, pushes them to ECR, updates Kubernetes deployment manifests, and deploys the application to EKS.
- **Docker**: Utilized for containerizing the Python Flask application and the MySQL database.
- **AWS CLI**: Used for interacting with AWS services programmatically.
- **kubectl**: Command-line tool for interacting with Kubernetes clusters.
- **AWS ECR**: Used as the Docker image registry to store built images.
- **AWS EKS**: Used for Kubernate Cluster.
- **Slack**: Used for receiving notifications on pipeline success or failure.
---
## Project Structure

**The project repository contains the following components:**

- **Docker**: Contains Dockerfiles for building Docker images for the Python Flask application and MySQL database.
- **K8S**: Contains Kubernetes manifests for deploying the application and its associated resources (e.g., deployment, deployment service, ingress, persistent volume, persistent volume claims, Configmap, Secrets, Statefulset, and Statefulsetservice ).
- **Terraform**: Contains Terraform modules for provisioning AWS infrastructure components VPC, EC2, ECR, and EKS.
- **Ansible**: Contains playbook for installing and configuring Jenkins, Docker, AWS CLI, and kubectl on the EC2 instance.
- **Jenkinsfile**: Contains the CI/CD pipeline definition for Jenkins.
- **Python script**: Initiates the deployment process, triggering Terraform for infrastructure provisioning, updating Ansible inventory, and executing Ansible playbooks.

## Step-by-Step 

### 1. Infrastructure Provisioning: The Python script triggers Terraform to provision the necessary AWS infrastructure, including VPC, EC2 instances, ECR repositories, and EKS clusters.

### 2. Ansible Configuration: The script then updates the Ansible inventory file with the EC2 instance's IP address and executes Ansible playbooks to install and configure Jenkins, Docker, AWS CLI, and kubectl on the EC2 instance.

### 3. Jenkins Pipeline:
* ####  Developer commits code to the GitHub repository.
* #### GitHub webhook triggers the Jenkins pipeline.
* #### First: CI
    1) Checks out the repository.
    2) Builds Docker images for the application and database.
    3) Pushes the Docker images to ECR.
    4) Updates the image tags in Kubernetes deployment manifests.
* #### Second: CD
    1) Deploys the updated application to EKS using kubectl apply.
    2) Retrieves the website URL using kubectl.
    3) Sends a notification to Slack indicating success or failure of the deployment.


----
## Conclusion

#### This DevOps project provides a streamlined and automated approach to deploying a Python application with a MySQL database on AWS infrastructure. By leveraging Terraform for infrastructure provisioning, Ansible for configuration management, and Jenkins for CI/CD automation, the project ensures consistency, scalability, and reliability in the deployment process. With this setup, developers can focus on writing code, while the automated pipeline takes care of building, testing, and deploying the application with minimal manual intervention.




