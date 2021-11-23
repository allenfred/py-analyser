FROM python:3.8-alpine as BUILD

# Copy dependencies/configurations
RUN apk update \
&& apk add bash \
&& mkdir -p /app

RUN apk --no-cache add musl-dev linux-headers g++

WORKDIR /app

COPY . /app/
RUN python -m pip install --trusted-host mirrors.aliyun.com --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install --trusted-host mirrors.aliyun.com -r requirements2.txt -i https://mirrors.aliyun.com/pypi/simple/