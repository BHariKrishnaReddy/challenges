#write the class for node and single linked list 
from LinkedList import LinkedList ,Node

def intersection (list1,list2):

  if list1.tail is not list2.tail:
    #as per conditions checking whether the tail is same or not
    return "They are not intersecting"
  lenA,lenB = len(list1),len(list2) #this function is created in my linkedList program so importing it 

  shoter = list1 if lenA <lenB else list2 #finding shorter linkedList
  longer = list2 if len<lenB else list1

  dif = len(longer) - len(shorter)

  longerNode =  longer.head
  shorterNode = shorter.head

  for i in range(dif):
    longerNode = longerNode.next # we are moving our pointer to avoid excess nodes from longer liked list


  while shorterNode is not longerNode:
    shorterNode = shorterNode.next
    longerNode = longerNode.next
  return longerNode
