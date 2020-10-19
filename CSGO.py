import requests
import hashlib
import json
import random
from CSGO_dicts import *
import message_sender


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
        match_info = r['data']
        if len(match_info) < 3:
            return -1
        return match_info[2]['data'][0]
    else:
        return -1


# 接收某局比赛的玩家列表, 生成开黑战报
# 参数为玩家对象列表
def generate_party_message(player_list):
    player_num = len(player_list)

    # 队伍信息
    team = player_list[0].csgo_team
    win_team = player_list[0].csgo_win_team
    if win_team == team:
        win = True
    else:
        win = False

    nicknames = ''
    if player_num >= 3:
        for i in range(player_num - 1):
            nicknames += player_list[i].nickname
            nicknames += ', '
    else:
        nicknames += player_list[0].nickname

    nicknames += '和'
    nicknames += player_list[player_num - 1].nickname

    top_rating = 0
    for i in player_list:
        if i.rating > top_rating:
            top_rating = i.rating

    if (win and top_rating > 1) or (not win and top_rating > 1):
        postive = True
    elif (win and top_rating < 0.5) or (not win and top_rating < 0.5):
        postive = False
    else:
        if random.randint(0, 1) == 0:
            postive = True
        else:
            postive = False

    print_str = ''
    if win and postive:
        print_str += random.choice(WIN_POSTIVE_PARTY).format(nicknames) + '\n'
    elif win and not postive:
        print_str += random.choice(WIN_NEGATIVE_PARTY).format(nicknames) + '\n'
    elif not win and postive:
        print_str += random.choice(LOSE_POSTIVE_PARTY).format(nicknames) + '\n'
    else:
        print_str += random.choice(LOSE_NEGATIVE_PARTY).format(nicknames) + '\n'

    start_time = player_list[0].csgo_start_time
    score1 = player_list[0].csgo_team_1_score
    score2 = player_list[0].csgo_team_2_score
    print_str += "开始时间: {}\n".format(start_time)
    print_str += "比分: [{}/{}]\n".format(score1, score2 if team == 1 else score2, score1)

    print_str += '游戏模式: [{}/{}]\n'.format(player_list[0].csgo_map, player_list[0].csgo_mode)

    for i in player_list:
        nickname = i.nickname
        rating = i.csgo_rating
        kills, deaths, assists = i.csgo_kill, i.csgo_death, i.csgo_assist

        print_str += "{}KDA: [{}/{}/{}], rating: {}\n" \
            .format(nickname, kills, deaths, assists, rating)
    # print(print_str)
    message_sender.message(print_str)


# 接收某局比赛的玩家信息, 生成单排战报
# 参数为玩家对象
def generate_solo_message(player_obj):
    # 队伍信息
    team = player_obj.csgo_team
    win_team = player_obj.csgo_win_team
    if win_team == team:
        win = True
    else:
        win = False

    nicknames = player_obj.nickname

    if (win and player_obj.csgo_rating > 1) or (not win and player_obj.csgo_rating > 1):
        postive = True
    elif (win and player_obj.csgo_rating < 0.5) or (not win and player_obj.csgo_rating < 0.5):
        postive = False
    else:
        if random.randint(0, 1) == 0:
            postive = True
        else:
            postive = False

    print_str = ''
    if win and postive:
        print_str += random.choice(WIN_POSTIVE_PARTY).format(nicknames) + '\n'
    elif win and not postive:
        print_str += random.choice(WIN_NEGATIVE_PARTY).format(nicknames) + '\n'
    elif not win and postive:
        print_str += random.choice(LOSE_POSTIVE_PARTY).format(nicknames) + '\n'
    else:
        print_str += random.choice(LOSE_NEGATIVE_PARTY).format(nicknames) + '\n'

    start_time = player_obj.csgo_start_time
    if team == 1:
        score1 = player_obj.csgo_team_1_score
        score2 = player_obj.csgo_team_2_score
    else:
        score1 = player_obj.csgo_team_2_score
        score2 = player_obj.csgo_team_1_score
    print_str += "开始时间: {}\n".format(start_time)
    print_str += "比分: [{}:{}]\n".format(score1, score2)

    print_str += '游戏模式: [{}/{}]\n'.format(player_obj.csgo_map, player_obj.csgo_mode)

    print_str += "{}KDA: [{}/{}/{}], rating: {}\n"\
        .format(player_obj.nickname, player_obj.csgo_kill,
                player_obj.csgo_death, player_obj.csgo_assist, player_obj.csgo_rating)

    # print(print_str)
    message_sender.message(print_str)