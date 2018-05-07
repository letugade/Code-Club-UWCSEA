import math
p = (math.sqrt(5) + 1) / 2
def f(i):
	return int((math.pow(p,i) - math.pow(-p, -i)) / math.sqrt(5))
inp = 0
while(True):
	inp = int(input("Enter the index you want to find: "))
	if inp == -1:
		break
	print(f(inp))

