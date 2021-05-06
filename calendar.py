# What's today?
day = int(input('Day (0-6)? '))

if day == 0:
    print('Today is Sunday.')
elif day == 1:
    print('Today is Monday.')
elif day == 2:
    print('Today is Tuesday.')
elif day == 3:
    print('Today is Wednesday.')
elif day == 4:
    print('Today is Thursday.')
elif day == 5:
    print('Today is Friday.')
elif day == 6:
    print('Today is Saturday.')
else:
    print('Please type a number 0-6.')

# Do I have to work today?
if day >= 1 and day <= 5:
    print('It\'s a weekday. Time to go to work.')
elif day == 0 or day == 6:
    print('It\'s the weekend! You\'re free to sleep-in.')
