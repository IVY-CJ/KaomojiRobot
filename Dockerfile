FROM python:3.8.5-slim-buster

ARG BOT_DIR=${BOT_DIR:-telegram_bot}
ARG REPO="https://github.com/IVY-CJ/KaomojiRobot.git"
ARG BRANCH=${BRANCH:-master}

ENV BOT_DIR ${BOT_DIR}
ENV REPO=${REPO}
ENV BRANCH=${BRANCH}
ENV BOT_FILE ${BOT_FILE}

RUN apt update && apt install -y git

RUN git clone --branch ${BRANCH} ${REPO} /${BOT_DIR}

RUN pip install -r /${BOT_DIR}/requirements.txt

CMD cd /${BOT_DIR} && git pull && python3 ${BOT_FILE}