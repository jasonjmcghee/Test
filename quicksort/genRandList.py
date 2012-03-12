import random

def genRandList(length, minNum, maxNum):
	mylist = []
	
	while length > 0:
		mylist.append(random.randrange(minNum, maxNum))
		length -= 1

	return mylist
