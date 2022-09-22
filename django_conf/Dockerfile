# base image
FROM python:3.10.4

ENV APP_ROOT /srv
ENV CONFIG_ROOT /config

# set work directory
RUN mkdir ${CONFIG_ROOT}
WORKDIR ${APP_ROOT}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ${CONFIG_ROOT}/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

ADD . ${APP_ROOT}