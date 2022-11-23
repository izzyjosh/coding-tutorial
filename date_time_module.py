

#d = timedelta(days = 25, microseconds = -1, weeks = 2, hours = 7 )
#print(d)
#print(timedelta.min)
#print(timedelta.max)
#print(timedelta.resolution)

#c = timedelta(days = 50)
#f = timedelta(days = 30)
#e = c - f
#print(e)

from datetime import date
#year = timedelta(days=365)
#ten_years = 10 * year
#print(ten_years)
#timedelta(days=3650)
#print(ten_years.days // 365)

#nine_years = ten_years - year
#nine_years
#datetime.timedelta(days=3285)
#three_years = nine_years // 3
#three_years, three_years.days // 365
#(datetime.timedelta(days=1095), 3)
#print(datetime.date(2004, 5, 7))

year = int(input("Enter year: "))
month= int(input("Enter month : "))
day = int(input("Enter day: "))
date1 = date(year, month, day)
date2 = date.today()
print(date1 - date2)