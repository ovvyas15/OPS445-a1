#!/usr/bin/env python3

import sys
from datetime import datetime, date, timedelta

def leap_year(year):
    """Return True if year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month, year):
    """Return the maximum number of days in the given month and year."""
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def valid_date(date_str):
    """Return True if date_str is a valid date in YYYY-MM-DD format."""
    try:
        # Check format
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            return False
        
        # Parse year, month, day
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
        
        # Check ranges
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False
            
        # Check day against month maximum
        if day > mon_max(month, year):
            return False
            
        return True
    except ValueError:
        return False

def day_of_week(year, month, day):
    """Return the day of the week (mon, tue, etc.) for the given date."""
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    d = date(year, month, day)
    # Adjust for Python's week starting on Monday (0)
    return days[d.weekday()]

def after(date_str):
    """Return the next date after date_str in YYYY-MM-DD format."""
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    
    # Create date object and add one day
    d = date(year, month, day)
    next_date = d + timedelta(days=1)
    
    # Format result as YYYY-MM-DD
    return next_date.strftime('%Y-%m-%d')

def day_count(start_date, end_date):
    """Return the number of weekend days between start_date and end_date inclusive."""
    # Convert strings to date objects
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    
    # Ensure start is before end
    if start > end:
        start, end = end, start
    
    # Count weekend days
    weekend_days = 0
    current = start
    while current <= end:
        if current.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
            weekend_days += 1
        current += timedelta(days=1)
    
    return weekend_days

def usage():
    """Print usage message."""
    print("Usage: python3 assignment1.py <date1> <date2>")
    print("Date format: YYYY-MM-DD")
    sys.exit()

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 3:
        usage()
    
    date1, date2 = sys.argv[1], sys.argv[2]
    
    # Validate dates
    if not valid_date(date1) or not valid_date(date2):
        usage()
    
    # Ensure dates are in chronological order
    if date1 > date2:
        date1, date2 = date2, date1
    
    # Calculate weekend days
    weekend_count = day_count(date1, date2)
    
    # Print result
    print(f"The period between {date1} and {date2} includes {weekend_count} weekend days.")
