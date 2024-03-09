import os
from rich import print
from rich.console import Group
from rich.panel import Panel

class UI:
    def __init__(self):
        self.header = "Calculator\n"
        self.history = "History"
        self.expression = ""
        self.instructions = "\n  Operations:\n\n  add: +\n  subtract: -\n  divide: /\n  multiply: * \n\n  EXIT: q   CLEAR: c  CALCULATE: enter"
        pass

    def renderInstructions(self):
        pass

    def renderHistory(self):
        pass
    
    def renderExpression(self):
        pass

    def render(self, currentExpression):
        print("\033c", end="", flush=True)

        self.renderInstructions()
        self.renderHistory()
        self.renderExpression()

        panel_group = Group(
            self.header,
            Panel(currentExpression),
            self.instructions
        )
        
        

        print(Panel(panel_group))
