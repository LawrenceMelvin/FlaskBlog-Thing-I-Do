**Flask Application**
----------------------

A Blog application where we can post the thing we learn or do in daily basis.
The Blog application is made using flask.

1. Home Page
2. Login/ SignUp Page
3. Post Page
4. Post Update Page

The code is deployed in jenkins via an AWS EC2 instance.

EC2 Instance
------------
The Jenkins is installed in an **AWS EC2** instance. It used a public ip to run the jenkins in port 8080

Pipeline
--------
The pipelines run's automatically when the code is committed in the master branch.

Docker
------
The docker is used to run the application in the EC2 instance. The docker image is created and pushed to the docker hub.