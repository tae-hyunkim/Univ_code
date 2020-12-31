import sys
import random
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QPixmap

class Sim_GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected = True
        self.currentStars = 0
        self.tryUpgrade = 0
        self.failedNums = 0

    
    def initUI(self):
        # 왼쪽 부분(직접 1회씩 강화 시뮬레이션을 하는 부분)의 위젯들을 작성
        self.rating = 15
        ##레벨 선택
        level = QLabel("레벨 : ", self)
        self.selectedLevel = QComboBox()
        self.selectedLevel.addItem("150")
        self.selectedLevel.addItem("160")
        self.selectedLevel.addItem("200")
        levelButton = QPushButton("선택")

        ##현재강화등급
        nowStarLabel = QLabel("현재 강화 등급 : ", self)
        self.nowStar = QLineEdit("0")
        self.nowStar.setAlignment(Qt.AlignCenter)
        self.nowStar.setReadOnly(False)
        self.nowStar.setValidator(QIntValidator())
        self.nowStar.setValidator(QIntValidator(0, 24, self))
        emptyPlace = QLabel(" ", self)

        ##시도횟수
        countUpgradeLabel = QLabel("시도 횟수 : ", self)
        self.countUpgrade = QLineEdit("0")
        self.countUpgrade.setAlignment(Qt.AlignCenter)
        self.countUpgrade.setReadOnly(True)

        ##파괴횟수
        countDestroyedLabel = QLabel("파괴 횟수 : ", self)
        self.countDestroyed = QLineEdit("0")
        self.countDestroyed.setAlignment(Qt.AlignCenter)
        self.countDestroyed.setReadOnly(True)

        ##사진
        self.weapons = {"150":"./img/150.png", "160":"./img/160.png", "200":"./img/200.png"}
        self.weaponImage = QPixmap()
        self.weaponImage.load(self.weapons["150"])
        self.weaponImage = self.weaponImage.scaled(150, 150)
        self.displayImage = QLabel()
        self.displayImage.setPixmap(self.weaponImage)
        self.nowWeaponText = "150"



        ##현재 아이템 정보(확률 등)
        self.currentInfo = QTextEdit()
        self.currentInfo.setReadOnly(True)

        ##필요한 메소
        needMesoLabel = QLabel("필요한 메소 : ", self)
        self.needMeso = QLineEdit()
        self.needMeso.setAlignment(Qt.AlignRight)
        self.needMeso.setReadOnly(True)

        ##사용한 메소
        usedMesoLabel = QLabel("사용한 메소 : ", self)
        self.usedMeso = QLineEdit()
        self.usedMeso.setAlignment(Qt.AlignRight)
        self.usedMeso.setReadOnly(True)

        ##강화, 초기화 버튼
        upgrade = QPushButton("강화")
        reset = QPushButton("초기화")
        hbox01 = QHBoxLayout()
        hbox01.addStretch(1)

        k = 0
        if (self.rating < 15):

            for i in range(int(self.nowStar.text())):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("./img/yellowstar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
                k = k + 1
                if (k % 5 == 0):
                    hbox01.addWidget(emptyPlace)
            for i in range(15 - self.rating):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("./img/greystar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
                k = k + 1
                if (k % 5 == 0):
                    hbox01.addWidget(emptyPlace)
            hbox01.addStretch(1)

            hbox02 = QHBoxLayout()
            hbox02.addStretch(1)
            for i in range(10):
                k = k + 1
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("./img/greystar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
                if (k % 5 == 0):
                    hbox01.addWidget(emptyPlace)

            hbox02.addStretch(1)

        if (self.rating >= 15):
            for i in range(15):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("./img/yellowstar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
                k = k + 1
                if (k % 5 == 0):
                    hbox01.addWidget(emptyPlace)
            hbox01.addStretch(1)

            hbox02 = QHBoxLayout()
            hbox02.addStretch(1)
            for i in range(self.rating - 15):
                k = k + 1
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("./img/yellowstar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
                if (k % 5 == 0):
                    hbox02.addWidget(emptyPlace)
            for i in range(10 - self.rating + 15):
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("./img/greystar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
                k = k + 1
                if (k % 5 == 0):
                    hbox02.addWidget(emptyPlace)
            hbox02.addStretch(1)

        # 왼쪽 레이아웃에 위젯들을 추가
        leftLayout = QGridLayout()
        leftLayout.addWidget(self.displayImage, 2, 1)
        leftLayout.addWidget(self.currentInfo, 2, 2, 1, 8)
        leftLayout.addWidget(level, 3, 1, Qt.AlignRight)
        leftLayout.addWidget(self.selectedLevel, 3, 2)
        leftLayout.addWidget(nowStarLabel, 3, 3, Qt.AlignRight)
        leftLayout.addWidget(self.nowStar, 3, 4)
        leftLayout.addWidget(levelButton, 3, 5)
        leftLayout.addWidget(countUpgradeLabel, 4,1, Qt.AlignRight)
        leftLayout.addWidget(self.countUpgrade, 4,2)
        leftLayout.addWidget(countDestroyedLabel, 4,3, Qt.AlignRight)
        leftLayout.addWidget(self.countDestroyed, 4,4)
        leftLayout.addWidget(needMesoLabel, 5,1,Qt.AlignRight)
        leftLayout.addWidget(self.needMeso, 5,2)
        leftLayout.addWidget(usedMesoLabel, 5,3,Qt.AlignRight)
        leftLayout.addWidget(self.usedMeso, 5,4,)

        leftLayout.addWidget(upgrade, 6, 2)
        leftLayout.addWidget(reset, 6, 4)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox01)
        vbox.addLayout(hbox02)
        vbox.addLayout(leftLayout)
        """
        leftLayout.addWidget(emptyPlace, 0, 0, 1, 3)
        leftLayout.addWidget(level, 0, 3, 1, 2, Qt.AlignRight)
        leftLayout.addWidget(self.selectedLevel, 0, 5, 1, 1)
        leftLayout.addWidget(levelButton, 0, 6, 1, 2)
        leftLayout.addWidget(emptyPlace, 0, 8, 1, 3)
        leftLayout.addWidget(nowStarLabel, 0, 11, 1, 3, Qt.AlignRight)
        leftLayout.addWidget(self.nowStar, 0, 14, 1, 3)
        leftLayout.addWidget(emptyPlace, 0, 17, 1, 3)

        leftLayout.addWidget(countUpgradeLabel, 1, 3, 1, 2, Qt.AlignRight)
        leftLayout.addWidget(self.countUpgrade, 1, 5, 1, 2)
        leftLayout.addWidget(countDestroyedLabel, 1, 10, 1, 4, Qt.AlignRight)
        leftLayout.addWidget(self.countDestroyed, 1, 14, 1, 3)

        leftLayout.addWidget(self.displayImage, 2, 3, 1, 3) 
        leftLayout.addWidget(self.currentInfo, 2, 7, 1, 10)

        leftLayout.addWidget(needMesoLabel, 3, 3, 1, 1)
        leftLayout.addWidget(self.needMeso, 3, 4, 1, 13)
        leftLayout.addWidget(usedMesoLabel, 4, 3, 1, 1)
        leftLayout.addWidget(self.usedMeso, 4, 4, 1, 13)

        leftLayout.addWidget(upgrade, 5, 3, 1, 7)
        leftLayout.addWidget(reset, 5, 10, 1, 7)
        """


        # 오른쪽 부분(여러 횟수를 자동으로 시뮬레이션하여 평균적인 기댓값 산출하는 부분)의 위젯들을 작성
        """
        startStarsLabel = QLabel("시작 수치 : ", self)
        self.startStars = QLineEdit()
        self.startStars.setAlignment(Qt.AlignCenter)
        self.startStars.setPlaceholderText("(0 ~ 25)")
        self.startStars.setValidator(QIntValidator(0, 25, self))
        """
        #목표등급
        toStarsLabel = QLabel("목표 수치 : ", self)
        self.toStars = QLineEdit()
        self.toStars.setAlignment(Qt.AlignCenter)
        self.toStars.setPlaceholderText("~ 25")
        self.toStars.setValidator(QIntValidator(0, 25, self))
        #시도횟수
        tryNumsLabel = QLabel("시도 횟수 : ", self)
        self.tryNums = QLineEdit()
        self.tryNums.setAlignment(Qt.AlignCenter)
        self.tryNums.setPlaceholderText("(1 ~ 10000)")
        self.tryNums.setValidator(QIntValidator(1, 10000, self))
        #시뮬레이션 시작버튼
        startSimulationButton = QPushButton("시뮬레이션 시작")
        #시뮬창
        self.simulationStatus = QTextEdit()
        self.showSimulationMessage("무기의 레벨을 선택 후, \"시뮬레이션 시작\" 버튼을 클릭해 주세요.")
        #사용메소
        averageUsedMesoLabel = QLabel("평균 사용 메소 : ", self)
        self.averageUsedMeso = QLineEdit()
        self.averageUsedMeso.setAlignment(Qt.AlignRight)
        self.averageUsedMeso.setReadOnly(True)

        minUsedMesoLabel = QLabel("최소 사용 메소 : ", self)
        self.minUsedMeso = QLineEdit()
        self.minUsedMeso.setAlignment(Qt.AlignRight)
        self.minUsedMeso.setReadOnly(True)

        maxUsedMesoLabel = QLabel("최대 사용 메소 : ", self)
        self.maxUsedMeso = QLineEdit()
        self.maxUsedMeso.setAlignment(Qt.AlignRight)
        self.maxUsedMeso.setReadOnly(True)

        # 시도 횟수
        averageTryLabel = QLabel("평균 시도 횟수 : ", self)
        self.averageTry = QLineEdit()
        self.averageTry.setAlignment(Qt.AlignRight)
        self.averageTry.setReadOnly(True)

        minTryLabel = QLabel("최소 시도 횟수 : ", self)
        self.minTry = QLineEdit()
        self.minTry.setAlignment(Qt.AlignRight)
        self.minTry.setReadOnly(True)

        maxTryLabel = QLabel("최대 시도 횟수 : ", self)
        self.maxTry = QLineEdit()
        self.maxTry.setAlignment(Qt.AlignRight)
        self.maxTry.setReadOnly(True)
        # 오른쪽 레이아웃에 위젯들을 추가
        rightLayout = QGridLayout()

        #rightLayout.addWidget(startStarsLabel, 0, 3, 1, 2, Qt.AlignRight)
        #rightLayout.addWidget(self.startStars, 0, 5, 1, 2)
        #rightLayout.addWidget(emptyPlace, 0, 7, 1, 1)
        rightLayout.addWidget(toStarsLabel, 0,0, Qt.AlignRight)
        rightLayout.addWidget(self.toStars, 0,1,1,2)
        rightLayout.addWidget(tryNumsLabel, 0,3, Qt.AlignRight)
        rightLayout.addWidget(self.tryNums, 0, 4,1,3)
        rightLayout.addWidget(startSimulationButton, 0,9)

        rightLayout.addWidget(self.simulationStatus, 2, 0, 1, 15)

        rightLayout.addWidget(averageUsedMesoLabel, 3, 0, Qt.AlignRight)
        rightLayout.addWidget(self.averageUsedMeso, 3, 1,1,3)
        rightLayout.addWidget(averageTryLabel, 3, 4, Qt.AlignRight)
        rightLayout.addWidget(self.averageTry, 3, 5)

        rightLayout.addWidget(minUsedMesoLabel, 4, 0, Qt.AlignRight)
        rightLayout.addWidget(self.minUsedMeso, 4, 1, 1,3)
        rightLayout.addWidget(minTryLabel, 4, 4, Qt.AlignRight)
        rightLayout.addWidget(self.minTry, 4, 5)

        rightLayout.addWidget(maxUsedMesoLabel, 5, 0, Qt.AlignRight)
        rightLayout.addWidget(self.maxUsedMeso, 5, 1, 1,3)
        rightLayout.addWidget(maxTryLabel, 5, 4, Qt.AlignRight)
        rightLayout.addWidget(self.maxTry, 5, 5)

        # 좌우측 레이아웃을 통합
        mainLayout = QGridLayout()

        mainLayout.addLayout(vbox, 0, 0)
        mainLayout.addLayout(rightLayout, 0, 1)

        levelButton.clicked.connect(self.buttonclicked)
        upgrade.clicked.connect(self.buttonclicked)
        reset.clicked.connect(self.buttonclicked)
        startSimulationButton.clicked.connect(self.buttonclicked)

        # 레이아웃의 크기를 고정하고, 윈도우의 이름 정의
        #mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(mainLayout)
        self.setGeometry(500, 300, 900, 365)
        self.setWindowTitle("Starforce Simulator")
    
    def buttonclicked(self):
        sender= self.sender()
        if sender.text() == "선택":
            if self.selected:
                self.selected = False
                self.nowWeaponText = self.selectedLevel.currentText()
                """
                self.rating = int(self.nowStar.text())
                self.initUI()
                """
                self.weaponImage.load(self.weapons[self.nowWeaponText])
                self.weaponImage = self.weaponImage.scaled(150, 150)
                self.needMeso.setText(str(self.calcMeso(0)))
                self.usedMeso.setText("0")
                self.showUpgradeIndex(0)
        elif self.selected == False:
            if sender.text() == "강화":
                prevStar = self.nowStar.text()
                nextStar = self.doUpgrade(int(prevStar))
                self.usedMeso.setText(str(int(self.usedMeso.text())+int(self.needMeso.text())))
                self.countUpgrade.setText(str(int(self.countUpgrade.text())+1))
                if nextStar == "-1":
                    self.nowStar.setText("12")
                    #self.rating = 12
                    self.countDestroyed.setText(str(int(self.countDestroyed.text())+1))
                else:
                    self.nowStar.setText(nextStar)
                    #self.rating = int(nextStar)
                self.showUpgradeIndex(int(self.nowStar.text()))
                self.needMeso.setText(str(self.calcMeso(int(self.nowStar.text()))))
            elif sender.text() == "초기화":
                self.selected = True
                self.needMeso.clear()
                self.usedMeso.clear()
                self.nowStar.setText("0")
                #self.rating = 0
                self.countUpgrade.setText("0")
                self.countDestroyed.setText("0")
                self.currentInfo.clear()
                self.showSimulationMessage("무기의 레벨을 선택 후, \"시뮬레이션 시작\" 버튼을 클릭해 주세요.")
                self.toStars.setText("")
                self.tryNums.setText("")
                self.maxUsedMeso.setText("")
                self.minUsedMeso.setText("")
                self.averageUsedMeso.setText("")
        if sender.text() == "시뮬레이션 시작": # 무기레벨 설정이 시뮬레이션 구역과는 동떨어져있으므로 혼선을 방지하기 위해 위 if-elif-else문에 포함시키지 않고 독립적으로 생성함
            if self.selected == True:
                self.showSimulationMessage("먼저 무기의 레벨을 선택해주세요.")
            elif ((self.nowStar.text() == "") or (self.toStars.text() == "") or (self.tryNums.text() == "")):
                self.showSimulationMessage("시작 등급, 목표 등급, 시뮬레이션 횟수를 입력해주세요.")
            else:
                self.showSimulationMessage("시뮬레이션중...")
                minTry = 0
                maxTry = 0
                sumTry = 0
                minMeso = 0
                maxMeso = 0
                sumMeso = 0
                for i in range(int(self.tryNums.text())):

                    startStar = int(self.nowStar.text())
                    toStar = int(self.toStars.text())
                    currentStar = startStar
                    currentMeso = 0
                    currentTry = 0
                    while currentStar < toStar:
                        currentMeso += self.calcMeso(currentStar)
                        currentTry += 1
                        nextStar = self.doUpgrade(currentStar)

                        if nextStar == "-1":
                            currentStar = 12
                        else:
                            currentStar = int(nextStar)
                    if currentMeso > maxMeso:
                        maxMeso = currentMeso
                    if currentMeso < minMeso or minMeso == 0:
                        minMeso = currentMeso
                    if currentTry > maxTry:
                        maxTry = currentTry
                    if currentTry < minTry or minTry == 0:
                        minTry = currentTry

                    sumTry += currentTry
                    sumMeso += currentMeso
                sumMeso = int(sumMeso / int(self.tryNums.text()))
                sumTry = int(sumTry / int(self.tryNums.text()))
                self.maxUsedMeso.setText(str(maxMeso))
                self.minUsedMeso.setText(str(minMeso))
                self.averageUsedMeso.setText(str(sumMeso))
                self.maxTry.setText(str(maxTry))
                self.minTry.setText(str(minTry))
                self.averageTry.setText(str(sumTry))
                #self.rating = toStars.text()
                self.showSimulationMessage("시뮬레이션이 완료되었습니다.")
    
    def doUpgrade(self, prevStar):
        # 강화 성공/실패/파괴에 따른 결과값 리턴
        if self.failedNums == 2:
            self.failedNums = 0
            return str(prevStar + 1)
        percent, broken = self.calcPercent(prevStar)
        result = random.choices(range(0, 3), weights = [100-percent-broken, percent, broken])
        if result[0] == 2:

            return "-1"

        elif result[0] == 1:
            self.failedNums = 0

            return str(prevStar + 1)
        else:
            if prevStar <= 10 or prevStar == 15 or prevStar == 20:
                self.showSimulationMessage(str(prevStar))
                return str(prevStar)
            else:
                self.failedNums += 1

                return str(prevStar - 1)

    def calcPercent(self, prevStar):
        # 강화시 성공/파괴될 확률 계산
        percent = 0
        broken = 0
        if prevStar <= 2:
            percent = 95 - 5 * prevStar
        elif prevStar <= 14:
            percent = 100 - 5 * prevStar
            if prevStar == 12:
                broken = 0.6
            elif prevStar == 13:
                broken = 1.3
            elif prevStar == 14:
                broken = 1.4
        elif prevStar <= 21:
            percent = 30
            if prevStar <= 17:
                broken = 2.1
            elif prevStar <= 19:
                broken = 2.8
            else:
                broken = 7
        elif prevStar == 22:
            percent = 3
            broken = 19.4
        elif prevStar == 23:
            percent = 2
            broken = 29.4
        elif prevStar == 24:
            percent = 1
            broken = 39.6
        return [percent, broken]
    
    def calcMeso(self, prevStar):
        # 강화 시도에 사용된 비용을 계산
        useMeso = 0
        weaponLV = int(self.nowWeaponText)
        if prevStar <= 9:
            useMeso = 1000 + weaponLV**3 * (prevStar + 1) / 25
        elif prevStar <= 14:
            useMeso = 1000 + weaponLV**3 * (prevStar + 1)**2.7 / 400
        else:
            useMeso = 1000 + weaponLV**3 * (prevStar + 1)**2.7 / 200
        useMeso = int((useMeso / 100) * 100)
        return useMeso
    
    def showUpgradeIndex(self, nowStars):
        # 무기 사진 오른쪽에 표시하는 정보들
        percent, broken = self.calcPercent(nowStars)
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
    
    def showSimulationMessage(self, Message):
        #시뮬레이션의 상태를 표시하기 위한 함수
        self.simulationStatus.clear()
        self.simulationStatus.setAlignment(Qt.AlignCenter)
        self.simulationStatus.append("\n\n\n\n" + Message)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    Main_GUI = Sim_GUI()
    Main_GUI.show()
    sys.exit(app.exec_())

