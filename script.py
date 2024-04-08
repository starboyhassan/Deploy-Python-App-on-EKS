#!/usr/bin/env python3

import os
import subprocess

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
terraform_dir = os.path.join(script_dir, "Terraform")
ansible_dir = os.path.join(script_dir, "Ansible")

def run_terraform():
    os.chdir(terraform_dir)
    print(f"Running Terraform in {terraform_dir}")
    subprocess.run(["terraform", "init"], check=True)
    subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
    print("Terraform execution completed.")

def update_inventory():
    print("Updating Ansible inventory file")
    os.chdir(terraform_dir)
    with open(os.path.join(terraform_dir, "ec2-ip.txt"), "r") as file:
        ip_address = file.read().strip()
    with open(os.path.join(ansible_dir, "inventory.txt"), "w") as file:
        file.write(f"jenkins-ec2 ansible_host={ip_address} ansible_user=ubuntu ansible_ssh_private_key_file=/home/hassan/ec2key.pem\n")
    print("ansible_host is updated in inventory file.")

def clean_ec2_ip():
    with open(os.path.join(terraform_dir, "ec2-ip.txt"), "w") as file:
        file.write("")
    print("EC2 IP cleaned up.")

def run_ansible():
    os.chdir(ansible_dir)
    print(f"Running Ansible playbook in {ansible_dir}")
    subprocess.run(["ansible-playbook", "-i", "inventory", "playbook.yml"], check=True)
    print("Ansible execution completed.")

if __name__ == "__main__":
    run_terraform()
    update_inventory()
    clean_ec2_ip()
    run_ansible()
