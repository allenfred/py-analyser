FROM python:3.8-alpine as BUILD

# Copy dependencies/configurations
RUN apk update \
&& apk add bash gcc \
&& mkdir -p /app

RUN apk --no-cache add musl-dev linux-headers g++

WORKDIR /app

COPY . /app/

RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.8/site-packages

RUN python -m pip install --trusted-host mirrors.aliyun.com --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install --trusted-host mirrors.aliyun.com pandas PyMySQL SQLAlchemy TA-Lib tushare -i https://mirrors.aliyun.com/pypi/simple/