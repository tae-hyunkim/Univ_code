import turtle
import random


# 원의 반지름 추출을 위한 class 정의 부분 
class Radius:

    # Radius의 생성자 부분 define class에 내장된 함수를 활용해 최대한 간단히 작업을 진행하도록 함. 
    def __init__(self,debugging):
        self.D = debugging
        
        self.radi_Length = self.randomNumber()
        print(">> 결정된 반지름 : {} \n".format(self.radi_Length))

        self.num = self.NumberCheck()
        if self.D:
            print("입력된 전진을 위한 값은 {}입니다.".format(self.num))
            
    # 주사위를 던져 1~6사이의 값을 내보내는 함수 
    def randomNumber(self):
        print(">> 반지름을 주사위를 던져 1~6 까지의 하나의 숫자를 받아들입니다.")
        return random.randint(1,6) * 10

    # 내보낸 수를 활용해 해당 수의 3배 이상인지 확인하는 함수
    def NumberCheck(self):
        # num은 0을 쓴 이유는 self.radi_Length의 값이 10 20 30 40 50 60이기 때문이다. 
        num = 0
        print(">> turtle이 앞으로 진행할 길이에 해당하는 값을 입력, \n   결정된 반지름의 3배이상 값이어야 합니다.")
        # 입력한 값이 미리 정의된 반지름의 3배 이상이 될때까지 반복하도록 실행 
        while num < 3*self.radi_Length:

            # 이 구문을 활용해 처음 실행 시 해당 print문이 실행 안되도록 작업 
            if num != 0:
                print(">> {} 보다 3배이상의 값을 입력하세요".format(self.radi_Length))
            
            num = int(input(">>>길이 :"))
            print(">>입력된 길이 : {}\n".format(num))
                      
        return num
                
# Turtle 그래픽을 통해 그림 그리는 Class 구문 앞서 정의한 Radius함수를 상속받음 
class turtle_graphic(Radius):

    # Radius에서 정의된 radi_Length값과 num값을 상속받기 위해 super().__init__() 활용
    # 나머지 생성자들은 추후 작업에서 사용하기 위해 미리 define 
    def __init__(self,debug):
        super().__init__(debug)
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.labeling = ['첫번','두번','세번']
        self.Checking = ['6각형','5각형']

        if self.D:
            print("상속받은 값은 다음과 같습니다. 반지름 : {}, 전진거리 : {}".format(self.radi_Length,self.num))
            
    # 그림을 최종적으로 그리는 함수 define 
    def drawing(self):
        
        # 함수 선언시 1~6사이의 숫자를 받아와 작업을 시행 
        Number = random.randint(1,6)
        if self.D:
            print("두번째 주사위를 굴린 결과는 다음과 같습니다. {}".format(Number))
        # 총 3번의 그림을 그릴 예정이며 해당 그림에 따라 다른 작업을 수행하기 위해 시행
        for i in range(0,3):
            
            # drawPicture 함수를 활용 첫번째 그림인지 구분짓는 인자와 홀수 짝수 구분을 위한 값 삽입 
            self.drawPicture(Number,i)
            
            if i < 2:
                print("\n>> {}째 원에서는 {}을 그렸습니다. {}째 원에서는 {}을 그립니다.".format(
                    self.labeling[i],self.Checking[Number%2],self.labeling[i+1],self.Checking[(Number+1)%2]))
            Number += 1

                
    def drawPicture(self,number,count):

        # 원 그리기 
        self.t.circle(self.radi_Length)

        # 들어오는 count값이 0이면 처음 그리는 그림이기 때문에 print문 출력 아니면 그림 그리기
        if count <1:
            if number % 2 == 0:
                print("\n>> 선택된값이 짝수입니다. 첫번째 원내에 6각형을 그립니다.")
                self.t.circle(self.radi_Length,steps=6)
            else:
                print("\n>> 선택된값이 홀수입니다. 첫번째 원내에 5각형을 그립니다.")
                self.t.circle(self.radi_Length,steps=5)
        else:
            
            if number % 2 == 0:
                self.t.circle(self.radi_Length,steps=6)
            else:
                self.t.circle(self.radi_Length,steps=5)

        # point 전진시킴 
        self.t.forward(self.num)
        
        # 반지름 1.2배 증가
        
        if self.D:
            print('\n현재 반지름의 길이 :{}'.format(self.radi_Length))
        self.radi_Length *= 1.2

def debug():
    debug = input("디버깅 유무를 입력해 주세요 (Y or n / N or n):")
    while True:
        if debug == 'Y' or debug =='y':
            return True
            break
        elif debug == 'N' or debug =='n':
            return False
            break
        else:
            debug = input(" 제대로된 값을 입력해 주세요 (Y or n / N or n)")
        
def main():
    bug = debug()
    # class Loading
    Class = turtle_graphic(bug)
    # Drawing 
    Class.drawing()

main()
