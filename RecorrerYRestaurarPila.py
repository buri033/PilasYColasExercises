class pilallena():
  def __init__(self):
    self.Stack:list = []


  def pop(self, idx: int = 0) -> int:
    if len(self.Stack) > 0:
      return self.Stack.pop()
    else:
      raise Exception ("La pila está vacía")

  def push(self,e:int)->int:
    return self.Stack.append(e)

  def peek(self) -> int:
    if len(self.Stack) > 0:
      return self.Stack[-1]

  def __len__(self):
    return len(self.Stack)

  def __repr__(self):
    return str(self.Stack)

def recorrer_y_restaurar(Stack2):
  Stack3 = pilallena()

  while len(Stack2) > 0 :
      elemento = Stack2.pop()
      print(f"Elemento extraído: {elemento}")
      Stack3.push(elemento)
      print(Stack3)

  while len(Stack3) > 0 :
      elemento = Stack3.pop()
      Stack2.push(elemento)
      print(Stack2)

li = pilallena()
li.push(5)
li.push(10)
li.push(6)
print(li)
recorrer_y_restaurar(li)
