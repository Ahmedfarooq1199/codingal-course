

import datetime


now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Today's Date:", now.date())
print("Current Time:", now.time())


hour = now.hour

if hour < 12:
    print("Good Morning!")
elif 12 <= hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")


weekday = now.weekday()

if weekday < 5:
    print("Today is a Weekday. Time for work/study!")
else:
    print("It's the Weekend! Relax and enjoy.")
