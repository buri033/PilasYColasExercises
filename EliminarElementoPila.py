class pilallena():
    def __init__(self):
        self.Stack: list = []

    def pop(self) -> int:
        if len(self.Stack) > 0:
            return self.Stack.pop()
        else:
            raise Exception("La pila está vacía")

    def push(self, e: int) -> None:
        self.Stack.append(e)

    def peek(self) -> int:
        if len(self.Stack) > 0:
            return self.Stack[-1]

    def __len__(self):
        return len(self.Stack)

    def __repr__(self):
        return str(self.Stack)


def eliminar_elemento(pila: pilallena, elemento: int) -> None:
    """Elimina el primer elemento encontrado en la pila mientras la recorre."""
    temp_stack = pilallena()
    encontrado = False

    while len(pila) > 0:
        valor = pila.pop()
        if valor == elemento and not encontrado:
            encontrado = True
            print(f"Elemento {elemento} eliminado de la pila.")
        else:
            temp_stack.push(valor)

    while len(temp_stack) > 0:
        pila.push(temp_stack.pop())

    if not encontrado:
        print(f"Elemento {elemento} no encontrado en la pila.")


# Ejemplo de uso:
li = pilallena()
li.push(5)
li.push(10)
li.push(6)
print("Pila antes de eliminar:", li)
eliminar_elemento(li, 10)
print("Pila después de eliminar:", li)
