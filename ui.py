import os
from rich import print
from rich.console import Group
from rich.panel import Panel

class UI:
    def __init__(self):
        self.header = Panel("Calculator")
        self.expression = ""
        self.instructions = "\nSum: +\nDiv: /"
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
            currentExpression,
            self.instructions
        )

        print(Panel(panel_group))

