#1. INCLUDE VER 1.3
#2. ACCEPT DAY-OF-WEEK, VALIDATE.
#3. DISPLAY: FUTURE DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR, DAY-OF-WEEK

weekday=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]#subscripts
dayss=[0,'st','nd','rd']+['th']*17+['st','nd','rd']+['th']*7+['st']
monthss=[0,'January','February','March','April','May','June','July','August','September','October','November','December']
days_in_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_nonleap = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print('Enter the Day, Month, Year and Day of week')                 #collect inputs from user and validate
year=input('Year: ')
if year.isdigit():                                                  # year validation
    year=int(year)
else:
    print('Invalid year, program will exit now')
    exit()
month=input('Month: ')
if month.isdigit()and 0<int(month) <13:                             #  month validation
    month=int(month)
else:
    print('Invalid month, program will exit now')
    exit()

if year%4==0:                                                       # leap year check
    days_in_year=days_in_leap
else:
    days_in_year=days_in_nonleap


day=input('Day: ')
if day.isdigit() and 0<int(day)<=int(days_in_year[month]):          # day validation
    day=int(day)
else:
    print('%d %s has only %s days, program will exit now'%(year,monthss[month],days_in_year[month]))
    exit()

daysinfuture=input('Enter the days in future 0<year>90:')


day_of_week=input('Enter the day of week: ')                        # day of the week validation
day_of_week=day_of_week.upper()
if day_of_week not in weekday:
    print('Invalid weekday, program now will exit')
    exit()

location=weekday.index(day_of_week)                                 # finding the position of day of week from weekday list

if daysinfuture.isdigit():                                          # future day validation
    daysinfuture=int(daysinfuture)
else:
    print('Invalid entry, program will exit now')
    exit()
future_day_of_week=weekday[(location+daysinfuture)%7]               # finding the day of week for future day

if day+daysinfuture <= days_in_year[month]:                         #check if the future day is in the same month
    balancedays=day+daysinfuture
else :
    balancedays=day+daysinfuture-days_in_year[month]                # check if the future date is within the range of three months
    if month > 11:
        month = 1
        year = year + 1
        if year%4==0:
            days_in_year = days_in_leap
        else:
            days_in_year = days_in_nonleap

    if balancedays > (days_in_year[int(month)]):
        balancedays = balancedays - days_in_year[month]
        month = month + 1
        if month>11:
            month=1
            year=year+1
            if year % 4 == 0:
                days_in_year = days_in_leap
            else:
                days_in_year = days_in_nonleap

    if balancedays > (days_in_year[int(month)]):
        balancedays = balancedays - days_in_year[month]
        month = month + 1
        if month>11:
            month=1
            year=year+1
print('%s%s'%(balancedays,dayss[balancedays]), monthss[int(month)] , year, future_day_of_week)

