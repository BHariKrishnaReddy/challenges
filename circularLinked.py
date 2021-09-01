#circularLinked
class Node:
  def __init__(self,value):
    self.value=value
    self.next=none
class Cl:
  def __init__(self):
    self.head=None
    self.tail=None
  
  #insertoin
  def cinsert(self,val,l):
    newNode = Node(val)
    if self.head==None:
      print("Empty list so creating with this element")
      self.head=newNode
      self.tail=newNode
    elif l = 0:
      #start position
      self.tail.next=self.head.next
      self.head = self.head.next

    elif l = -1:
      #endpostion
      newNode.next = self.tail.next
      self.tail.next=newNode
      self.tail=newNode
      
    else:
      temp.i=self.head,0
      while i<l-1:
        temp=temp.next
        i=+1
      nextnode = temp.next
      temp.next=newNode
      newNode.next=nextnode

  #deletion
  def cdelet(self,val,l):
    if self.head==None:
      return "Empty list"
    elif l == 0:
      #start position
      self.head=self.head.next
      self.tail.next=self.head
    elif l == -1:
      #endpostion
      temp=self.head
      while temp is not None:
        if temp.next==self.tail:
          break
        temp=temp.next
      temp.next=self.head
      self.tail=temp
    else:
      temp.i=self.head,0
      while i<l-1:
        temp=temp.next
        i=+1
      nextnode = temp.next
      temp.next=nextnode.next
      
