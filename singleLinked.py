#singleLinkd
import itertools
class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None
class SL:
  def __init__(self):
    self.head=None
    self.tail=None

  #Travesal
  def travesel(self):
    if self.head==None:
      return "Empty list"
    else:
      temp=self.head
      while temp is not None:
        print(temp.value)
        temp=temp.next

  #itertion
  def _iter_(self):
    temp= self.head
    while temp:
      yield temp
      temp=temp.next

  #Insertion
  def insert(self,value,l):
    nn = Node(value)
    if self.head==none and self.tail==none:
      print("empty")
      self.head=nn
      self.tail=nn
    elif l==1:
      nn.next=self.head
      self.head=nn
    elif l==-1:
      self.tail.next=nn
      self.tail=nn
    else:
      temp,index=self.head,0
      while index<l-1:
        temp=temp.next
        i+=1
      nxtnode=temp.next
      temp.next=nn
      nn.next=nxtnode

  #deletion
  def delete(self,l):
    if self.head==None:
      return "Empty list"
    elif l==0:
      self.head= self.head.next
    elif l==-1:
      temp=self.head
      while temp is not None:
        if temp.next==self.tail:
          break
        temp=temp.next
      temp.next=None
      self.tail=temp
    else:
      temp,i=self.head,0
      while i<l-1:
        temp=temp.next
        i+=1
      nxtnode = temp.next
      temp.next=n.next
