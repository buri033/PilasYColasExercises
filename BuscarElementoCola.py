class EmptyQueue(Exception):
    ...


class Queue:
    def __init__(self):
        self.queue: list[int] = []

    # agrega al final de la cola
    def enqueue(self, element: int):
        self.queue.append(element)

    # retorna y elimina el primer elemento que entró
    def dequeue(self) -> int:
        if (len(self.queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.queue.pop(0)

    # retorna el primer elemento que entró
    def first(self) -> int:
        if (len(self.queue) == 0):
            raise EmptyQueue("Cola Vacía...")
        return self.queue[0]

    def __repr__(self):
        return str(self.queue)

    def __len__(self):
        return len(self.queue)


def buscar_elemento_en_cola(cola: Queue, elemento: int, cont: int = 0, encontrado: bool = False) -> bool:
    if (cont == len(cola)):
        return encontrado
    if (cola.first() == elemento):
        encontrado = True
    cola.enqueue(cola.dequeue())  # encolando otra vez el primer elemento
    return buscar_elemento_en_cola(cola, elemento, cont + 1, encontrado)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(buscar_elemento_en_cola(q, 6))  # True
