#FROM ubuntu:latest
FROM ubuntu:latest

RUN apt-get update
RUN apt -y install curl
RUN curl --version
RUN apt install -y python3-pip
RUN apt install -y python3-dev
RUN apt-get install -y libcairo2
RUN apt-get install -y libffi-dev
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y openbabel
RUN pip install Flask



EXPOSE 5000


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP app.py

CMD flask run --host=0.0.0.0