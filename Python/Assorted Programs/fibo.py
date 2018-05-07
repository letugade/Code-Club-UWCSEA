x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
n = int(input("How mnay terms do you want to print out: "))

for i in range(n):
	print(x)
	temp = x+y
	x = y
	y = temp
