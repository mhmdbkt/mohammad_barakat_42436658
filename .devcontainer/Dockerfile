FROM mcr.microsoft.com/devcontainers/universal:2


USER root
RUN apt-get update && apt-get install -y python3-pip

# Install frameworks
RUN pip3 install --no-cache-dir django flask

# Ensure Node LTS is ready (already present in base image, just set default)
RUN bash -lc "source /usr/local/share/nvm/nvm.sh && nvm install --lts && nvm alias default 'lts/*'"

USER vscode
