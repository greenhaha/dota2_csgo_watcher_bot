import requests
import hashlib
import json


def get_last_match_by_long_steamID(long_steamID):
    url = 'https://api.wmpvp.com/api/v2/home/validUser?sign='
    header = {
        "Host": "api.wmpvp.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://news.wmpvp.com",
        "x-requested-with": "XMLHttpRequest",
        "User-Agent": 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G9750 Build/LMY49I; wv) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 EsportsApp Version=1.4.3.43',
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "https://news.wmpvp.com/csgo-matchList.html?id=" + str(long_steamID) + "&type=00",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,en-US;q=0.8",
    }
    salt = '1f3192e58723aed15b8e8a9dc8e760861f3192e58723aed15b8e8a9dc8e76086'
    payload = '{"gameAbbr":"CSGO","steamId":"' + str(long_steamID) + \
              '","accessToken":null,"lastTimeStamp":"","dataSource":0,"pageSize":1} '
    sign = hashlib.md5((payload + salt).encode("utf-8")).hexdigest()
    r = json.loads(requests.post(url + sign, data=payload, headers=header).content)
    if r['statusCode'] == 0:
        match_info = r['data'][2]['data'][0]
        return match_info
    else:
        return "ERROR"


# 接收某局比赛的玩家列表, 生成开黑战报
# 参数为玩家对象列表
def generate_party_message(player_list):

    pass


# 接收某局比赛的玩家信息, 生成单排战报
# 参数为玩家对象
def generate_solo_message(player_obj):
    pass
