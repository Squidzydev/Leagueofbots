import cassiopeia as cass
class infoSummoner:
    def infoaboutsummoner(self, name, key):
        cass.set_riot_api_key(key)
        summoner = cass.get_summoner(region='RU', name=name)
        self.lvl = str(summoner.level)
        self.rank = str(summoner.league_entries[0].tier) + ' '+str(summoner.league_entries[0].division)
        self.mainer = str(summoner.champion_masteries[0].champion.name)

