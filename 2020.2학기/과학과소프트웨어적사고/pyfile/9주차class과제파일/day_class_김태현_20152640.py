import datetime

class Date_class:

    def __init__(self,standard_date):
        self.standard_date = standard_date
        self.date = datetime.datetime(int(standard_date[:4]),
                                      int(standard_date[4:6]),
                                      int(standard_date[6:]))
        self.DayofWeek = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
        print("\n>> 입력하신 기준 날짜는 {} 입니다.\n".format(self.date.strftime("%Y-%m-%d")))


    def add_date(self,later):
        
        new_date = self.date + datetime.timedelta(days=later)
        print("\n>> 더한 날짜는 다음과 같습니다.",new_date.strftime("%Y-%m-%d"))
        print("\n>> 요일은 다음과 같습니다.", self.DayofWeek[new_date.weekday()])


def main():

    n = input("\n>> 기준연월을 입력해 주세요(ex:20190308):")
    
    date = Date_class(n)

    add = int(input('\n>> 더하고자 하는 날짜를 입력해 주세요:'))
    date.add_date(add)

main()

        
