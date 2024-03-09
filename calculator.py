class Calculator:
    def __init__(self):
        pass

    def runOperation(self, expression):
        try: 
            resultado = eval(expression)
            return str(resultado)
        except Exception as e:
            return f"Error al evaluar la expresion: {e}"

