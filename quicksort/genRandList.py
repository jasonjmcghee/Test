import random

def genRandList(length, minNum, maxNum):
	mylist = []
	for x in range(length): mylist.append(random.randrange(minNum, maxNum+1))
	return mylist
