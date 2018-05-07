num = int(input("Enter a number: "))
base = int(input("Enter a base: "))
out = ""

conversions = {
	0: "0",
	1: "1",
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9",
	10: "A",
	11: "B",
	12: "C",
	13: "D",
	14: "E",
	15: "F",
}

if num == 0:
	out = "0"

while (num != 0):
	rem = num % base
	quo = num // base
	out = str(conversions[rem]) + out
	num = quo

print(out)