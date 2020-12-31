import sys
import random
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QPixmap
from Upgrader import *
from Calculator import *
from numToStr import *

class Sim_GUI(Upgrader):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected = True
        self.upgraded = 0
    
    def initUI(self):
        # 위쪽 레이아웃에 들어갈 위젯들 설정
        topLayout = QHBoxLayout()
        level = QLabel("레벨 : ", self)                             # 3가지 레벨제한의 무기중 1개 선택
        self.selectedLevel = QComboBox()
        self.selectedLevel.addItem("150")
        self.selectedLevel.addItem("160")
        self.selectedLevel.addItem("200")
        levelButton = QPushButton("선택")

        nowStarLabel = QLabel("시작 강화 등급 : ", self)            # 강화를 시작하는 등급을 지정
        self.nowStar = QLineEdit()
        self.nowStar.setAlignment(Qt.AlignCenter)
        self.nowStar.setPlaceholderText("(0 ~ 24)")
        self.nowStar.setValidator(QIntValidator(0, 24, self))
        self.nowStar.setReadOnly(False)
        emptyPlace = QLabel(" ", self)
        
        reset = QPushButton("초기화")                               # 현재까지의 데이터를 초기화하는 버튼 추가

        topLayout.addStretch(1)                                     # 위젯들을 레이아웃에 추가함
        topLayout.addWidget(level)
        topLayout.addWidget(self.selectedLevel)
        topLayout.addWidget(levelButton)
        topLayout.addWidget(emptyPlace)
        topLayout.addWidget(nowStarLabel)
        topLayout.addWidget(self.nowStar)
        topLayout.addWidget(reset)
        topLayout.addStretch(1)
        
        # 왼쪽 레이아웃(직접 1회씩 강화 시뮬레이션을 하는 부분)에 들어갈 위젯들을 작성
        gb1 = QGroupBox(self)                                       # 그룹박스를 통해 가시성 상승
        gb1.setTitle("강화 기능")

        countUpgradeLabel = QLabel("시도 횟수 : ", self)            # 현재까지 강화를 시도한 횟수 표시
        self.countUpgrade = QLineEdit("0")
        self.countUpgrade.setAlignment(Qt.AlignCenter)
        self.countUpgrade.setReadOnly(True)

        countDestroyedLabel = QLabel("파괴 횟수 : ", self)          # 현재까지 강화 도중 장비가 파괴된 횟수 표시
        self.countDestroyed = QLineEdit("0")
        self.countDestroyed.setAlignment(Qt.AlignCenter)
        self.countDestroyed.setReadOnly(True)

        self.weapons = {"150":"./img/150.png", "160":"./img/160.png", "200":"./img/200.png", "Default":"./img/default.png"}
        self.weaponImage = QPixmap()                                # 레벨 제한에 따른 무기의 이미지 표시
        self.weaponImage.load(self.weapons["Default"])
        self.weaponImage = self.weaponImage.scaled(150, 150)
        self.displayImage = QLabel()
        self.displayImage.setPixmap(self.weaponImage)

        self.currentInfo = QTextEdit()                              # 이번 강화에 대한 정보를 알려줄 공간
        self.currentInfo.setReadOnly(True)

        self.upgradeHistory = QScrollArea()                         # 지금까지의 강화 결과들을 표시
        self.historyMessage = "[강화 내역]"
        self.historyLabel = QLabel(self.historyMessage)
        self.upgradeHistory.setWidget(self.historyLabel)

        needMesoLabel = QLabel("필요한 메소 : ", self)              # 이번 강화를 위해 필요한 재화(메소)량을 표시
        self.needMeso = QLineEdit()
        self.needMeso.setAlignment(Qt.AlignRight)
        self.needMeso.setReadOnly(True)

        usedMesoLabel = QLabel("사용한 메소 : ", self)              # 현재까지 강화를 통해 소비한 재화(메소)량을 표시
        self.usedMeso = QLineEdit()
        self.usedMeso.setAlignment(Qt.AlignRight)
        self.usedMeso.setReadOnly(True)

        upgrade = QPushButton("강화")                               # 강화를 시도할 강화 버튼 추가

        # 왼쪽 레이아웃에 위젯들을 추가
        leftLayout = QGridLayout()                                  # 그룹박스에 레이아웃 삽입
        gb1.setLayout(leftLayout)

        self.starLine1 = QHBoxLayout()                              # 현재까지의 강화 수치를 별 이미지를 통해 표시
        self.starLine2 = QHBoxLayout()
        emptyPlace = QLabel(" ", self)
        self.statusinfo = {0:"./img/graystar.png", 1:"./img/yellowstar.png"}
        self.starstatus = [0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0]
        self.star = [QLabel(), QLabel(), QLabel(), QLabel(), QLabel(),
                     QLabel(), QLabel(), QLabel(), QLabel(), QLabel(),
                     QLabel(), QLabel(), QLabel(), QLabel(), QLabel(),
                     QLabel(), QLabel(), QLabel(), QLabel(), QLabel(),
                     QLabel(), QLabel(), QLabel(), QLabel(), QLabel()]
        self.starLine1.addStretch(1)
        for i in range(15):
            tmpstar = QPixmap()
            tmpstar.load(self.statusinfo[self.starstatus[i]])
            tmpstar = tmpstar.scaled(15, 15)
            self.star[i].setPixmap(tmpstar)
            self.starLine1.addWidget(self.star[i])
            if i%5==4:
                self.starLine1.addWidget(emptyPlace)
        self.starLine1.addStretch(1)
        self.starLine2.addStretch(1)
        for i in range(15, 25):
            tmpstar = QPixmap()
            tmpstar.load(self.statusinfo[self.starstatus[i]])
            tmpstar = tmpstar.scaled(15, 15)
            self.star[i].setPixmap(tmpstar)
            self.starLine2.addWidget(self.star[i])
            if i%5==4:
                self.starLine2.addWidget(emptyPlace)
        self.starLine2.addStretch(1)

        leftLayout.addLayout(self.starLine1, 0, 0, 1, 17)           # 별을 표시하는 레이아웃을 강화 기능 레이아웃에 추가
        leftLayout.addLayout(self.starLine2, 1, 0, 1, 17)

        leftLayout.addWidget(countUpgradeLabel, 2, 1, 1, 2, Qt.AlignRight)    # 강화 시도 횟수 위젯을 레이아웃에 추가
        leftLayout.addWidget(self.countUpgrade, 2, 3, 1, 2)
        leftLayout.addWidget(countDestroyedLabel, 2, 8, 1, 4, Qt.AlignRight)  # 파괴 횟수 위젯을 레이아웃에 추가
        leftLayout.addWidget(self.countDestroyed, 2, 12, 1, 3)

        leftLayout.addWidget(self.displayImage, 3, 1, 2, 3)         # 무기 이미지를 표시하는 위젯 추가
        leftLayout.addWidget(self.currentInfo, 3, 5, 1, 10)         # 현재 강화 정보와 히스토리 위젯 추가
        leftLayout.addWidget(self.upgradeHistory, 4, 5, 1, 10)

        leftLayout.addWidget(needMesoLabel, 5, 1, 1, 1)             # 이번 강화시 필요한 메소량을 레이아웃에 추가
        leftLayout.addWidget(self.needMeso, 5, 2, 1, 13)
        leftLayout.addWidget(usedMesoLabel, 6, 1, 1, 1)             # 총 사용 메소량 위젯을 레이아웃에 추가
        leftLayout.addWidget(self.usedMeso, 6, 2, 1, 13)

        leftLayout.addWidget(upgrade, 7, 4, 1, 8)                   # 업그레이드 버튼을 레이아웃에 추가

        # 오른쪽 레이아웃(여러 횟수를 자동으로 시뮬레이션하여 평균적인 기댓값 산출하는 부분)에 들어갈 위젯들을 작성
        gb2 = QGroupBox(self)                                       # 그룹박스를 통한 가시성 상승 2
        gb2.setTitle("시뮬레이션 기능")

        toStarsLabel = QLabel("목표 수치 : ", self)                 # 목표로 하는 강화 수치
        self.toStars = QLineEdit()
        self.toStars.setAlignment(Qt.AlignCenter)
        self.toStars.setPlaceholderText("(0 ~ 25)")
        self.toStars.setValidator(QIntValidator(0, 25, self))

        tryNumsLabel = QLabel("시도 횟수 : ", self)                 # 시작 수치부터 목표 수치까지 몇번 도달시킬지를 결정
        self.tryNums = QLineEdit()
        self.tryNums.setAlignment(Qt.AlignCenter)
        self.tryNums.setPlaceholderText("(1 ~ 10,000)")
        self.tryNums.setValidator(QIntValidator(1, 10000, self))

        startSimulationButton = QPushButton("시뮬레이션 시작")      # 버튼을 누르면 시뮬레이션이 시작됨

        averageUsedMesoLabel = QLabel("평균 사용 메소 : ", self)    # 시도 횟수동안의 평균 사용 메소량
        self.averageUsedMeso = QLineEdit()
        self.averageUsedMeso.setAlignment(Qt.AlignRight)
        self.averageUsedMeso.setReadOnly(True)

        minUsedMesoLabel = QLabel("최소 사용 메소 : ", self)        # 시도 횟수동안의 최소 사용 메소량
        self.minUsedMeso = QLineEdit()
        self.minUsedMeso.setAlignment(Qt.AlignRight)
        self.minUsedMeso.setReadOnly(True)

        maxUsedMesoLabel = QLabel("최대 사용 메소 : ", self)        # 시도 횟수동안의 최대 사용 메소량
        self.maxUsedMeso = QLineEdit()
        self.maxUsedMeso.setAlignment(Qt.AlignRight)
        self.maxUsedMeso.setReadOnly(True)

        averageTriedNumLabel = QLabel("평균 시도 횟수 : ", self)    # 시도 횟수동안의 평균 시도 횟수
        self.averageTriedNum = QLineEdit()
        self.averageTriedNum.setAlignment(Qt.AlignRight)
        self.averageTriedNum.setReadOnly(True)

        minTriedNumLabel = QLabel("최소 시도 횟수 : ", self)        # 시도 횟수동안의 최소 시도 횟수
        self.minTriedNum = QLineEdit()
        self.minTriedNum.setAlignment(Qt.AlignRight)
        self.minTriedNum.setReadOnly(True)

        maxTriedNumLabel = QLabel("최대 시도 횟수 : ", self)        # 시도 횟수동안의 최대 시도 횟수
        self.maxTriedNum = QLineEdit()
        self.maxTriedNum.setAlignment(Qt.AlignRight)
        self.maxTriedNum.setReadOnly(True)

        averageDestroyedNumLabel = QLabel("평균 파괴 횟수 : ", self) # 시도 횟수동안의 평균 파괴 횟수
        self.averageDestroyedNum = QLineEdit()
        self.averageDestroyedNum.setAlignment(Qt.AlignRight)
        self.averageDestroyedNum.setReadOnly(True)

        minDestroyedNumLabel = QLabel("최소 파괴 횟수 : ", self)    # 시도 횟수동안의 최소 파괴 횟수
        self.minDestroyedNum = QLineEdit()
        self.minDestroyedNum.setAlignment(Qt.AlignRight)
        self.minDestroyedNum.setReadOnly(True)

        maxDestroyedNumLabel = QLabel("최대 파괴 횟수 : ", self)    # 시도 횟수동안의 최대 파괴 횟수
        self.maxDestroyedNum = QLineEdit()
        self.maxDestroyedNum.setAlignment(Qt.AlignRight)
        self.maxDestroyedNum.setReadOnly(True)

        # 오른쪽 레이아웃에 위젯들을 추가
        rightLayout = QGridLayout()                                 # 그룹박스에 레이아웃 삽입
        gb2.setLayout(rightLayout)

        gb2_1 = QGroupBox(self)                                     # 그룹박스 내에서 역할에 따른 추가 그룹박스 생성
        gb2_1.setTitle("초기값 설정")                               # 초기 필요한 설정값 구역

        setLayout = QGridLayout()                                   # 목표 강화 수치, 시도 횟수를 그룹박스에 추가
        gb2_1.setLayout(setLayout)
        setLayout.addWidget(toStarsLabel, 0, 0, 1, 2, Qt.AlignRight)
        setLayout.addWidget(self.toStars, 0, 2, 1, 1)
        setLayout.addWidget(tryNumsLabel, 1, 0, 1, 2, Qt.AlignRight)
        setLayout.addWidget(self.tryNums, 1, 2, 1, 1)
        setLayout.addWidget(startSimulationButton, 0, 3, 1, 2)

        gb2_2 = QGroupBox(self)                                     # 메소와 관련된 위젯 구역
        gb2_2.setTitle("메소 사용량")

        mesoLayout = QGridLayout()                                  # 평균, 최소, 최대 메소 사용량을 그룹박스에 추가
        gb2_2.setLayout(mesoLayout)
        mesoLayout.addWidget(averageUsedMesoLabel, 0, 0, 1, 2, Qt.AlignRight)
        mesoLayout.addWidget(self.averageUsedMeso, 0, 2, 1, 1)

        mesoLayout.addWidget(minUsedMesoLabel, 1, 0, 1, 2, Qt.AlignRight)
        mesoLayout.addWidget(self.minUsedMeso, 1, 2, 1, 1)

        mesoLayout.addWidget(maxUsedMesoLabel, 2, 0, 1, 2, Qt.AlignRight)
        mesoLayout.addWidget(self.maxUsedMeso, 2, 2, 1, 1)

        gb2_3 = QGroupBox(self)                                     # 시도 횟수와 관련된 위젯 구역
        gb2_3.setTitle("시도 횟수")

        tryLayout = QGridLayout()                                   # 평균, 최소, 최대 시도 횟수를 그룹박스에 추가
        gb2_3.setLayout(tryLayout)
        tryLayout.addWidget(averageTriedNumLabel, 0, 0, 1, 2, Qt.AlignRight)
        tryLayout.addWidget(self.averageTriedNum, 0, 2, 1, 1)

        tryLayout.addWidget(minTriedNumLabel, 1, 0, 1, 2, Qt.AlignRight)
        tryLayout.addWidget(self.minTriedNum, 1, 2, 1, 1)

        tryLayout.addWidget(maxTriedNumLabel, 2, 0, 1, 2, Qt.AlignRight)
        tryLayout.addWidget(self.maxTriedNum, 2, 2, 1, 1)

        gb2_4 = QGroupBox(self)                                     # 파괴 횟수와 관련된 위젯 구역
        gb2_4.setTitle("파괴 횟수")

        destroyLayout = QGridLayout()                               # 평균, 최소, 최대 파괴 횟수를 그룹박스에 추가
        gb2_4.setLayout(destroyLayout)
        destroyLayout.addWidget(averageDestroyedNumLabel, 0, 0, 1, 2, Qt.AlignRight)
        destroyLayout.addWidget(self.averageDestroyedNum, 0, 2, 1, 1)

        destroyLayout.addWidget(minDestroyedNumLabel, 1, 0, 1, 2, Qt.AlignRight)
        destroyLayout.addWidget(self.minDestroyedNum, 1, 2, 1, 1)

        destroyLayout.addWidget(maxDestroyedNumLabel, 2, 0, 1, 2, Qt.AlignRight)
        destroyLayout.addWidget(self.maxDestroyedNum, 2, 2, 1, 1)

        rightLayout.addWidget(gb2_1, 0, 0, 1, 2)                    # 총 생성된 그룹박스들을 하나로 묶음
        rightLayout.addWidget(gb2_2, 1, 0, 1, 1)
        rightLayout.addWidget(gb2_3, 1, 1, 1, 1)
        rightLayout.addWidget(gb2_4, 2, 0, 1, 1)

        # 탭 구분
        tabs = QTabWidget()                                         # 강화 기능과 시뮬레이션 기능을 탭을 통해 구분하여
        tabUp = QWidget()                                           # 보다 깔끔한 인터페이스 생성
        tabSim = QWidget()

        tabs.addTab(tabUp, "강화창")
        tabs.addTab(tabSim, "시뮬레이션")

        tabUp.layout = QVBoxLayout(self)
        tabUp.layout.addWidget(gb1)
        tabUp.setLayout(tabUp.layout)

        tabSim.layout = QVBoxLayout(self)
        tabSim.layout.addWidget(gb2)
        tabSim.setLayout(tabSim.layout)

        # 좌우측 레이아웃을 통합
        
        mainLayout = QGridLayout()                                  # 전체적인 레이아웃 생성

        mainLayout.addLayout(topLayout, 0, 0, 1, 2)

        mainLayout.addWidget(tabs, 1, 0, 1, 1)

        #버튼 클릭 이벤트
        levelButton.clicked.connect(self.buttonclicked)
        upgrade.clicked.connect(self.buttonclicked)
        reset.clicked.connect(self.buttonclicked)
        startSimulationButton.clicked.connect(self.buttonclicked)

        # 레이아웃의 크기를 고정하고, 윈도우의 이름 정의
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(mainLayout)
        self.setWindowTitle("Starforce Simulator")
    
    def buttonclicked(self):                                        # 버튼이 클릭됐을 때의 기능
        sender= self.sender()
        if sender.text() == "선택":                                 # 무기 레벨제 선택시
            if self.nowStar.text() == "":                           # 에러 방지
                return
            if self.selected:                                       # 아직 선택이 안돼있는 상태일 경우 선택하고 초기값 설정
                self.selected = False                               # 이미 선택이 돼있는 경우 초기화 전까지 변경 불가능
                self.weaponImage.load(self.weapons[self.selectedLevel.currentText()])
                self.weaponImage = self.weaponImage.scaled(150, 150)
                self.displayImage.setPixmap(self.weaponImage)
                self.needMeso.setText(norToAbnor(str(calcMeso(self.upgraded, self.selectedLevel.currentText()))))
                self.usedMeso.setText("0")
                self.upgraded = int(self.nowStar.text())
                self.showUpgradeIndex(self.upgraded)
                self.nowStar.setReadOnly(True)
                self.checkStars()
                self.show()
        elif self.selected == False:                                # 선택이 됐을 경우 강화나 초기화 기능 사용 가능
            if sender.text() == "강화":                             # 강화 기능
                prevStar = self.upgraded
                nextStar = self.doUpgrade(prevStar)
                self.usedMeso.setText(norToAbnor(str(int(abnorToNor(self.usedMeso.text()))+int(abnorToNor(self.needMeso.text())))))
                self.countUpgrade.setText(norToAbnor(str(int(abnorToNor(self.countUpgrade.text()))+1)))
                if nextStar == "-1":                                # 파괴되었을 경우
                    self.historyMessage += "\n*파괴됨* : "+str(prevStar)+" --> 12"
                    self.historyLabel = QLabel(self.historyMessage)
                    self.upgradeHistory.setWidget(self.historyLabel)
                    self.upgraded = 12
                    self.countDestroyed.setText(abnorToNor(str(int(self.countDestroyed.text())+1)))
                else:                                               # 실패 or 성공했을 경우
                    if prevStar < int(nextStar):
                        self.historyMessage += "\n*강화 성공* : "+str(prevStar)+" --> "+nextStar
                        self.historyLabel = QLabel(self.historyMessage)
                        self.upgradeHistory.setWidget(self.historyLabel)
                        vbar = self.upgradeHistory.verticalScrollBar()
                        vbar.setValue(vbar.maximum())
                    elif prevStar > int(nextStar):
                        self.historyMessage += "\n강화 실패(하락) : "+str(prevStar)+" --> "+nextStar
                        self.historyLabel = QLabel(self.historyMessage)
                        self.upgradeHistory.setWidget(self.historyLabel)
                        vbar = self.upgradeHistory.verticalScrollBar()
                        vbar.setValue(vbar.maximum())
                    else:
                        self.historyMessage += "\n강화 실패(유지) : "+str(prevStar)+" --> "+nextStar
                        self.historyLabel = QLabel(self.historyMessage)
                        self.upgradeHistory.setWidget(self.historyLabel)
                        vbar = self.upgradeHistory.verticalScrollBar()
                        vbar.setValue(vbar.maximum())
                    self.upgraded = int(nextStar)
                self.showUpgradeIndex(self.upgraded)
                self.needMeso.setText(norToAbnor(str(calcMeso(self.upgraded, self.selectedLevel.currentText()))))
                self.checkStars()
                self.show()
            elif sender.text() == "초기화":                         # 초기화 버튼을 선택했을 경우
                self.selected = True
                self.needMeso.clear()
                self.usedMeso.clear()
                self.nowStar.clear()
                self.countUpgrade.setText("0")
                self.countDestroyed.setText("0")
                self.currentInfo.clear()
                self.weaponImage.load(self.weapons["Default"])
                self.weaponImage = self.weaponImage.scaled(150, 150)
                self.displayImage.setPixmap(self.weaponImage)
                self.nowStar.setReadOnly(False)
                self.checkStars()
                self.show()
        # 무기레벨 설정이 시뮬레이션 구역과는 동떨어져있으므로 혼선을 방지하기 위해 위 if-elif-else문에 포함시키지 않고 독립적으로 생성함
        if sender.text() == "시뮬레이션 시작":
            if self.selected == True:                               # 에러 방지
                pass
            elif ((self.toStars.text() == "") or (self.tryNums.text() == "")):
                pass
            else:                                                   # 시뮬레이션 실행
                minMeso = 0                                         # 평균, 최소, 최대 메소
                maxMeso = 0
                sumMeso = 0
                
                minTry = 0                                          # 평균, 최소, 최대 시도 횟수
                maxTry = 0
                sumTry = 0
                
                minDestroy = 0                                      # 평균, 최소, 최대 파괴 횟수
                maxDestroy = 0
                sumDestroy = 0
                
                for i in range(int(self.tryNums.text())):           # 입력된 값만큼 시도함
                    startStar = int(self.nowStar.text())
                    toStar = int(self.toStars.text())
                    currentStar = startStar
                    currentMeso = 0
                    currentTry = 0
                    currentDestroy = 0
                    while currentStar < toStar:                     # 목표 강화 수치에 도달하는 것이 한번임
                        currentMeso += calcMeso(currentStar, self.selectedLevel.currentText())
                        nextStar = self.doUpgrade(currentStar)
                        currentTry += 1
                        if nextStar == "-1":
                            currentStar = 12
                            currentDestroy += 1
                        else:
                            currentStar = int(nextStar)
                    if currentMeso > maxMeso:                       # 최소, 최댓값 체크
                        maxMeso = currentMeso
                    if currentMeso < minMeso or minMeso == 0:
                        minMeso = currentMeso
                    if currentTry > maxTry:
                        maxTry = currentTry
                    if currentTry < minTry or minTry == 0:
                        minTry = currentTry
                    if currentDestroy > maxDestroy:
                        maxDestroy = currentDestroy
                    if currentDestroy < minDestroy or minDestroy == 0:
                        minDestroy = currentDestroy
                    sumMeso += currentMeso                          # 평균값 계산을 위한 총합 저장
                    sumTry += currentTry
                    sumDestroy += currentDestroy
                sumMeso = int(sumMeso / int(self.tryNums.text()))   # 평균값 계산
                sumTry = int(sumTry / int(self.tryNums.text()))
                sumDestroy = int(sumDestroy / int(self.tryNums.text()))
                self.maxUsedMeso.setText(norToAbnor(str(maxMeso)))  # 표시 값 변경
                self.minUsedMeso.setText(norToAbnor(str(minMeso)))
                self.averageUsedMeso.setText(norToAbnor(str(sumMeso)))
                self.maxTriedNum.setText(norToAbnor(str(maxTry)))
                self.minTriedNum.setText(norToAbnor(str(minTry)))
                self.averageTriedNum.setText(norToAbnor(str(sumTry)))
                self.maxDestroyedNum.setText(norToAbnor(str(maxDestroy)))
                self.minDestroyedNum.setText(norToAbnor(str(minDestroy)))
                self.averageDestroyedNum.setText(norToAbnor(str(sumDestroy)))

    def checkStars(self):                                           # 강화 수치에 따라 별의 색이 바뀌도록 하는 함수
        for i in range(15):
            if self.upgraded > i:
                self.starstatus[i] = 1                              # 값이 1이면 노란색 별, 0이면 회색 별
            else:
                self.starstatus[i] = 0
            tmpstar = QPixmap()
            tmpstar.load(self.statusinfo[self.starstatus[i]])
            tmpstar = tmpstar.scaled(15, 15)
            self.star[i].setPixmap(tmpstar)
        for i in range(15, 25):
            if self.upgraded > i:
                self.starstatus[i] = 1
            else:
                self.starstatus[i] = 0
            tmpstar = QPixmap()
            tmpstar.load(self.statusinfo[self.starstatus[i]])
            tmpstar = tmpstar.scaled(15, 15)
            self.star[i].setPixmap(tmpstar)
    
    def showUpgradeIndex(self, nowStars):
        # 무기 사진 오른쪽에 표시하는 정보들
        percent, broken = calcPercent(nowStars)
        self.currentInfo.clear()
        if self.failedNums == 2:
            self.currentInfo.append("찬스 타임!!\n\n" + str(nowStars) + "성 -> " + str(nowStars+1) + "성\n")
        else: self.currentInfo.append("\n\n" + str(nowStars) + "성 -> " + str(nowStars+1) + "성\n")
        if self.failedNums == 2:
            self.currentInfo.append("강화 성공 확률 : 100%")
            return
        self.currentInfo.append("강화 성공 확률 : " + str(percent))
        if nowStars <= 10:
            self.currentInfo.append("강화 실패(유지) 확률 : " + str(100-percent-broken) + "%")
        elif nowStars <= 11:
            self.currentInfo.append("강화 실패(하락) 확률 : " + str(100-percent-broken) + "%")
        else:
            self.currentInfo.append("강화 실패(하락) 확률 : " + str(100-percent-broken) + "%")
            self.currentInfo.append("파괴 확률 : " + str(broken) + "%")


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    Main_GUI = Sim_GUI()
    Main_GUI.show()
    sys.exit(app.exec_())

