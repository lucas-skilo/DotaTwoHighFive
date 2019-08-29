import d2api
import datetime

api = d2api.APIWrapper('2179FDF11489B59187A1AD12B4B1E2C9')

match_hitory = api.get_match_history()

start_time = datetime.datetime.now()
matches_detailed = [api.get_match_details(match['match_id']) for match in match_hitory['matches']]
end_time = datetime.datetime.now()
print("Elapsed time: {}".format(end_time - start_time))

