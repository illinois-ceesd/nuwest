# root docker file
FROM quay.io/jupyter/scipy-notebook:lab-4.0.9
LABEL maintainer="Douglas N Friedel <friedel@illinois.edu>"

USER root
RUN apt-get update
RUN apt-get -y install libpocl-dev python3-numpy python3-pyopencl
USER 1000
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD --chown=1000:100 Parsl_tutorial/intro Parsl
ADD --chown=1000:100 mirge/demos Mirge
RUN rm -rf src work requirements.txt
