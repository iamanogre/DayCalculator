from utils import difference 

def intro():
	print("Gonna find out how old you is.")

def ask():
	birth = input("Enter your birthday in MM/DD/YYYY format: ")
	today = input("Enter today's day in MM/DD/YYYY format: ")
	return birth, today

def main():
	intro()
	start, stop = ask()
	days = difference(start, stop)
	print('You are', days, 'days old')

main()