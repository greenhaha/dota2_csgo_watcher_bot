import sqlite3
from player import player, PLAYER_LIST
conn = sqlite3.connect('playerInfo')
c = conn.cursor()


def init():
    cursor = c.execute("SELECT * from playerInfo")
    for row in cursor:
        player_obj = player()
        player_obj.short_steamID = row[0]
        player_obj.long_steamID = row[1]
        player_obj.nickname = row[2]
        player_obj.CSGO_rank = row[3]
        player_obj.DOTA2_score = row[4]
        player_obj.last_CSGO_match_ID = row[5]
        player_obj.last_DOTA2_match_ID = row[6]
        PLAYER_LIST.append(player_obj)


def update_CSGO_match_ID(short_steamID, last_CSGO_match_ID):
    c.execute("UPDATE playerInfo SET last_CSGO_match_ID={} "
              "WHERE short_steamID={}".format(short_steamID, last_CSGO_match_ID))
    conn.commit()


def update_DOTA2_match_ID(short_steamID, last_DOTA2_match_ID):
    c.execute("UPDATE playerInfo SET last_DOTA2_match_ID={} "
              "WHERE short_steamID={}".format(short_steamID, last_DOTA2_match_ID))
    conn.commit()


def insert_info(short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID):
    c.execute("INSERT INTO playerInfo (short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID) "
              "VALUES ({}, {}, {}, {}, {})"
              .format(short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID))
    conn.commit()


def is_player_stored(short_steamID):
    c.execute("SELECT * FROM playerInfo WHERE short_steamID=={}".format(short_steamID))
    if len(c.fetchall()) == 0:
        return False
    return True

