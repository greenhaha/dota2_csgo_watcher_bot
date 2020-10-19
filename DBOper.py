#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
from player import player, PLAYER_LIST
conn = sqlite3.connect('playerInfo')
c = conn.cursor()


def init():
    cursor = c.execute("SELECT * from playerInfo")
    for row in cursor:
        player_obj = player(short_steamID=row[0],
                            long_steamID=row[1],
                            nickname=row[2],
                            last_CSGO_match_ID=row[5],
                            last_DOTA2_match_ID=row[6])
        player_obj.CSGO_rank = row[3]
        player_obj.DOTA2_score = row[4]
        PLAYER_LIST.append(player_obj)


def update_CSGO_match_ID(short_steamID, last_CSGO_match_ID):
    c.execute("UPDATE playerInfo SET last_CSGO_match_ID='{}' "
              "WHERE short_steamID={}".format(last_CSGO_match_ID, short_steamID))
    conn.commit()


def update_DOTA2_match_ID(short_steamID, last_DOTA2_match_ID):
    c.execute("UPDATE playerInfo SET last_DOTA2_match_ID='{}' "
              "WHERE short_steamID={}".format(short_steamID, last_DOTA2_match_ID))
    conn.commit()


def insert_info(short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID):
    c.execute("INSERT INTO playerInfo (short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID) "
              "VALUES ({}, {}, '{}', '{}', '{}')"
              .format(short_steamID, long_steamID, nickname, last_CSGO_match_ID, last_DOTA2_match_ID))
    conn.commit()


def is_player_stored(short_steamID):
    c.execute("SELECT * FROM playerInfo WHERE short_steamID=={}".format(short_steamID))
    if len(c.fetchall()) == 0:
        return False
    return True

