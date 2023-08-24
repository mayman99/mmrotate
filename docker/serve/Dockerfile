FROM mmrotate
# add webupd8 repository

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    python3 openjdk-11-jre-headless build-essential

ARG TORCHSERVE="0.4.0"
RUN pip install torchserve==${TORCHSERVE} torch-model-archiver==${TORCHSERVE}

RUN useradd -m model-server \
    && mkdir -p /home/model-server/tmp

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh \
    && chown -R model-server /home/model-server

COPY config.properties /home/model-server/config.properties
RUN mkdir /home/model-server/model-store && chown -R model-server /home/model-server/model-store

EXPOSE 8080 8081 8082

USER model-server
WORKDIR /home/model-server
ENV TEMP=/home/model-server/tmp
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["serve"]
