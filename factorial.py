from functools import reduce

def fact(n):
	"""Doctest
	>>> fact(5)
	120
	"""
	return reduce(lambda x,y: x*y, range(1, n+1), 1)
