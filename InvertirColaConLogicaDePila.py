class pila():
  def __init__(self):
    self.Stack:list = []

  def push(self,e:int)->int:
    return self.Stack.append(e)


  def pop(self) -> int:
    if len(self.Stack) >0:
      return self.Stack.pop()
    else:
      raise Exception ("La pila está vacía")

  def peek(self) -> int:
    if len(self.Stack) > 0:
      return self.Stack[-1]

  def is_empty(self):
      return len(self.Stack) == 0


li = pila()
li.push(5)
li.push(10)
li.push(6)
print(li.peek())
print(li.pop())
print(li.Stack)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        self.queue.append(n)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise Exception("La cola está vacía")

    def first(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("La cola está vacía")

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self):
        return str(self.queue)


def invertir_cola(cola):
    stack_aux = pila()

    while not cola.is_empty():
        stack_aux.push(cola.dequeue())

    while not stack_aux.is_empty():
        cola.enqueue(stack_aux.pop())
    return cola


q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(34)
q.enqueue(8)
q.enqueue(10)

print("Cola antes de invertir:", q)
invertir_cola(q)
print("Cola después de invertir:", q)
