# Import the random integer function
from random import randint

# Define the stopping condition
stop = False

# Define a function that prints a random greeting
def greet():
	g = ["Hello", "Hi there", "What's up", "Hola"]
	print(g[randint(0,3)])

# Loop input
while not stop:
	inp = input("You have something to say? ")
	# Perform appropriate actions
	if inp == "Greet me":
		greet()
	elif inp == "go away":
		stop = True
	else:
		print("I don't know what you mean...")
	


