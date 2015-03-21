from tkinter import *
import datetime
from utils import differenceManual, MONTHS_TO_DAYS

def getTodayInfo():
	today = datetime.datetime.now()
	return [today.month, today.day, today.year]

def main():
	root = Tk()

	root.title("Day Calculator")

	Birthdate = Label(root, text="Birth Day").grid(row=0, column=0)
	Today = Label(root, text="Today").grid(row=0, column=2)
	monthLabel = Label(root, text="Month(MM)").grid(row=1, column=1)
	dayLabel = Label(root, text="Day(DD)").grid(row=2, column=1)
	yearLabel = Label(root, text="Year(YYYY)").grid(row=3, column=1)

	# want to make a switch thingy
	# is a spinbox, but still funky though.

	# the birth info
	birthMonth = Spinbox(root, from_=1, to=12, bd =5)
	birthDay = Spinbox(root, from_=1, to=31, bd =5)
	birthYear = Spinbox(root, from_=1900, to=3000, bd =5)
	birthMonth.delete(0, END)
	birthMonth.insert(10, 12)
	birthDay.delete(0, END)
	birthDay.insert(10, 5)
	birthYear.delete(0, END)
	birthYear.insert(10, 1994)

	# today info
	todayMonth = Spinbox(root, from_=1, to=12, bd =5)
	todayDay = Spinbox(root, from_=1, to=31, bd =5)
	todayYear = Spinbox(root, from_=1900, to=3000, bd =5)
	today = getTodayInfo()
	todayMonth.delete(0, END)
	todayMonth.insert(10, today[0])
	todayDay.delete(0, END)
	todayDay.insert(10, today[1])
	todayYear.delete(0, END)
	todayYear.insert(10, today[2])

	# grid it!
	birthMonth.grid(row=1, column=0)
	birthDay.grid(row=2, column=0)
	birthYear.grid(row=3, column=0)
	todayMonth.grid(row=1, column=2)
	todayDay.grid(row=2, column=2)
	todayYear.grid(row=3, column=2)

	text = Entry(root, bd=5)
	text.insert(END, "Press Submit")
	text.grid(row=4, column=2)

	# functions
	def calculate():
		text.delete(0, END)
		days = differenceManual(
					int(birthMonth.get()), 
					int(birthDay.get()),
					int(birthYear.get()), 
					int(todayMonth.get()),
					int(todayDay.get()), 
					int(todayYear.get()) )
		if days == -1:
			string = "Incorrect Date"
		else:
			string = str(days) + " Days Old!"
		text.insert(END, string)

	submit = Button(root, text ="Submit", command = calculate)
	quit = Button(root, text='Quit', command=root.quit)
	submit.grid(row=4, column=1) 
	quit.grid(row=4, column=0)

	# run!!!    
	root.mainloop()

main()