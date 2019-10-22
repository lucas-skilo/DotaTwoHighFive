import d2api
import json
import datetime


class MatchFecther(object):

    def __init__(self):
        patch_file = open("patch/patch-epoch.json", "r")
        self.patches = json.load(patch_file)
        self.patches.reverse()
        self.api = d2api.APIWrapper('2179FDF11489B59187A1AD12B4B1E2C9')

    def find_patch_for_match(self, match):
        for patch in self.patches:
            if match['start_time'] > patch['epoch']:
                return patch['name']
        print("Weird. Anomaly found when looking for patch of match {}".format(match['match_id']))
        return "NO_PATCH_FOUND"

    def validate_match(self, match, seq_num):
        if match['match_seq_num'] < seq_num:
            print("Match {} is invalid because it is older than our newest match")
            return False
        if match['lobby_type'] != 0 and match['lobby_type'] != 7 and match['lobby_type'] != 9:
            print("Match {} is invalid because of its lobby type ({})".format(match['match_id'], match['lobby_type']))
            return False
        if match.has_leavers():
            print("Match {} is invalid because it has leavers".format(match['match_id']))
            return False
        if match['game_mode'] != 2 and match['game_mode'] != 3 and match['game_mode'] != 4 and match['game_mode'] != 22:
            print("Match {} is invalid because of its game mode ({})".format(match['match_id'], match['game_mode']))
            return False
        if match['duration'] < 600:
            print("Match {} is invalid because it lasted less than 10 minutes".format(match['match_id']))
            return False
        print("Match {} has no problems and is considered valid. ----->VALID<-----".format(match['match_id']))
        return True

    def do_things(self):
        first_match_seq_num = 4031929837
        seq_num = first_match_seq_num
        batches = 0
        while True:
            print("starting batch {} now...".format(batches))
            match_history = self.api.get_match_history_by_sequence_num(start_at_match_seq_num=seq_num)

            # matches_detailed = []
            for match in match_history['matches']:
                match_detailed = self.api.get_match_details(match['match_id'])
                self.validate_match(match_detailed, seq_num)
                # patch = find_patch_for_match(match_detailed)
                seq_num = match_detailed['match_seq_num']
            batches += 1

MatchFecther().do_things()
