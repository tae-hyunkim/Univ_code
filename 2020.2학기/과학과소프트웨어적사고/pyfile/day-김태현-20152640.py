import datetime

DayofWeek = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

criteria = input("기준연월일을 입력해 주세요(ex20190308):")

day = datetime.datetime(int(criteria[:4]),int(criteria[4:6]),int(criteria[6:]))

print("입력하신 기준 날짜는 {} 입니다.".format(day.strftime("%Y-%m-%d")))

later = int(input("기준날짜에서 더하고 싶은 일수를 입력해 주세요: "))

new_date = day + datetime.timedelta(days=later)
print("더한 날짜는 다음과 같습니다.",new_date.strftime("%Y-%m-%d"))
print("요일은 다음과 같습니다.", DayofWeek[new_date.weekday()])
