import time
import quicksort
import genRandList

def testTime():
	t1 = time.time()
	result = quicksort.quicksort(genRandList.genRandList(50000, 0, 999999999))
	t2 = time.time()
	print('%.3f seconds'%(t2-t1))
