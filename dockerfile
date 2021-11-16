FROM ubuntu:16.04
LABEL maintainer="ricadevera@live.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cacheCOPY./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip freeze > requirements.txt
COPY . /app
RUN cd /app && python create_tables.py
ENTRYPOINT [ "python" ]
CMD [ "points_api.py" ]
