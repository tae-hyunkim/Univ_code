import random
from PyQt5.QtWidgets import *

from Calculator import *

class Upgrader(QWidget):

    def __init__(self):
        super().__init__()
        self.failedNums = 0

    def doUpgrade(self, prevStar, starcatch, preventDestroy):
        # 강화 성공/실패/파괴에 따른 결과값 리턴
        if self.failedNums == 2:
            self.failedNums = 0
            return str(prevStar + 1)
        percent, broken = calcPercent(prevStar, starcatch, preventDestroy)
        result = random.choices(range(0, 3), weights = [round(100-percent-broken, 4), percent, broken])
        if result[0] == 2:
            return "-1"
        elif result[0] == 1:
            self.failedNums = 0
            return str(prevStar + 1)
        else:
            if prevStar <= 10 or prevStar == 15 or prevStar == 20:
                return str(prevStar)
            else:
                self.failedNums += 1
                return str(prevStar - 1)
