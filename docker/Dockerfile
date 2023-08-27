FROM alpine:latest
COPY bot /opt/sdb
RUN apk update && apk add python3 py3-pip && pip install telebot
RUN ln -s /opt/sdb/bot.py /bin/dbot && \
    ln -s /opt/sdb/entrypoint.py /bin/entrypoint
ENTRYPOINT /bin/entrypoint
