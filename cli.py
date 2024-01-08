def determine_mode():
	mode = input("Would you like to read from a [s]helve or a [p]ortfolio spreadsheet?").lower()
	while mode != "a" and mode != "p":
		print("Invalid input, please try again")
		mode = input("Would you like to read from a [s]helve or a [p]ortfolio spreadsheet?")
	return mode


if __name__ == "__main__":
	mode = determine_mode()