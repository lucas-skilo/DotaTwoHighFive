import numpy as np
from enumerator import enumerate

a = np.array(0, dtype=np.int32)
b = np.array(0, dtype=np.int32)

file = open("1.wr", "wb+")
for i in range(1, enumerate(h5=114, T=114)+2):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("1 done")
file.close()

file = open("2.wr", "wb+")
for i in range(1, enumerate(h4=113, h5=114, T=114)+2):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("2 done")
file.close()

file = open("3.wr", "wb+")
for i in range(1, enumerate(h3=112, h4=113, h5=114, T=114)+2):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("3 done")
file.close()

file = open("4.wr", "wb+")
for i in range(1, enumerate(h2=111, h3=112, h4=113, h5=114, T=114)+2):
	file.write(a.tobytes())
	file.write(b.tobytes())
print("4 done")
file.close()

#file = open("5.wr", "wb+")
#for i in range(1, enumerate(h1=110, h2=111, h3=112, h4=113, h5=114, T=114)+2):
#	file.write(a.tobytes())
#	file.write(b.tobytes())
#print("5 done")
#file.close()