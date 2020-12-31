from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtWidgets import QLayout, QGridLayout


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)# 값 수정 가능하도록 
        self.display.setAlignment(Qt.AlignRight) # 값 정렬 (오른쪽 왼쪽 센터등)
        self.display.setMaxLength(15)

        # Layout
        mainLayout = QGridLayout()
        # 크기조절 불가능 하도록 막는 구문. 
        mainLayout.setSizeConstraint(QLayout.SetFixedSize) # 만들어진 창 크기에 맞게 제약을 주겟다. 

        mainLayout.addWidget(self.display, 0, 0, 1, 1) # 설정한 display window값 붙여넣기. 
        # 뒤에 2개의 인자값은 첫번째 값 행 몇칸 두번째값 열 몇칸 사용할지 
        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

