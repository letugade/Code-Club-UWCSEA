# Initialise variables
stop = False
s1 = 100000000
s2 = 100000000

# Continually take input
while not stop:
	inp = input("Enter an integer, or stop: ")

	# Stop execution if the user types 'stop'
	if inp == "stop": break

	# Handle the case where the user gave us bad input
	try:
		int(inp)
	except Exception as e:
		print("You did not enter stop, or an integer")
		continue

	# Update the variables as needed
	if int(inp) <= s1:
		s2 = s1
		s1 = int(inp)
	elif int(inp) < s2:
		s2 = int(inp)

# Output the second smallest number
print("The second smallest number is", s2)