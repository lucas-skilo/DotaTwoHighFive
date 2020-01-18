import d2api
from MatchFetcher import MatchFecther
from FileGenerator import FileGenerator

api = d2api.APIWrapper('2179FDF11489B59187A1AD12B4B1E2C9')
fetcher = MatchFecther(api)

first_match_seq_num = 4031929837
heroes_count = fetcher.get_heroes_count()

seq_num = first_match_seq_num
batches = 0

FileGenerator(heroes_count).generate_all()
while True:
    print("starting batch {} now...".format(batches))
    match_history = api.get_match_history_by_sequence_num(start_at_match_seq_num=seq_num)

    for match in match_history['matches']:
        match_treated = fetcher.fetch_match(match['match_id'])
        if match_treated:
            print("Treated a match: {}".format(match_treated))
        seq_num = match['match_seq_num']
    batches += 1
