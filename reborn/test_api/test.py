import d2api

api = d2api.APIWrapper('2179FDF11489B59187A1AD12B4B1E2C9')

# print(api.get_heroes())

match_history = api.get_match_history()

match_history = [api.get_match_details(m['match_id']) for m in match_history['matches']]

i = 0
matches = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
matches_ids = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
for match in match_history:
    print("match {} lobby type is {}".format(i, match['lobby_type']))
    matches[match['lobby_type'] + 1] += 1
    matches_ids[match['lobby_type'] + 1].append(match['match_id'])
    print("match {} has {}leavers".format(match['match_id'], "" if match.has_leavers() else "no "))
    i += 1

i = -1
for match in matches:
    print("type {} has {} matches".format(i, matches[i+1]))
    i+=1

i = -1
for match_list in matches_ids:
    print("type {} has these matches: {}".format(i, match_list))
    i+=1

print(match_history)