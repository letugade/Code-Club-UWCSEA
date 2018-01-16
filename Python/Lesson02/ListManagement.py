myList = []


while True:
	print()
	command = input("Enter your command (add, remove, print, exit): ").upper()
	if command == "ADD":
		val = input("Please enter the value you want to add: ")
		try:
			myList.append(val)
		except Exception as e:
			print("Unable to add", val, "to list.")
		
	elif command == "REMOVE":
		val = input("Please enter the value you want to remove: ")
		try:
			myList.remove(val)
		except Exception as e:
			print("Unable to remove", val, "from list.")
	elif command == "PRINT":
		try:
			print(myList)
		except Exception as e:
			print("Unable to print the list...")
	elif command == "EXIT":
		print("Thank you for using the list management app.")
		break
	else:
		print("Please enter a valid command (add, remove, print, exit).")

print()