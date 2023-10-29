FROM python:3.11


WORKDIR /usr/src/crypto_hub
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ./start.sh