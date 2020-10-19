#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, json
url = "http://127.0.0.1:8080"
# 群号
target = 1111111111
# bot的QQ号
bot_qq = 1111111111


def message(m):
    # Authorize
    auth_key = {"authKey": "xxxxxxxxx"}
    r = requests.post(url + "/auth", json.dumps(auth_key))
    if json.loads(r.text).get('code') != 0:
        print("ERROR@auth")
        print(r.text)
        exit(1)
    # Verify
    session_key = json.loads(r.text).get('session')
    session = {"sessionKey": session_key, "qq": bot_qq}
    r = requests.post(url + "/verify", json.dumps(session))
    if json.loads(r.text).get('code') != 0:
        print("ERROR@verify")
        print(r.text)
        exit(2)
    data = {
            "sessionKey": session_key,
            "target": target,
            "messageChain": [
                {"type": "Plain", "text": m}
            ]
        }
    r = requests.post(url + "/sendGroupMessage", json.dumps(data))
    # release
    data = {
            "sessionKey": session_key,
            "qq": bot_qq
        }
    r = requests.post(url + "/release", json.dumps(data))
    print(r.text)
