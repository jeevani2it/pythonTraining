words = ['consuming', 'dummy']

fh = open('toWrite.txt', 'w')
with open("toRead.txt") as f:
	for line in f:
		if any(word in line for word in words):
			fh.write(line)

fh.close()
