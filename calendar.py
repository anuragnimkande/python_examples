import calendar

# Input the year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Create a calendar for the specified year and month
cal = calendar.month(year, month)

# Print the calendar
print("Calendar:")
print(cal)
