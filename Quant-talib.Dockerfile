FROM centos:7

WORKDIR /app

RUN yum -y install sudo wget gcc gcc-c++ kernel-devel automake autoconf libtool make python3 python3-devel
RUN python3 -m pip install --trusted-host mirrors.aliyun.com --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN python3 -m pip install --no-cache-dir \
        numpy==1.19.5 pandas==1.1.5 PyMySQL==1.0.2 \
        SQLAlchemy==1.4.23 \
        tushare==1.2.64 -i https://mirrors.aliyun.com/pypi/simple/

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -xzf ta-lib-0.4.0-src.tar.gz
WORKDIR /app/ta-lib
RUN ./configure --prefix=/usr
RUN make
RUN sudo make install