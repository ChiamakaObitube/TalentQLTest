# Technical Assessment for Devops Engineer
* This repository is in fulfillment of the technical assessement test for the DevOps Engineer role at TalentQL
## Task 1 : Write a python script, which will convert json files to xml files, encrypt and transfer it in a remote location.
* The directory for the first task is contained in the jsontoxml directory.
* CD into the jsontoxml directory.
* Run ```docker-compose build ``` to build the containers
* Run ```docker-compose up``` to run the container.

## Task 2: This task uses ansible to automate the deployment of apache server on an EC2 instance.

To run this, take the following steps:
* clone the repository and cd into ubiquitous-bassoon directory 
* Ensure that ansible is installed on the local server 
* Run ```ansible-playbook launch.yml -i hosts --vault-password-file vault-password.txt```

## Continuous integration with Travis CI