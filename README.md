```
# python-flask-fruits-api

# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install flask
# pip3 install flask-sqlalchemy
# pip3 freeze > requirements.txt

# export FLASK_APP=colorfruits.py 
# export FLASK_ENV=development 

# >>> from colorfruits import db
# >>> db.create_all()
# >>> from colorfruits import Fruitscolor

# sudo docker build -t fruitsapi01 . 

The following example starts a fruitsapp01 container and configures it to always restart unless it is explicitly stopped or Docker is restarted.
$ sudo docker run -d --restart unless-stopped -p 80:80 --name=fruitsapi01 fruitsapi01:latest 

This command changes the restart policy for an already running container named fruitsapi01.
$ docker update --restart unless-stopped fruitsapi01

And this command will ensure all currently running containers will be restarted unless stopped.
$ docker update --restart unless-stopped $(docker ps -q)

```
