import numpy as np
import os

from Enumerator import Enumerator

a = np.array(0, dtype=np.int32)
b = np.array(0, dtype=np.int32)

total = input("Please insert how many heroes exist in dota currently: ")
print(total)
total_int = int(total)
enumerator = Enumerator(total_int)

try:
    os.mkdir(total)
except:
    pass

file = open(total + "/1.wr", "wb+")
for i in range(0, enumerator.enumerate(total_int)+1):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("1 done")
file.close()

file = open(total + "/2.wr", "wb+")
for i in range(0, enumerator.enumerate(total_int-1, total_int)+1):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("2 done")
file.close()

file = open(total + "/3.wr", "wb+")
for i in range(0, enumerator.enumerate(total_int-2, total_int-1, total_int)+1):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("3 done")
file.close()

file = open(total + "/4.wr", "wb+")
for i in range(0, enumerator.enumerate(total_int-3, total_int-2, total_int-1, total_int)+1):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("4 done")
file.close()

file = open(total + "/5.wr", "wb+")
for i in range(0, enumerator.enumerate(total_int-4, total_int-3, total_int-2, total_int-1, total_int)+1):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("5 done")
file.close()
