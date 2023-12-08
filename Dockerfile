# root docker file
FROM quay.io/jupyter/scipy-notebook:lab-4.0.9
LABEL maintainer="Douglas N Friedel <friedel@illinois.edu>"

USER root
RUN mamba install -y -p /opt/conda -c conda-forge numpy pocl pyopencl islpy pip
USER 1000
COPY mirge/requirements-docker.txt m-requirements.txt
RUN pip install -r m-requirements.txt
COPY Parsl_tutorial/requirements.txt p-requirements.txt
RUN pip install -r p-requirements.txt
ADD --chown=1000:100 Parsl_tutorial/intro Parsl
ADD --chown=1000:100 mirge/demos Mirge
RUN rm -rf src work m-requirements.txt p-requirements.txt
