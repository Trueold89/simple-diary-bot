FROM alpine:latest
COPY bot /bot
RUN apk update && apk add python3 py3-pip && pip install telebot
ENTRYPOINT [ "/bot/bot.py" ]
