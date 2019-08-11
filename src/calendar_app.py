import sys
from datetime import datetime
import calendar

def main(argv):

	if len(argv) == 0:
		# prints out current month as a calender if no arguments are passed
		current_year, current_month = datetime.now().year, datetime.now().month
		print("Current month calendar\n")
		print(calendar.month(current_year, current_month))
	elif len(argv) == 1:
		current_year = datetime.now().year
		current_month = int(argv[0])
		print(calendar.month(current_year, current_month))
	elif len(argv) == 2:
		current_year = int(argv[1])
		current_month = int(argv[0])
		print(calendar.month(current_year, current_month))
	else:
		print("\nUsage: python calendar_app.py <month> <year>\n")
		print("Example: python calendar_app.py 5 2019\n")
		sys.exit(2)



if __name__ == '__main__':

	# exclude script name from the arguments list and pass it to main()
	main(sys.argv[1:])




