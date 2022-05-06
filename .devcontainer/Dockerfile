FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

# to avoid selecting timezone on installing packages.
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3 \
    python3-distutils \
    git \
    curl \
    && rm -rf /var/lib/apt/lists

RUN echo "alias python='python3' " >> ~/.bashrc

COPY .devcontainer/scripts/docker-init.sh /usr/local/share

RUN source ~/.bashrc \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

#ENV PATH $PATH:/usr/.poetry/bin
