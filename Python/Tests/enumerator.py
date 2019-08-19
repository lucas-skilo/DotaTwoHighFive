import math
import datetime

def combination(n, r):
	return int(math.factorial(n) / (math.factorial(r) * (math.factorial(n-r))))

def enumerate(h5, T, h1 = None, h2 = None, h3 = None, h4 = None):
	h1min = 1

	if h1 is None:
		h2min = 1
		h1 = 0
	else:
		h2min = h1 + 1

	if h2 is None:
		h3min = 1
		h2 = 0
	else:
		h3min = h2 + 1

	if h3 is None:
		h4min = 1
		h3 = 0
	else:
		h4min = h3 + 1

	if h4 is None:
		h5min = 1
		h4 = 0
	else:
		h5min = h4 + 1

	result = 0

	if h1 is not None:
		for i in range(1, h1 - h1min + 1):
			result += combination(T - i, 4)

	if h2 is not None:
		for i in range(1, h2 - h2min + 1):
			result += combination(T - i - h1, 3)

	if h3 is not None:
		for i in range(1, h3 - h3min + 1):
			result += combination(T - i - h2, 2)

	if h4 is not None:
		for i in range(1, h4 - h4min + 1):
			result += T - i - h3

	result += h5 - h5min

	return result

#T = 114
#
#size = int(input())
#start = datetime.datetime.now()
#
#if (size == 1):
#	for h5 in range(1, T+1):
#		print(str(enumerate(h5=h5, T=T)))
#
#if (size == 2):
#	for h4 in range(1, T):
#		for h5 in range(h4+1, T+1):
#			print(str(enumerate(h4=h4, h5=h5, T=T)))
#
#if (size == 3):
#	for h3 in range(1, T-1):
#		for h4 in range(h3+1, T):
#			for h5 in range(h4+1, T+1):
#				print(str(enumerate(h3=h3, h4=h4, h5=h5, T=T)))
#
#if (size == 4):
#	for h2 in range(1, T-2):
#		for h3 in range(h2+1, T-1):
#			for h4 in range(h3+1, T):
#				for h5 in range(h4+1, T+1):
#					print(str(enumerate(h2=h2, h3=h3, h4=h4, h5=h5, T=T)))
#
#if (size == 5):
#	for h1 in range(1, T-3):
#		for h2 in range(1, T-2):
#			for h3 in range(h2+1, T-1):
#				for h4 in range(h3+1, T):
#					for h5 in range(h4+1, T+1):
#						print(str(enumerate(h1=h1, h2=h2, h3=h3, h4=h4, h5=h5, T=T)))
#
#end = datetime.datetime.now()
#print(str(end-start))