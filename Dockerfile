# Use below python base docker image
FROM python:3.10-slim-bullseye

WORKDIR /webapp

# Install pip requirements
COPY requirements.txt requirements.txt
RUN pip3 install flask 
RUN pip3 install -r requirements.txt


COPY webapp /webapp 


CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
