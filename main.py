// started at 9:33 2-9-2022

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    newList = LinkedList()
    newList.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)
    fourthNode = Node(4)
    fifthNode = Node(5)

    newList.head.next = secondNode
    secondNode.next = thirdNode
    thirdNode.next = fourthNode
    fourthNode,next = fifthNode

def InsertBeg(self, newData):
  newNode = Node(newData)
  newNode.next = self.head
  self.head = newNode

def InsertEnd(self, newData):
  newNode = Node(newData)
  if self.head is None:
    self.head = newNode
    return
  end = self.head
  while(end.next):
    end = end.next
  end.next = newNode

def RemoveNode(self, removeNode):
  currentNode = self.head
  if (currentNode is not None):
    if (currentNode.data == removeNode.data):
      self.head = currentNode.next
      currentNode = None
      return
    while (currentNode is not None):
      if currentNode.data == removeNode.data:
        break
    prev = currentNode
    currentNode = currentNode.next

  if (currentNode == None):
    return

  prev.next = currentNode.next

  currentNode = None
  
# Python code wars made a vowel counter
  
  def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels
# Cool code
# Ended at 9:33
