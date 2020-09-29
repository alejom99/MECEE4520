FROM python:3.7.2-slim-stretch
#MAINTAINER rhoai

#ENV DEBIAN_FRONTEND noninteractive



# Install core libraries
RUN apt-get update \
  && apt-get install -y git

RUN mkdir /MECEE4520 && git clone https://github.com/alejom99/MECEE4520.git /MECEE4520
RUN apt-get install -y gcc
RUN cd /MECEE4520/lecture_4 && pip install -r requirements.txt
WORKDIR /MECEE4520
#CMD ["jupyter notebook --notebook-dir=/tmp/MECEE4520"]