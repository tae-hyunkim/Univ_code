# 모듈 import 
import random, sys

# 함수 정의 Part
'''
제작한 함수는 Create_year, Check_year, Worldcup_year_check, Worldcup_Area 4가지이다.

Create_year 함수는 Check_year에 삽입되어 활용 되며 random하게 연도값을 제작하는 함수이다.

Check_year 함수는 Worldcup_year_check 함수에 활용되며 만들어진 연도값이 주어진 조건 2020 ~ 2050연도 내의 값을 가지고 있는지, 그동안 제작된 연도 값과 조건을 만족하는 연도값을 내보내는 함수이다.

Worldcup_year_check 함수는 Worldcup_Area에 Worldcup 개최연도값이 value값으로 설정이 되었을 때 활용되며 개최연도가 아닐경우 자기자신을 다시 실행하는 재귀함수이다.
Worldcup_year_check 함수에 Y,y,N,n을 활용하여 개최연도를 다시 찾을지 확인하는 함수에서 잘못된 값이 삽입되었을 때를 대비하여 제대로 된 값을 입력받을 때까지 다시 입력받도록 작업을 수행하였다. 

Worldcup_Area 함수는 주어진 월드컵 연도에 대하여 어떤 대륙에서 개최되는지에 대하여 알려주는 함수이다. 

'''
## 처음 4자리의 값을 가진 연도값을 만드는 함수
def Create_year():

    # 주사위 굴려 나오는 값 삽입할 list 생성 
    values = []

    # 주사위를 4번 굴려 나오는 값 list에 삽입
    for i in range(4):

        values += [random.randint(0,9)]

    # 주사위를 통해 나온 값을 year로 표현하기 위한 value 값 정의
    value = 0
    
    # 자리수 이용 값 Define
    # 첫번째 자리 값은 1000 두번째는 100 곱해줘야 하므로 작업 수행 
    for i in range(len(values)):
        value += values[i] * 10**(3-i)

    return value

## Create_year에서 정의한 함수 활용 내부에서 불러오며 주어진 조건에 맞는 연도가 나올때까지 반복하도록 작성
def Check_year():
    print("\n>> 10각형 주사위를 차례로 4번 던져 0 ~ 9 사이의 숫자를 총 4개를 생성합니다.")

    # 추후에 return 값으로 여태까지 제작한 list를 내보내야 하기 때문에 empty list 제작 
    year_list = []

    # While문을  사용하는 이유는 경우의 수가 무한대이기 때문에 조건을 만족할 때 까지 반복해야하기 때문이다. 
    while True:

        # year값 생셩 
        value = Create_year()

        # 만들어진 year값을 year_list 값에 삽입 
        year_list += [value]

        # 만들어진 year값이 조건에 적합한지 확인하는 구문 
        if value >= 2020 and value <= 2050:

            # 조건을 만족할 시 while문을 빠져나와야 하기 때문에 조건을 만족할 때 break 삽입하여 더이상 반복하지 않도록 작업  
            print(">> 생성된 연도(2020년 ~ 2050년 사이)는 {}입니다.\n".format(value))
            break

    # return으로 현재 만들어진 year 값과 만들어진 year의 값이 전부 들어있는 list까지 내보냄
    return value, year_list

## Worldcup이 개최되는 연도인지 확인하고 다양한 조건을 삽입하는 함수 
def Worldcup_year_check():

    # 앞서 정의한 Check_year 함수를 불러와서 작업을 시작
    ## 불러오는 값은 2020 ~ 2050연도 사이의 연도값과 그동안 제작된 year값이 담긴 list 
    value, value_list = Check_year()

    # 2022, 2026등 4년 주기로 월드컵이 개최되며 4로 나눈 후 2의 나머지를 가지는 연도에 개최되기 때문에 조건을 삽입 0
    if (value) % 4 == 2:

        # Worldcup이 개최될 때 실행되는 구문 삽입 
        print(">> {}년에는 세계컵이 개최됩니다.\n".format(value))
        print(">> 2020년 ~ 2050년 사이의 연도를 찾기 위해 {}개 만큼 다른 연도를 생성했습니다.".format(len(value_list)))
        print(">> 생성하였던 연도들의 리스트는 다음과 같습니다 :{}".format(value_list))

        # 후에 개최 대륙을 찾기 위해 value값을 다시 return 수행 
        return value

    # 월드컵 개최연도가 아닐경우 조건에 대한 구문 작성 
    else:
        print(">> {}년에는 세계컵이 개최되지 않습니다.\n".format(value))

        # Echo Checking 삽입부분 이때 사용자가 잘못 입력 시 뒤의 함수에서 오류가 발생할 수 있기 때문에 제대로된 값을 입력할 때까지 while문 활용 반복
        while True:
            input_value = input(">> 세계컵이 개최되는 년도를 계속 찾으시겠습니까 ? (Y or y, N or n) :")

            # not in 함수 활용하여 주어진 값이 아닌 다른 값을 입력할 때 다시 수행하도록 실행
            if input_value not in ['y','Y','N','n']:
                print("\n>> Y or y or N or n을 입력해 주세요.\n")
                
            # 제대로된 값을 입력할 시 while문에서 빠져나와 작업 수행 
            else:
                break

        # 주어진 조건에서 N, n을 입력시 더 이상 반복을 하지 않는다고 주어졌으므로 프로그램 종료 comment 출력 후 함수에서 빠져나옴
        # 이때 sys.exit() 함수를 활용하면 실행되고 있는 모든 함수에서 빠져 나온다는 의미 프로그램 작동을 종료시키기 때문 
        if input_value == 'n' or input_value == 'N':
            print('\n>> 프로그램을 종료합니다.')
            sys.exit()

        # Y, y를 입력할 시 앞서 작업한 과정을 처음부터 다시 수행하기 때문에 다시 작업 수행하도록 작성     
        if input_value == 'Y' or input_value =='y':
            return Worldcup_year_check()

# Worldcup 개최지역 뽑는 함수
def Worldcup_Area():

    # 앞서 모든 조건에 대하여 만족하도록 작성한 함수를 내부적 삽입
    ## 해당 함수의 value 값으로 삽입되는 것은 모든 조건을 깔끔하게 끝내고 온 월드컵이 개최되는 연도임.
    value = Worldcup_year_check()

    # 월드컵 개최지 list 제작 
    area = ['아시아','유럽','아프리카','남아메리카','북아메리카']

    # 월드컵 개최지의 index에 맞게 작업 수행 개최지는 20년마다 반복되며 주기는 4년
    # 즉 20으로 나누어진 나머지에 4로 나눈 몫의 값이 index값이 됨
    # ex) 2022(아시아개최) -> 2022 % 20 -> 2
    # 2 // 4 -> 0 idx = 0 , area[values] -> '아시아'
    values = value % 20 // 4

    # 만들어진 값과 원래 주어진 연도값을 활용 최종 출력문구 제작 
    print(">> {}년에는 {} 대륙에서 세계컵이 개최될 순서입니다.".format(value,area[values]))
    
# 처음 문구 작성
print("\n>> 2020년 ~ 2050년 사이의 연도를 random으로 생성하고 그 해에 세계컵이 개최되는지 확인합니다. \n  생성된 연도에 세계컵이 개최되는 경우 개최대륙을 출력합니다.")

# Main  함수 정의 
if __name__ == '__main__':
    Worldcup_Area()


