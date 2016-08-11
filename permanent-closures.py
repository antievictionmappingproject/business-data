## Program: Business Closure Analyzer
## Author: Katherine Phan <katherinexphan@gmail.com>
## About:
##
## This program reads a .csv of registered businesses in San Francisco, provided by data.sf.gov.
## It checks for businesses that have permanently closed since 2014, meaning that they closed in 2014
## and have not reopened later in 2015 or 2016.

## Currently does not look in 2014 for points of comparison. A more robust way of checking the closures is to
## compare the business' closure date against possible reopening dates. Right now we are missing businesses that
## close and reopen later in the year.

import csv
import time
from datetime import datetime
from pprint import pprint

def read():

	open_fifteen = set()
	open_sixteen = set()
	closed_fourteen = set()
	closed_fifteen = set()
	closed_fifteen_dict = {}

	csv_file = open('registered-business.csv')
	biz_list = csv.DictReader(csv_file)

	for biz in biz_list:
		opened = datetime.strptime(biz["Business_Start_Date"], '%M/%d/%Y')
		bizact = biz["DBA Name"]

		if opened.year == 2015:
			open_fifteen.add(bizact)
		elif opened.year == 2016:
			open_sixteen.add(bizact)

		if biz["Business_End_Date"]:
			closed = datetime.strptime(biz["Business_End_Date"],'%M/%d/%Y')
			if (closed.year == 2015):
				closed_fifteen.add(bizact)
			elif (closed.year == 2014):
				closed_fourteen.add(bizact)
				
	reopened = set.intersection(closed_fourteen, open_sixteen)
	reopened_ = set.intersection(closed_fourteen, open_fifteen)

	print "Unique businesses opened in 2016: ",len(open_sixteen)
	print "Business closed in 2014:", len(closed_fourteen)
	print "Businesses closed in 2015:" , len(closed_fifteen)
	print "Businesses that closed in 2014 and opened in 2015:", len(reopened_)
	print "Businesses that closed in 2014 and opened in 2016:", len(reopened)
	print "Businesses permanently closed since 2014: ", (len(closed_fourteen) - len(reopened_) - len(reopened))



def main():
	read()

if __name__ == "__main__":
    main()