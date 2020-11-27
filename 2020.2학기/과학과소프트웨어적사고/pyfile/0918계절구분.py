import datetime

now = datetime.datetime.now()
month = now.month//3
if month == 1 :
    print('봄')
elif month == 2:
    print("여름")
elif month == 3:
    print("가을")
else:
    print("겨울")
