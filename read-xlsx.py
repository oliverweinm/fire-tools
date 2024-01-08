import shelve
import pandas as pd
from stock import Stock
from os import listdir
from os.path import isfile, join

"""
#TODO: Mechanism which gives filename
#Implemented in the GUI.py or CLI.py
Documentation:
https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
"""

def read_xlsx(filename):
	#TODO: Implement read with pandas, then transform to Python shelv
	excel_df = pd.read_excel(filename, index_col=0)
	portfolio = list()
	db = shelve.open("portfolio")
	for index, row in excel_df.iterrows():
		db[index] = Stock(index, row[1], row[0], row[2], row[7])
	db.close()


def write_xlsx(filename, values):
	#TODO: turn the Python shelve back to an xlsx spreadsheet
	raise NotImplementedError

def dump_db(db_name="portfolio"):
	db = shelve.open(db_name)
	for key in db:
		print(key, "=>\n   ", db[key].name, db[key].amount, db[key].price)

def load_shelve(db_name="portfolio")
	db = shelve.open(db_name)
	return db


if __name__ == "__main__":
	mode = determine_mode()
	if mode == "s" or mode == "shelve":
		db = load_shelve()
	else:
		div_directory = input("What is the directory of your portfolio file? << ")
		print(f"Current files in your portfolio directory:")
		for file in sorted(dir_contents):
			print(f"\t {file}")
		filename = input("What is the full name of your portfolio file? << ")
		read_xlsx(f"{div_directory}{filename}")
	dump_db()
	update_yn = input("Do you want to automatically update your portfolio data before working on it?")