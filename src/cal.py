# import calendar
# import sys
import sys
import calendar


month = sys.argv[1]
year = sys.argv[2]
cal = calendar.TextCalendar()

if sys.argv[2] or sys.argv[1]:
  format_cal = cal.formatmonth(year, month)
  print(format_cal())
else:
  cal


