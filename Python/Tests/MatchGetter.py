import dota2api
import numpy as np
from enumerator import enumerate

# Initialise the API module
api = dota2api.Initialise("2179FDF11489B59187A1AD12B4B1E2C9", raw_mode=True)

total_matches = int(open("total.txt", "r").readline())

how_much_more_str = input()

if how_much_more_str == "":
	wanted_matches = total_matches + 500
else:
	wanted_matches = total_matches + int(how_much_more_str)

print("Wanted matches: " + str(wanted_matches))

# How many heroes?
T = 114

# How numbers are going to be stored?
dt = np.dtype(np.int32)
dtsize = dt.itemsize

while (total_matches < wanted_matches):
	# Read the last parsed match number
	oldnum = int(open("newnum.txt", "r").readline())

	# Get new matchlist beginning at last parsed match number
	match_list = api.get_match_history_by_seq_num(oldnum)
	newnum = oldnum
	matches = match_list.get("matches")

	if (len(matches) > 10):
		for match in matches:
			valid = True
			match_seq_num = match.get("match_seq_num")

			# If this match is older than the oldest parsed match, ignore it
			if(match_seq_num <= oldnum):
				valid = False
				continue

			# Check if it is a valid lobby type
			lobby_type = match.get("lobby_type")
			if (lobby_type == 0) or (lobby_type == 7):
				for player in match.get("players"):
					leaver_status = player.get("leaver_status")
					# Check for players' leaver status
					if (leaver_status != 0) and (leaver_status != 1):
						valid = False
						break
			else:
				valid = False
				
			if valid:
				if (match_seq_num > newnum):
					newnum = match_seq_num

				radiant_ids = np.array([], dtype=dt)
				dire_ids = np.array([], dtype=dt)

				for player in match.get("players"):
					if (player.get("player_slot") < 128):
						radiant_ids = np.append(radiant_ids, int(player.get("hero_id")))
					else:
						dire_ids = np.append(dire_ids, int(player.get("hero_id")))

				radiant_ids = np.sort(radiant_ids)
				dire_ids = np.sort(dire_ids)
				radiant_win = match.get("radiant_win")

				# Single Heroes:
				with open("1.wr", "rb+") as wrfile:
					for id1 in range(0, 5):
						position = enumerate(h5=radiant_ids[id1], T=T)
						if radiant_win:
							wrfile.seek(position*2*dtsize)
							wins = np.fromfile(wrfile, dtype=dt, count=1)
							wins += 1
							wrfile.seek(-dtsize, 1)
							wrfile.write(np.array(wins).tobytes())
						wrfile.seek((position*2*dtsize)+dtsize)
						total = np.fromfile(wrfile, dtype=dt, count=1)
						total +=1
						wrfile.seek(-dtsize, 1)
						wrfile.write(np.array(total).tobytes())
					for id1 in range(0, 5):
						position = enumerate(h5=dire_ids[id1], T=T)
						if not radiant_win:
							wrfile.seek(position*2*dtsize)
							wins = np.fromfile(wrfile, dtype=dt, count=1)
							wins += 1
							wrfile.seek(-dtsize, 1)
							wrfile.write(np.array(wins).tobytes())
						wrfile.seek((position*2*dtsize)+dtsize)
						total = np.fromfile(wrfile, dtype=dt, count=1)
						total +=1
						wrfile.seek(-dtsize, 1)
						wrfile.write(np.array(total).tobytes())
					
				# Dual Heroes
				with open("2.wr", "rb+") as wrfile:
					for id1 in range(0, 4):
						for id2 in range(id1+1, 5):
							position = enumerate(h4=radiant_ids[id1], h5=radiant_ids[id2], T=T)
							if radiant_win:
								wrfile.seek(position*2*dtsize)
								wins = np.fromfile(wrfile, dtype=dt, count=1)
								wins += 1
								wrfile.seek(-dtsize, 1)
								wrfile.write(np.array(wins).tobytes())
							wrfile.seek((position*2*dtsize)+dtsize)
							total = np.fromfile(wrfile, dtype=dt, count=1)
							total += 1
							wrfile.seek(-dtsize, 1)
							wrfile.write(np.array(total).tobytes())
					for id1 in range(0, 4):
						for id2 in range(id1+1, 5):
							position = enumerate(h4=dire_ids[id1], h5=dire_ids[id2], T=T)
							if not radiant_win:
								wrfile.seek(position*2*dtsize)
								wins = np.fromfile(wrfile, dtype=dt, count=1)
								wins += 1
								wrfile.seek(-dtsize, 1)
								wrfile.write(np.array(wins).tobytes())
							wrfile.seek((position*2*dtsize)+dtsize)
							total = np.fromfile(wrfile, dtype=dt, count=1)
							total += 1
							wrfile.seek(-dtsize, 1)
							wrfile.write(np.array(total).tobytes())

				# Tri Heroes
				with open("3.wr", "rb+") as wrfile:
					for id1 in range(0, 3):
						for id2 in range(id1+1, 4):
							for id3 in range(id2+1, 5):
								position = enumerate(h3=radiant_ids[id1], h4=radiant_ids[id2], h5=radiant_ids[id3], T=T)
								if radiant_win:
									wrfile.seek(position*2*dtsize)
									wins = np.fromfile(wrfile, dtype=dt, count=1)
									wins += 1
									wrfile.seek(-dtsize, 1)
									wrfile.write(np.array(wins).tobytes())
								wrfile.seek((position*2*dtsize)+dtsize)
								total = np.fromfile(wrfile, dtype=dt, count=1)
								total += 1
								wrfile.seek(-dtsize, 1)
								wrfile.write(np.array(total).tobytes())
					for id1 in range(0, 3):
						for id2 in range(id1+1, 4):
							for id3 in range(id2+1, 5):
								position = enumerate(h3=dire_ids[id1], h4=dire_ids[id2], h5=dire_ids[id3], T=T)
								if not radiant_win:
									wrfile.seek(position*2*dtsize)
									wins = np.fromfile(wrfile, dtype=dt, count=1)
									wins += 1
									wrfile.seek(-dtsize, 1)
									wrfile.write(np.array(wins).tobytes())
								wrfile.seek((position*2*dtsize)+dtsize)
								total = np.fromfile(wrfile, dtype=dt, count=1)
								total += 1
								wrfile.seek(-dtsize, 1)
								wrfile.write(np.array(total).tobytes())

				# Quad Heroes
				with open("4.wr", "rb+") as wrfile:
					for id1 in range(0, 2):
						for id2 in range(id1+1, 3):
							for id3 in range(id2+1, 4):
								for id4 in range(id3+1, 5):
									position = enumerate(h2=radiant_ids[id1], h3=radiant_ids[id2], h4=radiant_ids[id3], h5=radiant_ids[id4], T=T)
									if radiant_win:
										wrfile.seek(position*2*dtsize)
										wins = np.fromfile(wrfile, dtype=dt, count=1)
										wins += 1
										wrfile.seek(-dtsize, 1)
										wrfile.write(np.array(wins).tobytes())
									wrfile.seek((position*2*dtsize)+dtsize)
									total = np.fromfile(wrfile, dtype=dt, count=1)
									total += 1
									wrfile.seek(-dtsize, 1)
									wrfile.write(np.array(total).tobytes())
					for id1 in range(0, 2):
						for id2 in range(id1+1, 3):
							for id3 in range(id2+1, 4):
								for id4 in range(id3+1, 5):
									position = enumerate(h2=dire_ids[id1], h3=dire_ids[id2], h4=dire_ids[id3], h5=dire_ids[id4], T=T)
									if not radiant_win:
										wrfile.seek(position*2*dtsize)
										wins = np.fromfile(wrfile, dtype=dt, count=1)
										wins += 1
										wrfile.seek(-dtsize, 1)
										wrfile.write(np.array(wins).tobytes())
									wrfile.seek((position*2*dtsize)+dtsize)
									total = np.fromfile(wrfile, dtype=dt, count=1)
									total += 1
									wrfile.seek(-dtsize, 1)
									wrfile.write(np.array(total).tobytes())

				# Quid Heroes
				with open("5.wr", "rb+") as wrfile:
					position = enumerate(h1=radiant_ids[0], h2=radiant_ids[1], h3=radiant_ids[2], h4=radiant_ids[3], h5=radiant_ids[4], T=T)
					if radiant_win:
						wrfile.seek(position*2*dtsize)
						wins = np.fromfile(wrfile, dtype=dt, count=1)
						wins += 1
						wrfile.seek(-dtsize, 1)
						wrfile.write(np.array(wins).tobytes())
					wrfile.seek((position*2*dtsize)+dtsize)
					total = np.fromfile(wrfile, dtype=dt, count=1)
					total += 1
					wrfile.seek(-dtsize, 1)
					wrfile.write(np.array(total).tobytes())

					position = enumerate(h1=dire_ids[0], h2=dire_ids[1], h3=dire_ids[2], h4=dire_ids[3], h5=dire_ids[4], T=T)
					if not radiant_win:
						wrfile.seek(position*2*dtsize)
						wins = np.fromfile(wrfile, dtype=dt, count=1)
						wins += 1
						wrfile.seek(-dtsize, 1)
						wrfile.write(np.array(wins).tobytes())
					wrfile.seek((position*2*dtsize)+dtsize)
					total = np.fromfile(wrfile, dtype=dt, count=1)
					total += 1
					wrfile.seek(-dtsize, 1)
					wrfile.write(np.array(total).tobytes())

				total_matches += 1

		with open("newnum.txt", "w") as newnum_file:
			newnum_file.write(str(newnum))

		with open("total.txt", "w") as total_file:
			total_file.write(str(total_matches))
	
		print(str(total_matches) + " matches parsed!")

	else:
		print("Insufficient matches! Abort!")
		break

print("Ended job with " + str(total_matches) + " matches parsed.")
