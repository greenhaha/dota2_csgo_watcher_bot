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
    dota2_start_time = 0
    dota2_duration = 0
    dota2_game_mode = ''
    dota2_lobby_mode = ''
    dota2_kill = 0
    dota2_death = 0
    dota2_assist = 0
    # 1为天辉, 2为夜魇
    dota2_team = 1
    dota2_win_team = 1
    hero = ''
    last_hit = 0
    damage = 0
    team_damage = 0
    radiant_kill = 0
    dire_kill = 0
    radiant_death = 0
    dire_death = 0

    # CSGO专属
    csgo_kill = 0
    csgo_death = 0
    csgo_assist = 0
    # team分为1和2
    csgo_team = 1
    csgo_win_team = 1
    # 比分
    csgo_team_1_score = 0
    csgo_team_2_score = 0

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
        self.csgo_team = match_info['team']
        self.csgo_win_team = match_info['win_team']
        self.csgo_team_1_score = match_info['score1']
        self.csgo_team_2_score = match_info['score2']

    # dota2数据记录
    def dota2_data_set(self, match_info):
        self.dota2_kill = match_info['kill']
        self.dota2_death = match_info['death']
        self.dota2_assist = match_info['assist']
        self.dota2_team = match_info['team']
        self.dota2_win_team = match_info['win_team']
        self.hero = match_info['hero']
        self.last_hit = match_info['last_hit']
        self.damage = match_info['damage']
        self.team_damage = match_info['team_damage']
        self.radiant_kill = match_info['radiant_kill']
        self.dire_kill = match_info['dire_kill']

    # dota2的一些数据计算
    def get_kda(self):
        return float(self.dota2_kill + self.dota2_assist / (self.dota2_death if self.dota2_death != 0 else 1))

    def get_damage_rate(self):
        return float(self.damage / (self.team_damage if self.team_damage != 0 else 1))

    def get_participation(self):
        # 如果是天辉
        if self.dota2_team == 1:
            team_kill = self.radiant_kill
        # 否则是夜魇
        else:
            team_kill = self.dire_kill
        return float(self.dota2_kill + self.dota2_assist / (team_kill if team_kill != 0 else 1))

    def get_death_rate(self):
        if self.dota2_team == 1:
            team_death = self.radiant_death
        else:
            team_death = self.dire_death
        return float(self.dota2_death / (team_death if team_death != 0 else 1))


PLAYER_LIST = []
