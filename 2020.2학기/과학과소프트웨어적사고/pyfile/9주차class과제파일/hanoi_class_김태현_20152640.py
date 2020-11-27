class Hanoi:

    def __init__(self):
        pass 
    
    def hanoi(self,n,start,mid,end):
        if n == 1:
            print("%d : %c -> %c" %(n,start,end))

        else:
            self.hanoi(n-1,start,end,mid)
            print("%d : %c -> %c" %(n,start,end))

            self.hanoi(n-1,mid,start,end)


def main():
    n = int(input('>> 하노이 타워의 개수를 입력해 주세요:'))

    game = Hanoi()

    game.hanoi(n,'A','B','C')


main()
