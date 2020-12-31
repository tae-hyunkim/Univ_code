import pickle

'''
Age와 Score가 Int로 인식되게 해야함 -> pickle 사용 
find 명령어, inc 명령어, del 명령어 추가 및 수정  
inc 명령어는 name과 amount 인자를 받음 이때 name의 score에 amount 값 더해줌 -완료 
find 명령어는 name 인자를 받아옴. name과 일치하는 사람만 출력 - 완료
del 명령어 수정 name을 인자로 받아와 주어진 name이 같은 모든 사람 레코드 제거 - 완료
Error 처리를 최대한 진행 try except else 활용 

Error 개선 사항
 1. 필요 인자 개수 선 확인 후 명령어를 실행하도록 수행
 2. age와 Score의 값이 정수가 아닐 경우 에러 출력 
 
'''

dbfilename = 'assinment_3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        print("\n 활용할 수 있는 명령어는 add, del, show, find, inc, quit 입니다. \n")
        inputstr = (input("Score DB > "))

        if inputstr == "": continue

        parse = inputstr.split(" ")

        if parse[0] == 'add':
            # add를 할때 필요한 인자는 총 3개 Name, Age, Score 
            
            # add를 할 때 4개의 인자를 입력하지 않았을 경우 
            if len(parse) != 4:
                print("입력하신 값에 오류가 존재합니다.")
                print("필요한 인자는 총 4개로 명령어, Name, Age, Score 입니다.")
                print("입력하신 인자의 개수는 총 {}개 입니다.".format(len(parse)))
                continue
            
            # Age와 Score의 값을 정수로 삽입하지 않았을 경우 예외처리 
            try :
                parse[2] = int(parse[2])
            except:
                print("Age 인자가 정수가 아닙니다.")
                continue

            try :
                parse[3] = int(parse[3])
            except:
                print("Score 인자가 정수가 아닙니다.")
                continue

            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]

        # 9월 16일 좀더 진행해보자 일단 킵 
        elif parse[0] == 'del':
            # 수정사항: name이 같은 모든 사람 제거하게 코드를 수정 
            # 원래 있던 remove 활용 시 중간중간 삭제가 안되는 문제 발생 
            # 원인 파악 결과 하나씩 지워가는 과정에서 앞으로 당겨지면서 발생하는 문제 -> Index 번호를 먼저 가져오고 역순으로 지우기 시작하여 문제를 해결 
            if len(parse) != 2:
                print("정확한 인자의 수를 입력해 주세요.")
                continue
            
            # Name에 입력한 값이 있는 Index 추출

            idx = []
            for i,p in enumerate(scdb):
                if p['Name'] == parse[1]:
                    idx += [i]

            for i,p in sorted(enumerate(scdb),reverse=True):
                if i in idx:
                    scdb.remove(p)   

        elif parse[0] == 'show':
            # 수정사항 없음 
            if len(parse) > 2:
                print("불필요한 인자가 포함되어 있습니다.")
                continue
            
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'inc':
            if len(parse) != 3:
                print("인자의 개수가 잘못 되었습니다. inc 명령어에 필요한 인자는 이름, 숫자 입니다.")
                continue
            try:
                parse[2] = int(parse[2])
            except:
                print("추가하고자 하는 값이 정수가 아닙니다.")
                continue
            
            for p in scdb:
                if p['Name'] == parse[1]:
                    p['Score'] += parse[2]
            print("\n작업을 완료 하였습니다.\n")

        elif parse[0] == 'find':
            if len(parse) != 2:
                print("\n필요한 인자의 개수가 잘못되었습니다. find 명령어에 필요한 인자는 이름 입니다.")
                continue

            for p in scdb:
                if p['Name'] == parse[1]:
                    for attr in p:
                        print(attr + "=" + str(p[attr]), end=' ')
                    print()

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)