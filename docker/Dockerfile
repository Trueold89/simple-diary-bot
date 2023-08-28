FROM alpine:latest
COPY bot /opt/sdb
RUN apk update && apk add python3 py3-pip && pip install telebot
ENTRYPOINT /opt/sdb/bot.py
