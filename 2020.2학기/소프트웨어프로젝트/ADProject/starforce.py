# import
from PyQt5.QtCore import Qt
import sys, pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox01 = QHBoxLayout()
        #강화등급 표시
        hbox01.addStretch(1)
        rating = 22

        if(rating<15):
            for i in range(rating):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("ADProject/yellowstar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
            for i in range(15 - rating):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("ADProject/greystar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
            hbox01.addStretch(1)

            hbox02 = QHBoxLayout()
            hbox02.addStretch(1)
            for i in range(10):
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("ADProject/greystar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
            hbox02.addStretch(1)

        if (rating >= 15):
            for i in range(15):
                self.yellowstarImage = QLabel(self)
                pixmap = QPixmap("ADProject/yellowstar.png")
                self.yellowstarImage.setPixmap(QPixmap(pixmap))
                hbox01.addWidget(self.yellowstarImage)
            hbox01.addStretch(1)

            hbox02 = QHBoxLayout()
            hbox02.addStretch(1)
            for i in range(rating-15):
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("ADProject/yellowstar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
            for i in range(10-rating+15):
                self.greystarImage = QLabel(self)
                pixmap = QPixmap("ADProject/greystar.png")
                self.greystarImage.setPixmap(QPixmap(pixmap))
                hbox02.addWidget(self.greystarImage)
            hbox02.addStretch(1)

        #아이템 이미지
        hbox03 = QHBoxLayout()

        self.ItemImage = QLabel(self)
        pixmap = QPixmap("ADProject/item.jpg")
        self.ItemImage.setPixmap(QPixmap(pixmap))
        hbox03.addWidget(self.ItemImage)
        #아이템 정보
        self.enhance_textedit = QTextEdit(self)

        enhance_announce = str(rating)+"성"+" > "+str(rating+1)+"성" +"\n" + "성공확률: "+" 95.0"+"%"+ "\n" + "실패(유지)확률: "+"5.0"+"%"
        self.enhance_textedit.setPlainText(enhance_announce)
        self.enhance_textedit.setReadOnly(True)
        hbox03.addWidget(self.enhance_textedit)

        #파괴방지, 필요메서, 강화버튼, 취소버튼
        hbox04 = QHBoxLayout()
        break_checkbox = QCheckBox('파괴방지', self)
        hbox04.addWidget(break_checkbox)

        hbox05 = QHBoxLayout()
        need_money_label = QLabel('필요한 메소:' + '21500')
        hbox05.addStretch(1)
        hbox05.addWidget(need_money_label)
        hbox05.addStretch(1)

        hbox06 = QHBoxLayout()
        enhance_button = QPushButton("강화", self)
        cancle_button = QPushButton("취소", self)
        hbox06.addWidget(enhance_button)
        hbox06.addWidget(cancle_button)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox01)
        vbox1.addLayout(hbox02)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox03)
        vbox1.addLayout(hbox04)
        vbox1.addLayout(hbox05)
        vbox1.addLayout(hbox06)
        vbox1.addStretch(1)


        now_grade_label = QLabel('현재등급:')
        target_grade_label = QLabel('목표등급:')
        now_grade = []
        for i in range(0, 25):
            now_grade.append(str(i))
        target_grade = []
        for i in range(1, 26):
            target_grade.append(str(i))
        self.now_grade_combobox = QComboBox(self)
        self.now_grade_combobox.addItems(now_grade)
        self.target_grade_combobox = QComboBox(self)
        self.target_grade_combobox.addItems(target_grade)



        hbox1 = QHBoxLayout()
        hbox1.addWidget(now_grade_label)
        hbox1.addWidget(self.now_grade_combobox)
        hbox1.addStretch(1)
        hbox1.addWidget(target_grade_label)
        hbox1.addWidget(self.target_grade_combobox)
        hbox1.addStretch(1)

        lv_label = QLabel('레벨')
        lv = ['100','110','120','130','140','150']
        auto_checkbox = QCheckBox('자동강화',self)
        self.lv_combobox = QComboBox(self)
        self.lv_combobox.addItems(lv)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(lv_label)
        hbox2.addWidget(self.lv_combobox)
        hbox2.addStretch(1)

        hbox2.addWidget(auto_checkbox)
        hbox2.addStretch(1)

        max_money_label = QLabel('최대 사용메소(무제한은 0):')
        self.max_money_lineedit = QLineEdit(self)
        self.max_money_lineedit.setValidator(QIntValidator())
        hbox3 = QHBoxLayout()
        hbox3.addWidget(max_money_label)
        hbox3.addWidget(self.max_money_lineedit)

        paied_money_label = QLabel('사용된 메소:')
        self.paied_money_lineedit = QLineEdit(self)
        self.paied_money_lineedit.setReadOnly(True)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(paied_money_label)
        hbox4.addWidget(self.paied_money_lineedit)

        result_label = QLabel('강화결과:')
        self.result_lineedit = QLineEdit(self)
        self.result_lineedit.setReadOnly(True)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(result_label)
        hbox5.addWidget(self.result_lineedit)

        acc_result_label = QLabel('-누적결과-')
        hbox6 = QHBoxLayout()
        hbox6.addWidget(acc_result_label)

        self.result_textedit = QTextEdit(self)
        self.result_textedit.setPlainText("ex) 실패 "+"\n"+"성공")
        self.result_textedit.setReadOnly(True)
        hbox7 = QHBoxLayout()
        hbox7.addWidget(self.result_textedit)


        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox1)
        vbox2.addLayout(hbox2)
        vbox2.addLayout(hbox3)
        vbox2.addLayout(hbox4)
        vbox2.addLayout(hbox5)
        vbox2.addLayout(hbox6)
        vbox2.addLayout(hbox7)
        vbox2.addStretch(1)

        Hbox = QHBoxLayout()
        Hbox.addStretch(1)
        Hbox.addLayout(vbox1)
        Hbox.addStretch(1)
        Hbox.addLayout(vbox2)
        self.setLayout(Hbox)
        self.setGeometry(800, 300, 750, 365)
        self.setWindowTitle('STARFORCE')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
