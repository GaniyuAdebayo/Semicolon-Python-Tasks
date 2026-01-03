def encryption():

	real_password = input("Enter password to be encrypted: ")

	difference = int(input("Enter difference in character: "))

	encrypted_password = ""

	for letter in real_password:

		encrypted_password = encrypted_password + chr(ord(letter) + difference)

	return encrypted_password


print(encryption())