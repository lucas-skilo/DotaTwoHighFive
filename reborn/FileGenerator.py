import numpy as np
import os

from Enumerator import Enumerator

class FileGenerator(object):

	def __init__(self, total):
		self.total = total
		self.a = np.array(0, dtype=np.int32)
		self.b = np.array(0, dtype=np.int32)
		self.enumerator = Enumerator(self.total)

		try:
			os.mkdir(str(self.total))
		except:
			pass

	def generate_1(self):
		file = open(str(self.total) + "/1.wr", "wb+")
		for _ in range(0, self.enumerator.enumerate(self.total)+1):
			file.write(self.a.tobytes())
			file.write(self.b.tobytes())
		print("1 done")
		file.close()

	def generate_2(self):
		file = open(str(self.total) + "/2.wr", "wb+")
		for _ in range(0, self.enumerator.enumerate(self.total-1, self.total)+1):
			file.write(self.a.tobytes())
			file.write(self.b.tobytes())
		print("2 done")
		file.close()

	def generate_3(self):
		file = open(str(self.total) + "/3.wr", "wb+")
		for _ in range(0, self.enumerator.enumerate(self.total-2, self.total-1, self.total)+1):
			file.write(self.a.tobytes())
			file.write(self.b.tobytes())
		print("3 done")
		file.close()

	def generate_4(self):
		file = open(str(self.total) + "/4.wr", "wb+")
		for _ in range(0, self.enumerator.enumerate(self.total-3, self.total-2, self.total-1, self.total)+1):
			file.write(self.a.tobytes())
			file.write(self.b.tobytes())
		print("4 done")
		file.close()

	def generate_5(self):
		file = open(str(self.total) + "/5.wr", "wb+")
		for _ in range(0, self.enumerator.enumerate(self.total-4, self.total-3, self.total-2, self.total-1, self.total)+1):
			file.write(self.a.tobytes())
			file.write(self.b.tobytes())
		print("5 done")
		file.close()
	
	def generate_all(self):
		self.generate_1()
		self.generate_2()
		self.generate_3()
		self.generate_4()
		self.generate_5()
	
	def generate(self, how_many):
		if how_many not in range(1,6):
			raise Exception("File count is invalid ({})".format(how_many))
		self.generate_1()
		if how_many > 1:
			self.generate_2()
		if how_many > 2:
			self.generate_3()
		if how_many > 3:
			self.generate_4()
		if how_many > 4:
			self.generate_5()
