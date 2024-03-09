import os
from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.table import Column, Table

class UI:
    def __init__(self):
        self.header = "Calculator"
        self.expression = ""
        self.instructions = "\n  Operations:\n\n  add: +\n  subtract: -\n  divide: /\n  multiply: * \n\n  EXIT: q   CLEAR: c    CLEAR HISTORY: h    CALCULATE: enter    "
        self.history = ""
        pass

    def renderInstructions(self):
        pass

    def renderHistory(self):
        pass
    
    def renderExpression(self):
        pass
    
    def renderHistory(self):
        pass

    def render(self, currentExpression, lastExpression):
        print("\033c", end="", flush=True)

        self.renderInstructions()
        self.renderHistory()
        self.renderExpression()
        self.renderHistory()

        panel_group = Group(
            Panel(currentExpression),
            self.instructions
        )

        history = Group(
            lastExpression
        )
        
        table = Table(
        self.header,
        "History",
        )
        
        table.add_row(panel_group, history)
            
        print(table)