import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

def probabilty(current,current_enhance):
    if current > 11:
        return '강화 성공 확률 : {}%\n강화 실패 확률 : {}% \n장비 파괴 확률 : {}%'.format(current_enhance,100-current_enhance*100-0.1,0.1 )
    else:
        return '강화 성공 확률 : {}%\n강화 실패 확률 : {}% '.format(current_enhance*100, 100-current_enhance*100)

class Gui_Frame(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.showProba()
        self.showHistory()

    def initUI(self):
        self.title = QHBoxLayout()
        self.BaseLevel = QHBoxLayout()
        self.currentEnhance = QHBoxLayout()
        self.EnhanceFrame = QHBoxLayout()
        self.EnhanceButton = QHBoxLayout()
        self.totalMoney = QHBoxLayout()

        # 제목 삽입 
        self.title.addWidget(QLabel('★스타포스 강화기★'))
        self.title.setAlignment(Qt.AlignCenter)

        # Item Level 정보 삽입 부분 
        self.BaseLevel.addWidget(QLabel('Item Level'))
        self.item_edit = QLineEdit()
        self.BaseLevel.addWidget(self.item_edit)

        # 시작강화 정보 삽입 부분 
        self.BaseLevel.addStretch(1)
        self.BaseLevel.addWidget(QLabel('시작 강화 수치'))
        self.start_enhance_edit = QLineEdit()
        self.BaseLevel.addWidget(self.start_enhance_edit)
        
        # 적용 버튼 삽입 부분
        self.BaseLevel.addStretch(1)
        self.application = QPushButton('적용')
        self.application.clicked.connect(self.button_clicked)
        self.BaseLevel.addWidget(self.application)
        # self.application.clicked.connect(self.application_button_clicked)
        
        
        # 현재 강화수치 삽입 부분 
        self.currentEnhance.addWidget(QLabel('현재 수치'))
        ## 강화수치 함수 적용 
        self.current_number = QLineEdit()
        self.current_number.setReadOnly(True)
        self.currentEnhance.addWidget(self.current_number)
        self.currentEnhance.addStretch(2)
        self.currentEnhance.addWidget(QLabel('과거 이력'))
        self.currentEnhance.addStretch(2)

        # 강화 확률 및 화면 출력 부분 
        self.Enhancetext = QTextEdit()
        self.Enhancetext.setReadOnly(True)
        self.EnhanceFrame.addWidget(self.Enhancetext)

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.EnhanceFrame.addWidget(self.history)

        # 단어 삽입부분

        # 강화, 초기화버튼 (강화버튼은 아이템 파괴시 전승버튼으로 변환)
        
        self.Enhance_B = QPushButton('강화/전승')
        self.EnhanceButton.addWidget(self.Enhance_B)
        self.EnhanceButton.addStretch(2)
        self.Enhance_R = QPushButton('초기화')
        self.EnhanceButton.addWidget(self.Enhance_R)
        self.Enhance_R.clicked.connect(self.button_clicked)
        self.EnhanceButton.addStretch(2)

        # 성공 횟수
        self.EnhanceButton.addStretch(2)
        self.EnhanceButton.addWidget(QLabel('누적 성공'))
        self.Enhance_S_edit = QLineEdit('1')
        self.Enhance_S_edit.setReadOnly(True)
        self.EnhanceButton.addWidget(self.Enhance_S_edit)

        # 실패 횟수
        self.EnhanceButton.addStretch(2)
        self.EnhanceButton.addWidget(QLabel('누적 실패'))
        self.Enhance_F_edit = QLineEdit('1')
        self.Enhance_F_edit.setReadOnly(True)
        self.EnhanceButton.addWidget(self.Enhance_F_edit)

        # 파괴 횟수
        self.EnhanceButton.addStretch(2)
        self.EnhanceButton.addWidget(QLabel('누적 파괴'))
        self.Enhance_D_edit = QLineEdit('1')
        self.Enhance_D_edit.setReadOnly(True)
        self.EnhanceButton.addWidget(self.Enhance_D_edit)

        # 누적 메소 사용량 
        self.totalMoney.addStretch(8)
        self.totalMoney.addWidget(QLabel('누적메소사용량 :'))
        self.totalMoney_edit = QLineEdit(str(100000))
        self.totalMoney.addWidget(self.totalMoney_edit)

        # Frame 구축부분 
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.title)
        self.vbox.addLayout(self.BaseLevel)
        self.vbox.addLayout(self.currentEnhance)
        self.vbox.addLayout(self.EnhanceFrame)
        self.vbox.addLayout(self.EnhanceButton)
        self.vbox.addLayout(self.totalMoney)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Assignment6') 
        
        self.show()

    def showHistory(self):
        self.history.append('{}강 -> {}강 {}'.format('12','13','성공'))
        # self.history.append('{}강 -> {}강 {}'.format('13','14','실패'))

    def showProba(self):
        self.Enhancetext.clear()
        self.Enhancetext.append(probabilty(10,0.3))


    def start_Num(self):
        self.current_number.clear()
        self.current_number.setText(str(self.current))


    def button_clicked(self):

        key = self.sender().text()

        if key =='적용':
            
            self.current = self.start_enhance_edit.text()
            self.item_Level = self.item_edit.text()

            self.start_Num()

        if key =='초기화':
            self.current = ''
            self.item_level = ''
            self.history.clear()
            self.Enhance_D_edit.clear()
            self.Enhance_F_edit.clear()
            self.Enhance_S_edit.clear()
            self.item_edit.clear()
            self.start_enhance_edit.clear()
            self.totalMoney_edit.clear()
            self.current_number.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Gui_Frame()
    calc.show()
    sys.exit(app.exec_())
