import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)
label = QLabel("Hello PyQt")
label.show()
label2 = QPushButton("Button")
label2.show()
app.exec_()

