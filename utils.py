# UTILS.PY

# Standard things
MONTHS_TO_DAYS = { 1:31, 2:28, 3:31, 4:30, \
				   5:31, 6:30, 7:31, 8:31, \
				   9:30, 10:31, 11:30, 12:31 }

MONTH_TO_NUM = { "jan": 1, "feb": 2, "mar": 3, \
				 "apr": 4, "may": 5, "jun": 6, \
				 "jul": 7, "aug": 8, "sep": 9, \
				 "oct": 10, "nov": 11, "dec": 12 }

# for future updates
DAY_TO_NUM = { "sunday": 1, "monday": 2, "tueday": 3, \
			   "wednesday": 4, "thursday": 5, "friday": 6, \
			   "saturday": 7 }

NUM_TO_DAY = { 1: "sunday", 2: "monday", 3: "tuesday", \
			   4: "wednesday", 5: "thursday", 6: "friday", \
			   7: "saturday" }

MONTH_FIRST = 1
MONTH_LAST = 12
YEAR_STANDARD = 365
YEAR_LEAP = 366

def isLeapYear(year):
	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 == 0):
				return True
			else:
				return False
		else:
			return True
	else:
		return False

#def convertMonth(month):

#return days in difference of days
def differenceDays(day1, day2):
	if day1 < day2:
		return differenceDays(day2, day1)
	return day1 - day2 + 1

#days left in month to finish
def daysLeft(month, day):
	days = MONTHS_TO_DAYS[month]
	return differenceDays(days, day)

# from day 1 to day whatever
def daysExcess(day):
	return differenceDays(day, 1)

# return days in difference of months
def differenceMonths(month1, month2, inclusiveStart=True, inclusiveEnd=False):
	#assert!!!
	if month2 < month1: #strange, I don't know if I need this
		return differenceMonths(month2, month1)
	counter = 0
	if not inclusiveStart:
		month1 += 1
	if inclusiveEnd:
		month2 += 1
	for num in range(month1, month2):
		counter += MONTHS_TO_DAYS[num]
	return counter

# return days in difference of years
def differenceYears(year1, year2, inclusiveStart=False):
	#assert
	counter = 0
	if not inclusiveStart:
		year1 += 1
	for num in range(year1, year2):
		if isLeapYear(num):
			counter += YEAR_LEAP
		else:
			counter += YEAR_STANDARD
	return counter

#start a year (as in finish)
def startYear(month, day):
	counter = 0
	counter += differenceMonths(MONTH_FIRST, month)
	counter += daysExcess(day)
	return counter

#end a year/ return number of days
def endYear(month, day):
	counter = 0
	counter += daysLeft(month, day)
	counter += differenceMonths(month, MONTH_LAST, inclusiveStart=False, inclusiveEnd=True)
	return counter

def isvalidDate(date):
	month, day, year = date
	if year < 0:
		return False
	if month < MONTH_FIRST or month > MONTH_LAST:
		return False
	if MONTHS_TO_DAYS[month] < day:
		return False
	return True

def parse(strDate):
	date = tuple(int(x) for x in strDate.replace('/', ' ').split())
	if isvalidDate(date):
		return date
	else:
		return (0, 0, 0) # or possibly exception???

def difference(date1, date2):
	data1 = parse(date1) 
	data2 = parse(date2)
	month1, day1, year1 = data1
	month2, day2, year2 = data2
	return differenceManual(month1, day1, year1, month2, day2, year2)

def differenceManual(month1, day1, year1, month2, day2, year2):
	if year1 > year2:
		return 0
	counter = 0
	if month1 == month2 and year1 == year2:
		counter += differenceDays(day1, day2)
	elif year1 == year2:
		counter += daysLeft(month1, day1)
		counter += differenceMonths(month1, month2)
		counter += daysExcess(day2)
	else:
		counter += endYear(month1, day1)
		counter += differenceYears(year1, year2)
		counter += startYear(month2, day2)
		#counter *= 60 * 60 * 24 # calculations in seconds
	return counter