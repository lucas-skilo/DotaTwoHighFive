import d2api

api = d2api.APIWrapper('2179FDF11489B59187A1AD12B4B1E2C9')

match_history = api.get_match_history()

i = 0
matches = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
for match in match_history['matches']:
    print("match {} lobby type is {}".format(i, match['lobby_type']))
    matches[match['lobby_type'] + 1] += 1
    i += 1

i = -1
for match in matches:
    print("type {} has {} matches".format(i, matches[i+1]))
    i+=1

# print(match_history)