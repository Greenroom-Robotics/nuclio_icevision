FROM nvidia/cuda:11.5.1-cudnn8-devel-ubuntu20.04
LABEL org.opencontainers.image.source=https://github.com/Greenroom-Robotics/nuclio_icevision

ENV DEBIAN_FRONTEND=noninteractive

# Remote nvidia lists as they have a borked GPG
RUN rm /etc/apt/sources.list.d/cuda.list

# Install opencv deps
RUN apt-get update
RUN apt install -y python3-pip wget curl git python3-tk libglib2.0-0
RUN apt-get install -y python-is-python3

# Install icevision
RUN wget https://raw.githubusercontent.com/airctic/icevision/master/icevision_install.sh
RUN bash icevision_install.sh cuda11

COPY ./nuclio_icevision /opt/nuclio

WORKDIR /opt/nuclio

# Run the tests
# Nuclio will overwrite this CMD when it is deployed
CMD pytest . -vv