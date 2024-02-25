from sys import exit
import rw_xlsx as rw


def determine_mode():
	mode = input("Would you like to read from a [s]helve or a [p]ortfolio spreadsheet?").lower()
	while mode != "s" and mode != "p":
		print("Invalid input, please try again")
		mode = input("Would you like to read from a [s]helve or a [p]ortfolio spreadsheet?")
	return mode


if __name__ == "__main__":
	#if shelve already found: ask to determine mode
	mode = determine_mode()
	if mode == "s" or mode == "shelve":
		db = rw.load_shelve()
	else:
		div_directory = input("What is the directory of your portfolio file? << ")
		print(f"Current files in your portfolio directory:")
		for file in sorted(dir_contents):
			print(f"\t {file}")
		filename = input("What is the full name of your portfolio file? << ")
		read_xlsx(f"{div_directory}{filename}")
	rw.dump_db()
	update_yn = input("Do you want to automatically update your portfolio data before working on it? [y/n]").lower()
	if update_yn == "y" or update_yn == "yes":
		update_stocks(db)
	else:
		exit()