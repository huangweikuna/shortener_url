FROM python:3.9.6-slim
# https://stackoverflow.com/questions/67444811/docker-unable-to-find-a-version-that-satisfies-the-requirement-mysqlclient-2
RUN mkdir /app && set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*
ADD .  /app
WORKDIR /app

RUN pip install -r /app/requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
