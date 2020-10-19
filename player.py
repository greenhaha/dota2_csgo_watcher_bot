#!/usr/bin/python
# -*- coding: UTF-8 -*-
class player:
    # 基本属性
    short_steamID = 0
    long_steamID = 0
    nickname = ''
    CSGO_rank = ''
    DOTA2_score = ''
    last_CSGO_match_ID = 0
    last_DOTA2_match_ID = 0

    # 玩家在最新的一场比赛中的数据
    # dota2专属
    dota2_kill = 0
    dota2_death = 0
    dota2_assist = 0
    # 1为天辉, 2为夜魇
    dota2_team = 1
    gpm = 0
    xpm = 0
    hero = ''
    last_hit = 0
    damage = 0

    # CSGO专属
    csgo_kill = 0
    csgo_death = 0
    csgo_assist = 0
    csgo_rating = 0
    # team分为1和2
    csgo_team = 1
    csgo_win_team = 1
    # 比分
    csgo_team_1_score = 0
    csgo_team_2_score = 0
    # 地图和模式
    csgo_map = ''
    csgo_mode = ''
    # 时间
    csgo_start_time = ''

    def __init__(self, nickname, short_steamID, long_steamID, last_CSGO_match_ID, last_DOTA2_match_ID):
        self.nickname = nickname
        self.short_steamID = short_steamID
        self.long_steamID = long_steamID
        self.last_DOTA2_match_ID = last_DOTA2_match_ID
        self.last_CSGO_match_ID = last_CSGO_match_ID

    # csgo的数据记录
    def csgo_data_set(self, match_info):
        self.csgo_kill = match_info['kill']
        self.csgo_death = match_info['death']
        self.csgo_assist = match_info['assist']
        self.csgo_rating = match_info['rating']
        self.csgo_team = match_info['team']
        self.csgo_win_team = match_info['winTeam']
        self.csgo_team_1_score = match_info['score1']
        self.csgo_team_2_score = match_info['score2']
        self.csgo_map = match_info['mapName']
        self.csgo_mode = match_info['mode']
        self.csgo_start_time = match_info['startTime']


PLAYER_LIST = []
