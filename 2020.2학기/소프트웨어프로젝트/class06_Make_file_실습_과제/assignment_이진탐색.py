# 이진탐색의 재귀적 구현 
## 코드 구조를 뜯어보면 처음 입력받은 사이즈의 리시트에서 다음 입력받은 갯수의 Target 값을 가지지 않은 값의 개수를 찾는 과정 
'''
 재귀함수를 1000번 이상 사용하면 maximum recursion depth exceeded in comparison 이라는 오류가 발생한다.
 이 에러를 해결하기 위해서 우리는 재귀를 1000번 이상 하여도 상관 없도록 만들어 주어야 한다.
 이때 sys 패키지에 존재하는 setrecursionlimit를 풀어주면 된다. 
 내 노트북 사양으로는 약 3800번 반복까지만 되고 나머진 되지 않는다. 
'''
import time
import random

import sys
sys.setrecursionlimit(10000)

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

'''
 함수를 만들 때 함수를 해석해 보면 리스트의 있는 값 하나 하나를 target과 비교해서 작업한다는 사실을 알 수 있음
 함수를 만들때 다음과 같은 과정을 반복할 예정
  1. 리스트 마지막 값과 target값 비교를 통해 같으면 1 반환 
  2. last index 값이 0이면 -1을 반환
  3. 위의 조건을 만족 X -> 재귀함수를 활용 last index에 -1을 해주어 작업을 진행
'''

def recbinsearch(L, l, u, target):
    if L[u-1] == target: 
        return 1
    if u-1 == l:
        return -1
    return recbinsearch(L,l,u-1,target)

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
tss = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, tss))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
tts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, tts))

print("\n탐색 과정을 반복하여 {0}번을 비교해본 결과 재귀함수 사용시 약 {1:.5f} 이진 탐색시 약{2:.5f}초가 걸린다.".format(len(numbers),tss,tts))
print("이를 토대로 우리는 재귀함수보다 이진탐색의 연산복잡도가 더 낮고 훨씬 효율적 사용이 가능하다는 사실을 알 수 있다.")