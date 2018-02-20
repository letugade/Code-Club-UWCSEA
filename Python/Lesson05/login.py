# admin, admin
# Import libraries
import hashlib, sys, pickle

# Helper functions
def exit():
	f = open("saveFile", "wb")
	pickle.dump(creds, f)
	f.close()
	sys.exit()

def load():
	f = open("saveFile", "rb")
	creds = load(f)
	f.close()

# Set up encryption system
#creds = {"admin": "21232f297a57a5a743894a0e4a801fc3"}
load()

while True:
	# Take in login details
	print("\nWelcome! Please log in below")
	uname = input("Enter your username: ")
	pword = input("Enter your password: ")

	# Encrypt password
	encrypter = hashlib.md5()
	encrypter.update(str(pword).encode('utf-8'))
	pwordC = encrypter.hexdigest()

	# Check if user exists
	print("")
	if uname not in creds:
		print("The user", uname, "does not exist")
		exit()

	# Check if password is correct
	if creds[uname] != pwordC:
		print("Wrong password")
		print("You input", pword.encode('utf-8'))
		print(creds[uname], "is not equal to", pwordC)
		exit()

	# Print welcome message
	print("Welcome,", uname)

	# Start the prompt
	userCommand = ""

	while userCommand != "exit":
		userCommand = input(">>> ").lower()
		print()
		if userCommand == "exit":
			exit()
		elif userCommand == "help":
			print("Commands are as follows:\n" + 
				"\thelp\n" + 
				"\texit\n" + 
				"\tlogout\n" + 
				"\tadd user\n" + 
				"\tremove user\n")
		elif userCommand == "add user":
			if uname != "admin":
				print("You are not authorised to perform this operation")
				continue
			newUsername = input("Enter the username for the new user: ")
			newPassword = input("Enter the password for the new user: ")
			encrypter = hashlib.md5()
			encrypter.update(str(newPassword).encode('utf-8'))
			pwordC = encrypter.hexdigest()
			creds[newUsername] = pwordC
			print("You input", pwordC.encode('utf-8'))
			print("User", newUsername, "created with password", pwordC)
		elif userCommand == "remove user":
			if uname != "admin":
				print("You are not authorised to perform this operation")
				continue
			newUsername = input("Enter the username for the user to be removed: ")
			if newUsername not in creds:
				print("The user", newUsername, "does not exist")
				continue
			creds.pop(newUsername)
		elif userCommand == "logout":
			break
		else:
			print("Invalid command. For help, type 'help'.")



