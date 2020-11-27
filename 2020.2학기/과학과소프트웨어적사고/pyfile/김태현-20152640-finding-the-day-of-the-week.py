import datetime

print("요일을 구하고자 하는 날짜를 연 월 일로 입력해 주세요.")

year = int(input(">> 연도를 입력해 주세요. :"))
month = int(input(">> 월  을 입력해 주세요. :"))
day = int(input(">> 일자를 입력해 주세요. :"))
print("\n>> datetime 패키지 활용해서 구하기")
dayofweek = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

# datetime 패키지 활용해서 구하는 방법 
weekday = datetime.date(year,month,day) - datetime.date(1,1,1)

print("{}년 {}월 {}일의 요일은 {} 입니다.".format(year, month, day, dayofweek[weekday.days%7]))

# 패키지 사용하지 않고 구하는 방법

print("\n>> 패키지 없이 구하기")
## 윤년 찾아 활용


days = 0
for i in range(1,year):
    if((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):
        days += 366
    else:
        days += 365

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    monthday = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    monthday = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(month-1):
    days += monthday[i]

days += day -1

print("{}년 {}월 {}일의 요일은 {} 입니다.".format(year, month, day, dayofweek[days%7]))
