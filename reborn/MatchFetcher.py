import json
import datetime


class MatchFecther(object):

    def __init__(self, api):
        patch_file = open("patch/patch-epoch.json", "r")
        self.patches = json.load(patch_file)
        self.patches.reverse()
        self.api = api
        self.heroes_count = self._set_heroes_count()

    def _set_heroes_count(self):
        maximum_hero_id = 0
        heroes = self.api.get_heroes()['heroes']
        for hero in heroes:
            if hero['id'] > maximum_hero_id:
                maximum_hero_id = hero['id']
        return maximum_hero_id

    def find_patch_for_match(self, match):
        for patch in self.patches:
            if match['start_time'] > patch['epoch']:
                return patch['name']
        print("Weird. Anomaly found when looking for patch of match {}".format(match['match_id']))
        return "NO_PATCH_FOUND"

    def is_match_valid(self, match, seq_num):
        if match['match_seq_num'] < seq_num:
            # print("Match {} is invalid because it is older than our newest match")
            return False
        if match['lobby_type'] != 0 and match['lobby_type'] != 7 and match['lobby_type'] != 9:
            # print("Match {} is invalid because of its lobby type ({})".format(match['match_id'], match['lobby_type']))
            return False
        if match.has_leavers():
            # print("Match {} is invalid because it has leavers".format(match['match_id']))
            return False
        if match['game_mode'] != 2 and match['game_mode'] != 3 and match['game_mode'] != 4 and match['game_mode'] != 22:
            # print("Match {} is invalid because of its game mode ({})".format(match['match_id'], match['game_mode']))
            return False
        if match['duration'] < 600:
            # print("Match {} is invalid because it lasted less than 10 minutes".format(match['match_id']))
            return False
        # print("Match {} has no problems and is considered valid. ----->VALID<-----".format(match['match_id']))
        return True

    def fetch_match(self, match_id):
        match = self.api.get_match_details(match_id)
        if self.is_match_valid(match, match['match_seq_num']):
            radiant_heroes = [int(player['hero']['hero_id']) for player in match['players_minimal'] if player['side'] == "radiant"]
            radiant_heroes.sort()
            dire_heroes = [int(player['hero']['hero_id']) for player in match['players_minimal'] if player['side'] == "dire"]
            dire_heroes.sort()
            return {
                'radiant_heroes': radiant_heroes,
                'dire_heroes': dire_heroes,
                'winning_team': match['winner'],
            }
        else:
            return False

    def get_heroes_count(self):
        return self.heroes_count
