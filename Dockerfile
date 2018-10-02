FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir /usr/app
WORKDIR /usr/app
ADD ./requirements.txt /usr/app/
RUN pip install -r requirements.txt
ADD . /usr/app
