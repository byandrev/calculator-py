import os
from ui import UI
from calculator import Calculator
import readchar

class App:
    allow_letters = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*"]

    def __init__(self):
        self.currentExpression = ""
        self.ui = UI()
        self.calculator = Calculator()

    def start(self):
        self.ui.render(self.currentExpression)

        while True:
            key = readchar.readkey()

            if key == readchar.key.BACKSPACE:
                self.currentExpression = self.currentExpression[:-1]
            elif key == readchar.key.ENTER:
                self.currentExpression = self.calculator.runOperation(self.currentExpression)
            elif key in self.allow_letters:
                self.currentExpression = self.currentExpression + key
            
            self.ui.render(self.currentExpression)

            if key == "c":
                self.currentExpression = ""
                self.ui.render(self.currentExpression)

            if key == "q":
                break
