import os
from rich import print
from rich.console import Group
from rich.panel import Panel

class UI:
    def __init__(self):
        self.header = "Calculator\n"
        self.expression = ""
        self.instructions = "\nOperations:\n  Enter: <return>\n  add: +\n  subtract: -\n  divide: /\n  multiply: *"
        pass

    def renderInstructions(self):
        pass

    def renderExpression(self):
        pass

    def render(self, currentExpression):
        print("\033c", end="", flush=True)

        self.renderInstructions()
        self.renderExpression()

        panel_group = Group(
            self.header,
            Panel(currentExpression),
            self.instructions
        )

        print(Panel(panel_group))

