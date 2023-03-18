import random
from datetime import datetime, timedelta

# Get user input for start and end dates
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Convert input strings to datetime objects
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

# Calculate the absolute value of the difference between the two dates:
delta = abs(end_date - start_date)

# Generate a random date between the start and end dates
random_days = random.randrange(delta.days)
new_date = start_date + timedelta(days=random_days)

# Check if the new date falls on a Monday
if new_date.weekday() == 0:
    print("I don't have vinaigrette!")
else:
    print("The new date is:", new_date.strftime('%Y-%m-%d'))
