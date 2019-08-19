prev = int(input())
print("Start = " + str(prev))
i = 1
while(1):
	value = input()
	i += 1
	if (value == "END"):
		print("SUCCESS, End = " + str(current))
		exit()
	else:
		current = int(value)
		if (current != prev + 1):
			print("WRONG! LINE=" + str(i) + " Got " + str(current) + ", expected " + str(prev + 1) + ".")
			exit()
		prev += 1