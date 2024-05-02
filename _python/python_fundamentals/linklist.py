

class Node: 
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkList:
    def __init__(self) -> None:
     self.head = None 

    def insertToTail(self,data): 
       newNode = Node(data)

       if(self.head == None):
          self.head = newNode
       else: 
          temp = self.head 
          while(temp.next):
             temp = temp.next
          temp.next = newNode 
       

    def printList(self): 
       temp = self.head 
       while(temp):
          print(temp.data,end=" ----> " if temp.next != None else " ----> Null\n" )
          temp = temp.next


mylist = LinkList()
mylist.insertToTail(5)
mylist.printList()
mylist.insertToTail(4)
mylist.printList()











