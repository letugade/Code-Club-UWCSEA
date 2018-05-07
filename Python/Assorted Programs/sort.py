from random import random
from datetime import datetime

def mySort(arr):
	for i in range(len(arr)):
		for j in range(i-1, len(arr)-1):
			if (arr[j+1] < arr[j]):
				(arr[j+1], arr[j]) = (arr[j], arr[j+1])


a = [random() for i in range(10000)]
startTime = datetime.now()
mySort(a)
timeTaken = datetime.now() - startTime
print("Took", str(timeTaken.seconds) + "." + str(timeTaken.microseconds), "seconds.")
