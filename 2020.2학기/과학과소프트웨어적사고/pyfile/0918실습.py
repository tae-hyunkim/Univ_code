import datetime

now = datetime.datetime.now()

print("현재시간은", now, "입니다.")
print("현재는",'오전' if now.hour <12 else '오후','입니다.')
print("END")


year = int(input("판단하고자 하는 연도를 입력해 주세요:"))

if year % 4 == 0 :
    if year%400 == 0:
        a = '윤년'
    elif year % 100 == 0:
        a = '윤년아님'
    else:
        a = '윤년'
else:
    a = '윤년아님'
print(a)

if year % 400 == 0 :
    a = '윤년'
elif year % 100 == 0:
    a = '윤년아님'
elif year % 4 == 0:
    a ='윤년'
else:
    a = '윤년아님'
print(a)

if (year % 400 == 0) or ((year % 4 == 0) and (not(year%100 == 0))):
    print("\n{} is a leap year".fotmat(year))
else:
    print("\n{} is not a leap year".format(year))
