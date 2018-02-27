print()

x = 1
count = 0
lastYear = int(input("Enter previous year of appearance: "))
repYear = int(input("Enter number of years in cycle: "))
n = int(input("Enter how many of leap years you want to output: "))

print()

if (lastYear % 2 == 1) and (repYear % 2 == 0):
	print("No such leap year exists")
	exit()

while count < n:
	year = lastYear + (x * repYear)
	if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
		print(year)
		count += 1
	x += 1

print()