# Technical Assessment for Devops Engineer

## Task 1

1. Write a python script, which will convert json files to xml files, encrypt and transfer it in a remote location.

## Task 2
1. Deploy apache on a cloud instance of your choice, verify you can access a working instance and tear down the entire infrastructure

# This tasks uses ansible to automate the deployment of apache server on an EC2 instance.
* 

* To run this, take the following steps:
* clone the repository and cd into ubiquitous-bassoon directory 
* Ensure that ansible is installed on the local server 
* Run ```ansible-playbook -i hosts --ask-vault-pass launch.yml```