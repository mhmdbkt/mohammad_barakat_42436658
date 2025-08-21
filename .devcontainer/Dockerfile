FROM mcr.microsoft.com/devcontainers/universal:2

USER root
RUN apt-get update && apt-get install -y curl gnupg lsb-release ca-certificates

# MongoDB 7.0 (pin to jammy for Codespaces reliability)
RUN curl -fsSL https://pgp.mongodb.com/server-7.0.asc | gpg --dearmor -o /usr/share/keyrings/mongodb-server-7.0.gpg && \
    echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" \
      | tee /etc/apt/sources.list.d/mongodb-org-7.0.list && \
    apt-get update && apt-get install -y mongodb-org && \
    rm -rf /var/lib/apt/lists/*

# Python frameworks
RUN pipx install django && pipx ensurepath
RUN pip install --no-cache-dir flask gunicorn "pymongo[srv]" djongo

# Node LTS
RUN bash -lc "source /usr/local/share/nvm/nvm.sh && nvm install --lts && nvm alias default 'lts/*'"

# Mongo data dir
RUN mkdir -p /workspace/.mongo/data && chown -R vscode:vscode /workspace/.mongo
USER vscode
