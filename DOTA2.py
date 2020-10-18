import requests
import json
api_key = "2B469C11A7D6FF2D0E97D2347FA1AF28"


def get_last_match_by_short_steamID(short_steamID):
    # get match_id
    url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key={}' \
          '&account_id={}&matches_requested=1'.format(api_key, short_steamID)
    match_id = json.loads(requests.get(url).content)["result"]["matches"][0]["match_id"]

    # get match detail
    url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/' \
          '?key={}&match_id={}'.format(api_key, match_id)
    match_info = json.loads(requests.get(url).content)["result"]

    return match_info


# 接收某局比赛的玩家列表, 生成开黑战报
# 参数为玩家对象列表
def generate_party_message(player_list):

    pass


# 接收某局比赛的玩家信息, 生成单排战报
# 参数为玩家对象
def generate_solo_message(player_obj):
    pass
