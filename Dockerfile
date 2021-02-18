FROM python:3.8.5-slim-buster

ARG BRANCH=${BRANCH:-master}
ARG BOT_DIR='/${BOT_DIR:-telegram_bot}'
ENV BOT_DIR ${BOT_DIR}
ENV BOT_FILE ${BOT_FILE}

RUN apt update && apt install -y git

RUN git clone -b ${BRANCH} ${BOT_DIR}/

RUN pip install -r ${BOT_DIR}/requirements.txt

CMD cd ${BOT_DIR} && git pull && python3 ${BOT_FILE}