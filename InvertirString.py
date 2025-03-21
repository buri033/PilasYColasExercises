class Pila():
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

  def __len__(self):
    return len(self.Stack)

  def __repr__(self):
    return str(self.Stack)

def invertir_string(string:str):
  pila = Pila()

  for palabra in string:
    print(palabra)
    pila.push(palabra)

  string = ""
  for j in range(len(pila)):
    print(string)
    string += pila.pop()

  return string

invertir_string("hola")