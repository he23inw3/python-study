FROM python:3
USER root

WORKDIR /app
ADD . /app

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --trusted-host pypi.python.org -r requirements.txt