## Here is a example of tasks to generate and visualisate random data  
- The gen folder contains a real-time random data generator  
- The visual folder contains a real-time price visualization web service  

### How to use it simple with Docker:  
- go to folder contain Dockerfile  
- build Docker image  
`docker build --pull --rm -f "Dockerfile" -t vdservices:latest "."`  
- run Docker image interactive (-it) or as daemon (-d)
`docker run --rm -it --network="host" -p 5000:5000/tcp -p 8050:8050/tcp vdservices:latest`  
- open in web-browser URL 127.0.0.1:8050 for test visualisation  
- open in web-browser URL 127.0.0.1:5000 for test generator 

### You can use it whithout Docker in Linux
- go to folder contain file requirements.txt  
- install all requirements  
`pip install -r requirements.txt`
- run in bash  
`start_host.sh` 
- open in web-browser URL 127.0.0.1:8050 for test visualisation  
- open in web-browser URL 127.0.0.1:5000 for test generator 
