import shelve
import update
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

def load_shelve(db_name="portfolio"):
	db = shelve.open(db_name)
	return db

def update_stocks(db):
	#TODO: iterate through all isins and call get_consorsbank_info
	for key in db:
		isin = db[key].isin
		updates = update.get_consorsbank_info(isin)
		db[key].price = updates[0]
		db[key].dividend_per_share = updates[1]
