import CSGO
import DOTA2
from DBOper import update_CSGO_match_ID, update_DOTA2_match_ID
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
        if match_info == -1:
            continue
        match_id = match_info['matchId']
        if match_id != i.last_CSGO_match_ID:
            # 把最新一局的比赛信息进行更新
            i.csgo_data_set(match_info)
            if result.get(match_id, 0) != 0:
                result[match_id].append(i)
            else:
                result.update({match_id: [i]})
            # 更新数据库的last_CSGO_match_id字段
            update_CSGO_match_ID(i.short_steamID, match_id)

    return result


def update_and_send_message_CSGO():
    # 格式: { match_id1: [player1, player2, player3], match_id2: [player1, player2]}
    result = update_CSGO()
    for match_id in result:
        if len(result[match_id]) > 1:
            CSGO.generate_party_message(player_list=result[match_id])
        elif len(result[match_id]) == 1:
            CSGO.generate_solo_message(player_obj=result[match_id][0])


def update_DOTA2():
    result = {}
    for i in PLAYER_LIST:
        match_id = DOTA2.get_last_match_id_by_short_steamID(i.short_steamID)
        if match_id != i.last_DOTA2_match_ID:
            if result.get(match_id, 0) != 0:
                result[match_id].append(i)
            else:
                result.update({match_id: [i]})
            # 更新数据库的last_DOTA2_match_id字段
            update_DOTA2_match_ID(i.short_steamID, match_id)

    return result


def update_and_send_message_DOTA2():
    # 格式: { match_id1: [player1, player2, player3], match_id2: [player1, player2]}
    result = update_DOTA2()
    for match_id in result:
        if len(result[match_id]) > 1:
            DOTA2.generate_party_message(match_id=match_id, player_list=result[match_id])
        elif len(result[match_id]) == 1:
            DOTA2.generate_solo_message(match_id=match_id, player_obj=result[match_id][0])
