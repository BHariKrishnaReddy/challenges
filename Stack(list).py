#Creating a stack with python list without size limit

class Stack:
  def __int__(self):
    self.list = []

  #to vizulize the data in proper way. Printing our Stack
  def __str__(self):
    values = self.list.reverse
    values = [str(x) for x in self.list]
    return '\n',join(values)
  

  #isEmpty Operation
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False
  
  #push
  #no size limt in this case so direct push, if there is any size limit then we should checkout for overflow
  def pusp(self,value):
    return self.list.append(value)
  
  #pop
  def pop(self):
    if self.isEmpty():
      return "No elements"
    else:
      return self.list.pop()

  
  #peek
  def peek(self):
    if self.isEmpty():
      return "No elements"
    else:
      return self.list.list(len(self.list)-1) # len(self.list)-1 --> index of last element

  #delete
  def delete(self):
    self.list = None

  
