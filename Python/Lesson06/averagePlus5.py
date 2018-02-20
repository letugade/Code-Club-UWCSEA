arr = []
t = 0

while True:
	inp = input("Enter a number for the array, or done: ")
	if inp == "done":
		break
	t += int(inp)
	arr.append(int(inp))

a = t/len(arr)

arr.append((a+5)*(len(arr) + 1) - t)
print(arr)