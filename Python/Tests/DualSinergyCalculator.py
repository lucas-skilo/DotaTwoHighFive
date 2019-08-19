import numpy as np
from enumerator import enumerate

def winrate1(id1, file, dtype):
	position = enumerate(h5=id1, T=114)
	file.seek(position*2*dtype.itemsize)
	wins = np.fromfile(file, dtype=dtype, count=1)[0]
	total = np.fromfile(file, dtype=dtype, count=1)[0]

	if (total == 0):
		return 0.0

	return wins/total

def winrate2(id1, id2, file, dtype):
	position = enumerate(h4=id1, h5=id2, T=114)
	file.seek(position*2*dtype.itemsize)
	wins = np.fromfile(file, dtype=dtype, count=1)[0]
	total = np.fromfile(file, dtype=dtype, count=1)[0]

	if (total == 0):
		return 0.0

	return wins/total

dt = np.dtype(np.int32)

wr1 = open("1.wr", "rb")
wr2 = open("2.wr", "rb")

for hero1 in range(1, 114):
	for hero2 in range(hero1+1, 115):
		wrhero1 = winrate1(hero1, wr1, dt)
		wrhero2 = winrate1(hero2, wr1, dt)
		wrhero12 = winrate2(hero1, hero2, wr2, dt)

		wrmean = (wrhero1 + wrhero2) / 2

		if wrhero12 == 0.0:
			wrfactor = 0.0
		else:
			wrfactor = wrhero12 - wrmean

		if(wrfactor >= 0):
			print("Heroes " + str(hero1) + " and " + str(hero2) + " have good sinergy!: " + str(wrfactor))
		else:
			print("Heroes " + str(hero1) + " and " + str(hero2) + " have bad sinergy!: " + str(wrfactor))

		#if wrhero1 != 0.0 and wrhero2 != 0.0 and wrhero12 != 0.0:
		#	print("Hero " + str(hero1) + " has winrate " + str(wrhero1) + ", Hero " + str(hero2) + " has winrate " + str(wrhero2) + ", but together they have winrate " + str(wrhero12))