def quicksort(mylist):
	#Using my ternary operators :D
	"""Works well with genRandList.py
	quick little doctest...
	>>> quicksort([4, 5, 3, 6, 1, 34, 556, 734, 34, 25, 266, 32, 16, 278])
	[1, 3, 4, 5, 6, 16, 25, 32, 34, 34, 266, 278, 556, 734]
	"""

	return [] if mylist == [] else quicksort([x for x in mylist[1:] if x < mylist[0]]) + [mylist[0]] + quicksort([x for x in mylist[1:] if x >= mylist[0]])
