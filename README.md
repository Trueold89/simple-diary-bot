# Simple Diary Bot

## Simple diary telegram bot for single user

### Start with docker:

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

### Run without docker:

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
