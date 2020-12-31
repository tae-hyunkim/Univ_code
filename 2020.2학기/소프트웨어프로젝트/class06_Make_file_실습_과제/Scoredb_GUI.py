import pickle
import sys

from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

def toString(data: dict) -> str:
    name, age, score = data['Name'], data['Age'], data['Score']
    return '{0:^30}{1:^24}{2:^18}'.format(name, age, score) 

class ScoreDB(QWidget):
    # constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = list()
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        # create five horizontal-boxes
        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        # set Name, Age, Score label on hbox0
        self.hbox0.addWidget(QLabel('  Name '))
        self.name_edit = QLineEdit()
        self.hbox0.addWidget(self.name_edit)

        self.hbox0.addWidget(QLabel('Age'))
        self.age_edit = QLineEdit()
        self.hbox0.addWidget(self.age_edit)

        self.hbox0.addWidget(QLabel('Score'))
        self.score_edit = QLineEdit()
        self.hbox0.addWidget(self.score_edit)

        # set Amount, Key label on hbox1

        self.hbox1.addWidget(QLabel('Amount'))
        self.amount_edit = QLineEdit()
        self.hbox1.addWidget(self.amount_edit)
        self.hbox1.addStretch(2)
        self.hbox1.addWidget(QLabel('Key'))

        # create combo-box, add key items
        self.key_box = QComboBox()

        self.key_box.addItem('Name')
        self.key_box.addItem('Age')
        self.key_box.addItem('Score')

        # add to horizontal-box
        self.hbox1.addWidget(self.key_box)

        # create five buttons, connect function
        self.addButton = QPushButton('ADD')
        self.addButton.clicked.connect(self.button_clicked)

        self.delButton = QPushButton('DEL')
        self.delButton.clicked.connect(self.button_clicked)

        self.findButton = QPushButton('FIND')
        self.findButton.clicked.connect(self.button_clicked)

        self.incButton = QPushButton('INC')
        self.incButton.clicked.connect(self.button_clicked)

        self.showButton = QPushButton('SHOW')
        self.showButton.clicked.connect(self.button_clicked)

        # set buttons on hbox2
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.addButton)
        self.hbox2.addWidget(self.delButton)
        self.hbox2.addWidget(self.findButton)
        self.hbox2.addWidget(self.incButton)
        self.hbox2.addWidget(self.showButton)

        # add Result label on hbox3
        self.hbox3.addWidget(QLabel('Result Table'))
        self.hbox3.addStretch(3)

        # add labels on hbox4
        category = '%18s%24s%20s' % ('Name', 'Age', 'Score')
        self.hbox4.addWidget(QLabel(category))

        # add text-edit on hbox5
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.hbox5.addWidget(self.result_text)

        # set horizontal-boxes on virtual-box
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6') 
        
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')

        except FileNotFoundError as e:
            self.scoredb = list()
            print(e)
            return self.scoredb

        try:
            self.scoredb = pickle.load(fH)

        except:
            pass

        fH.close()

        return self.scoredb

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        # initialize result text
        self.result_text.clear()

        # iterate db, append to result text
        for data in self.scoredb:
            self.result_text.append(toString(data))

    def button_clicked(self):
        key = self.sender().text()

        if key == 'ADD':
            # 입력값 읽어오기 (ADD에는 3개의 값이 필요함)
            name_content = self.name_edit.text()
            age_content = self.age_edit.text()
            score_content = self.score_edit.text()

            # 3개의 값 확인 후 맞으면 삽입 
            if len(name_content) != 0 and len(age_content) != 0 and len(score_content) != 0:
                
                new_data = dict(Name=name_content,Age=age_content, Score=score_content)

                self.scoredb += [new_data]

                self.showScoreDB()
            # 개수가 잘못 입력 되었을 때 삽입 안하도록 작업.

        elif key == 'DEL':
            # Score DB에서 Del 명령어를 입력할 때 Name에 아무것도 없어도 지우는게 없기 때문에 상관 X 
            name_content = self.name_edit.text()

            if name_content == '__ALL__':
                self.scoredb.clear()
                print('ALL DATA CASCADED')
            else:
                self.scoredb = list(
                    filter(lambda data: data['Name'] != name_content, self.scoredb))

            self.showScoreDB()

        elif key == 'FIND':
            
            # FIND값을 누를 때 name_content값이 아무것도 없을 경우 작동 안하도록 변경.
            name_content = self.name_edit.text()

            if len(name_content) != 0:
                search_result = [data for data in self.scoredb if data['Name'] == name_content]

                self.result_text.clear()

                for data in search_result:
                    self.result_text.append(toString(data))

        elif key == 'INC':

            name_content = self.name_edit.text()
            amount_content = self.amount_edit.text()

            for data in self.scoredb:
                if data['Name'] == name_content:
                    data['Score'] = str(int(data['Score'])+int(amount_content))

            self.showScoreDB()

        elif key == 'SHOW':

            combo_box_content = self.key_box.currentText()
            self.result_text.clear()

            # combo box에서 선택한 값에 따라 정렬 기준이 다름. 
            if combo_box_content == 'Name':
                for data in sorted(self.scoredb, key=lambda d: d[combo_box_content]):
                    self.result_text.append(toString(data))
                return

            elif combo_box_content in ['Age', 'Score']:
                for data in sorted(self.scoredb, key=lambda d: int(d[combo_box_content])):
                    self.result_text.append(toString(data))
                return



# execute
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())