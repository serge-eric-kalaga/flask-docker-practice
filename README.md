
# Flask with Docker   🐍 🚢
Run a "Flask" application with "Docker"

## Get Started 🚀  

Clone the project 

~~~bash  
  git clone https://github.com/serge-eric-kalaga/flask-docker-practice.git
~~~

Go to the project directory  

~~~bash  
cd flask-docker-practice
~~~

Create the "Docker" image 

~~~bash  
docker image build -t flask_docker_test .
~~~

Run the container

~~~bash  
docker run -p 5000:5000 -d flask_docker_test 
~~~


Go to browser and enter this link 
~~~bash  
localhost:5000
~~~


To run the project with Docker-Compose
~~~bash 
docker-compose up --build
~~~



 
# Congratulations! 👋  