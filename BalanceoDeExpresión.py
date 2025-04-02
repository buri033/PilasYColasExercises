class EmptyStack(Exception):
    """Excepción que se lanza cuando se intenta acceder a una pila vacía."""
    pass


class Pila():
    def __init__(self):
        self.Stack: list = []

    def push(self, e: int) -> int:
        return self.Stack.append(e)

    def pop(self) -> int:
        if len(self.Stack) > 0:
            return self.Stack.pop()
        else:
            raise Exception("La pila está vacía")

    def peek(self) -> int:
        if len(self.Stack) > 0:
            return self.Stack[-1]

    def __len__(self):
        return len(self.Stack)

    def __repr__(self):
        return str(self.Stack)


def verificar_balanceo(expresion):
    pila = Pila()
    apertura = "([{"
    cierre = ")]}"

    for caracter in expresion:
        if caracter in apertura:
            pila.push(caracter)
        elif caracter in cierre:
            if len(pila) == 0:  # Pila vacía, no hay apertura correspondiente
                return False
            ultimo = pila.pop()
            if apertura.index(ultimo) != cierre.index(caracter):  # No coinciden
                return False

    return len(pila) == 0  # Balanceado si la pila está vacía al final


expresion1 = "{ [ ( ) ] }"
expresion2 = "{ [ ( ] ) }"

print(f"Expresión 1: {expresion1}, Balanceada: {verificar_balanceo(expresion1)}")
print(f"Expresión 2: {expresion2}, Balanceada: {verificar_balanceo(expresion2)}")
