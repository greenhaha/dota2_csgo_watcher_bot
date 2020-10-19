#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from common import update_and_send_message_CSGO, update_and_send_message_DOTA2, steam_id_convert_32_to_64
import json
from player import PLAYER_LIST, player
from DBOper import is_player_stored, insert_info, update_CSGO_match_ID, update_DOTA2_match_ID
import CSGO
import DOTA2


def init():
    for nickname, short_steamID in json.load(open("list.json", encoding="utf-8")).items():

        long_steamID = steam_id_convert_32_to_64(short_steamID)
        last_CSGO_match_info = CSGO.get_last_match_by_long_steamID(long_steamID)
        if last_CSGO_match_info != -1:
            last_CSGO_match_ID = last_CSGO_match_info["matchId"]
        else:
            last_CSGO_match_ID = "-1"

        last_DOTA2_match_ID = DOTA2.get_last_match_id_by_short_steamID(short_steamID)

        # 如果数据库中没有这个人的信息, 则进行数据库插入
        if not is_player_stored(short_steamID):
            # 插入数据库
            insert_info(short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID)
        # 如果有这个人的信息则更新其最新的比赛信息
        else:
            update_CSGO_match_ID(short_steamID, last_CSGO_match_ID)
            update_DOTA2_match_ID(short_steamID, last_DOTA2_match_ID)
        # 新建一个玩家对象, 放入玩家列表
        temp_player = player(short_steamID=short_steamID,
                             long_steamID=long_steamID,
                             nickname=nickname,
                             last_CSGO_match_ID=last_CSGO_match_ID,
                             last_DOTA2_match_ID=last_DOTA2_match_ID)

        if last_CSGO_match_info != -1:
            temp_player.csgo_data_set(last_CSGO_match_info)

        PLAYER_LIST.append(temp_player)


def update():
    update_and_send_message_CSGO()
    update_and_send_message_DOTA2()
    time.sleep(10 * 60)


def main():
    init()
    while True:
        update()


if __name__ == '__main__':
    main()
