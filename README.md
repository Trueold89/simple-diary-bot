# Simple Diary Bot

## Simple diary telegram bot for single user

<img src="https://cloud.orudo.ru/apps/files_sharing/publicpreview/YJn2M7CrWp5gY9Y?file=/&fileId=18725&x=1920&y=1200&a=true&etag=17225f744eabcb82e6e37e3c8cc35f61" width=640>

---

### Features:

#### Creating a schedule from the tty

![](https://cloud.orudo.ru/s/ygGAMZt8Kecmfdz/download?path=&files=)

#### Access by telegram id

![](https://cloud.orudo.ru/s/dgp5HBY9cAEMMrM/download?path=&files=)

#### Dual language support (English, Russian)

![](https://cloud.orudo.ru/s/JTRDGJXtyHgJ4K7/download?path=&files=)

---

### Start with docker:
![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/zgZkksrFnE6Mxok?file=/&fileId=18722&x=1920&y=1200&a=true&etag=7d0b55cda2b2370af3166f3e96683742)

##### Use [Docker Hub Image](https://hub.docker.com/r/trueold89/simple-diary-bot) or:

**Build image:**
 - clone this repo or download "docker-build.tar.gz" from Releases
 - ```cd simple-diary-bot/docker```
 - ```docker build -t your_image_name .```

**Create volume:**

```
docker volume create sdr
```
**Run container:**

```
docker run \
 --name sdr \
 --restart=unless-stopped \
 -v sdr:/etc/dbot \
 -e TOKEN="your_bot_token_here" \
 -e USERS="('userid')" \
 -e LANG="ENG" \
 -it your_image_here
```

**You can give access to multiple users by changing "USERS" line to:**

```
-e USERS="('userid_1','userid_2', etc.)" \
```

**Available languages:**

- English: ```-e LANG="ENG" \```
- Russian: ```-e LANG="RU" \```

---

### Run without docker:
![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/mkAKQtW5NZMZtfa?file=/&fileId=18720&x=1920&y=1200&a=true&etag=0654cb5d47d4351026972ed9c9cec586)

**Install deps:**

- Python3
- Python3-pip

**Install telebot python lib**

```
pip install telebot
```
**Set ENV values:**

```
$ export TOKEN="your_bot_token_here"
$ export USERS="('userid')"
$ export LANG="ENG"
```
*You can also change the default values in the "env.py" file*

**Run:**
- Clone this repo or download "sdr.tar.gz" from Releases
- ```cd simple-diary-bot```
- ```python3 bot.py```

---

### Git repos:
![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/iMGZZNRxFom7Yrq?file=/&fileId=18718&x=1920&y=1200&a=true&etag=47ba7ca5563f2f5cb9db19e27a91e2af)

- **[ORUDO Git (Faster updates)](https://git.orudo.ru/trueold89/simple-diary-bot)**
- **[GitHub](https://github.com/Trueold89/simple-diary-bot)**
- **[GitLab](https://gitlab.com/Trueold89/simple-diary-bot)**

---
