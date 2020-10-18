import CSGO
import DOTA2
from DBOper import update_CSGO_match_ID
from player import PLAYER_LIST


def steam_id_convert_32_to_64(short_steamID):
    return short_steamID + 76561197960265728


def steam_id_convert_64_to_32(long_steamID):
    return long_steamID - 76561197960265728


# 返回一个最新比赛变化过的字典
# 格式: { match_id1: [player1, player2, player3], match_id2: [player1, player2]}
def update_CSGO():
    result = {}
    for i in PLAYER_LIST:
        match_info = CSGO.get_last_match_by_long_steamID(i.long_steamID)
        match_id = match_info['matchId']
        if match_id != i.last_CSGO_match_ID:
            if result.get(match_id, 0) != 0:
                result[match_id].append(i)
            else:
                result.update({match_id, [i]})
            # 更新数据库的last_CSGO_match_id字段
            update_CSGO_match_ID(i.short_steamID, match_id)

    return result


def update_and_send_message_CSGO():
    # 格式: { match_id1: [player1, player2, player3], match_id2: [player1, player2]}
    result = update_CSGO()
    for match_id, players in result:
        if len(players) > 1:
            CSGO.generate_party_message(player_list=players)
        elif len(players) == 1:
            CSGO.generate_solo_message(player_obj=players[0])


def update_DOTA2():
    result = {}
    for i in PLAYER_LIST:
        match_info = DOTA2.get_last_match_by_short_steamID(i.long_steamID)
        match_id = match_info['matchId']
        if match_id != i.last_CSGO_match_ID:
            if result.get(match_id, 0) != 0:
                result[match_id].append(i)
            else:
                result.update({match_id, [i]})
            # 更新数据库的last_DOTA2_match_id字段
            update_CSGO_match_ID(i.short_steamID, match_id)

    return result


def update_and_send_message_DOTA2():
    # 格式: { match_id1: [player1, player2, player3], match_id2: [player1, player2]}
    result = update_DOTA2()
    for match_id, players in result:
        if len(players) > 1:
            DOTA2.generate_party_message(player_list=players)
        elif len(players) == 1:
            DOTA2.generate_solo_message(player_obj=players[0])

