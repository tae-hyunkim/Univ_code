#-*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman
from guess import Guess
from word import Word


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database        
        self.word = Word('class06_Make_file_실습_과제/hang_man_gui/words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        # 해당 부분에서 단어 추출 -> 11글자 이상 단어 추출 안되도록 작업 
        self.guess = Guess(self.word.randFromDB())
        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            self.message.setText('Game over!')
            return 
        
        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if len(guessedChar) != 1:
            self.message.setText('입력하신 단어의 개수가 옳지 않습니다.')
            return 

        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if guessedChar in self.guess.displayGuessed():
            self.message.setText('이미 추정한 단어입니다.')
            return 

        success = self.guess.guess(guessedChar)
        if success == False:
            
            # 남아 있는 목숨을 1 만큼 감소
            self.hangman.decreaseLife()
            # 메시지 출력
            self.message.setText(guessedChar + '은 시크릿 단어가 아니였습니다.')
            pass
        
        # 알파벳 유무 점검 
        if not guessedChar.isalpha():
            self.message.setText(guessedChar + '은 알파벳을 입력해 주셔야 합니다.')
            return
        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력
        self.guessedChars.setText(self.guess.displayGuessed())

        # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
        if self.guess.finished():
            self.message.setText('성공!')
            self.gameOver = True

        # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
        elif self.hangman.getRemainingLives() == 0:
            self.message.setText('실패하셨습니다. 단어는: ' + self.guess.secretWord)
            self.gameOver = True


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

