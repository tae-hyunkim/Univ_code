## 필요한 정보 아이템정보, 시작강화수치, 스타캐치 유무, 파괴방지 정보, MVP 등급, PC방, sunday메이플 
# return 값들 -> 성공확률, 실패확률, 파괴확률, 필요한 메소량 정보 
# 스타캐치의 추가확률 경우 곱연산을 적용해 활용 자료출처 http://www.inven.co.kr/board/maple/2304/19474
import random 

class StarCatch:
    def __init__(self, item_level = 150, reinforce = 0, starcatch = False, destroy = False, MVP = 0,PCroom = False, sunday = False):
        self.level = item_level
        self.reinforce = reinforce
        self.starcatch = starcatch
        self.destroy = destroy
        self.destroy_num = 0
        self.mvp = MVP
        self.currentfail = 0
        self.PCroom = PCroom
        self.sunday = sunday
        self.total_Meso = 0
        self.success = 0
        self.destruction = 0
        self.fail_prob = 0

        
    # 강화에 필요한 메소 함수 
    def need_Meso(self):
        # Base 강화비용 계산
        sales = 0

        if self.reinforce < 10:
            Meso =  int(round((1000 + (self.level**3)*(self.reinforce+1)/25),-2))
        elif self.reinforce < 15:
            Meso = int(round((1000 + (self.level**3)*((self.reinforce+1)**2.7)/400),-2))
        else:
            Meso = int(round((1000 + (self.level**3)*((self.reinforce+1)**2.7)/200),-2))
        
        # mvp 등급별 할인 
        if self.mvp == 'silver' and self.reinforce <= 17:
            sales = 0.03
        elif self.mvp == 'gold' and self.reinforce <= 17:
            sales = 0.05
        elif (self.mvp == 'diamond' or self.mvp == 'red') and self.reinforce <= 17:
            sales = 0.1
        
        # PC방에서 강화시 5% 추가할인
        if self.PCroom:
            sales += 0.05
        
        # sundayMaple 이벤트시 30% 곱연산 깍아줌 
        if self.sunday:
            Meso = int(Meso * (1 - sales) * 0.7)

        # 파괴방지 버튼 클릭시 메소 2배 
        if self.destroy > 11 and self.destroy < 17 and self.destroy:
            Meso = Meso * 2

        return Meso 

    # 강화 성공확률 return 
    def enhance_Proba(self):

        if self.reinforce < 3:
            return 0.95-0.05*self.reinforce
        elif self.reinforce < 10:
            return 1-0.05*self.reinforce
        elif self.reinforce <12:
            return 0.55 - 0.1*(self.reinforce - 9)
        elif self.reinforce<22:
            return 0.3
        elif self.reinforce == 22:
            return 0.03
        elif self.reinforce == 23:
            return 0.02
        elif self.reinforce == 24:
            return 0.01

    # 강화시도시 터지는 확률 계산 함수 
    def destroy_proba(self):
        
        # 파괴방지 버튼 클릭시 17성까지는 터지는 확률 0 
        if self.reinforce < 18 and self.destroy:
            return 0

        if self.reinforce < 12:
            return 0
        elif self.reinforce<13:
            return 0.009
        elif self.reinforce<14:
            return 0.019
        elif self.reinforce<18:
            return 0.03
        elif self.reinforce<20:
            return 0.04
        elif self.reinforce<22:
            return 0.1
        elif self.reinforce==22:
            return 0.2
        elif self.reinforce==23:
            return 0.3
        elif self.reinforce==24:
            return 0.4

    def probabilty(self):
        self.success = self.enhance_Proba()

        if self.starcatch:
            self.success *= 1.0572

        if self.currentfail == 2:
            self.currentfail = 0
            self.success = 1

        self.success = round(self.success,4)
        self.destruction = round((1 - self.success) * self.destroy_proba(),4)
        self.fail_prob = round(1 - self.success - self.destruction,4)

    def enhance(self):
        
        self.probabilty()
        prob = random.random()
        self.total_Meso += self.need_Meso()

        # 성공 
        if prob < self.success:
            self.currentfail = 0
            self.reinforce += 1
            return 0

        # 파괴
        elif 1-self.destroy < prob:
            self.destroy_num += 1
            self.reinforce = 12 
            return 2

        # 실패
        else:
            if self.reinforce > 9:
                if self.reinforce % 5 == 0:
                    self.currentfail = 0
                    pass
                else:
                    self.reinforce -= 1
                    self.currentfail += 1 
            return 1

if __name__ == '__main__':

    item = StarCatch(160,18,False,False,'silver',False,False)
    print("\n{}제 아이템 스타캐치 프로그램입니다.\n parameter는\n item_level \t 현재강화 \t 스타캐치유무 \t 파괴방지유무 \n MVP등급 (Normal, bronz, silver, gold, Diamod, red) \n PC방 유무 \t 선데이메이플유무\n 입니다.\n".format(item.level))
    
    lis = ['성공','실패','터짐']

    print("\n\n 시작 강화 수치 : {}\n".format(item.reinforce))
    for i in range(20):
        a = item.enhance()
        print("강화 결과 : {}".format(lis[a]))
        print("성공 확률 : {} \n 실패확률 : {} \n 파괴확률 : {}".format(item.success, item.fail_prob,item.destruction))
        print('현재강화 수치 : {}'.format(item.reinforce))
        print("사용한 메소 총량: {} \n".format(item.total_Meso))
        
        