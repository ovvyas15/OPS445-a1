import sys
from datetime import datetime, timedelta

# 1. mon_max function: Returns the maximum day for a given month, including leap year check.
def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        return 31
    elif month in [4, 6, 9, 11]:  # Months with 30 days
        return 30
    elif month == 2:  # February
        return 29 if leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

# 2. leap_year function: Checks if a year is a leap year.
def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# 3. valid_date function: Checks the validity of a given date in YYYY-MM-DD format.
def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid"
    try:
        str_year, str_month, str_day = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        
        return True
    except ValueError:
        return False

# 4. usage function: Provides usage instructions for the user.
def usage():
    "Print a usage message to the user"
    print("Usage: python assignment1.py YYYY-MM-DD YYYY-MM-DD")
    print("Example: python assignment1.py 2023-06-01 2023-06-10")
    print("The script calculates the number of weekend days between two dates.")

# 5. day_of_week function: Returns the day of the week for a given date.
def day_of_week(year: int, month: int, day: int) -> str:
    "Returns the day of the week ('mon', 'tue', 'wed', etc.)"
    return datetime(year, month, day).strftime('%a').lower()

# 6. after function: Returns the next date after the current date.
def after(date: str) -> str:
    "Returns the next date in YYYY-MM-DD format"
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    next_day = date_obj + timedelta(days=1)
    return next_day.strftime('%Y-%m-%d')

# 7. day_count function: Counts the number of weekend days (Saturday and Sunday) between two dates.
def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    if not valid_date(start_date) or not valid_date(stop_date):
        raise ValueError("Invalid date format")
    
    count = 0
    current_date = start_date

    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)
    
    return count

# Main block: Handles user input and calls the appropriate functions.
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    
    start_date = sys.argv[1]
    stop_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(stop_date):
        print("Error: One or both dates are invalid.")
        usage()
        sys.exit(1)
    
    try:
        weekends = day_count(start_date, stop_date)
        print(f"There are {weekends} weekend days between {start_date} and {stop_date}.")
    except ValueError as e:
        print(f"Error: {e}")
        usage()
        sys.exit(1)

