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


li = pila()
li.push(5)
li.push(10)
li.push(6)
print(li.peek())
print(li.pop())
print(li.Stack)