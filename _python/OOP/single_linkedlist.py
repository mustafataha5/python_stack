


class SNode:
    def __init__(self,val) :
        self.val = val 
        self.next = None

class SList:
    def __init__(self) :
        self.head = None
        self.lenght= 0 

    def add_to_front(self,val):
        newNode = SNode(val)
        newNode.next = self.head
        self.head = newNode
        return self

    def print_values(self):
        current = self.head 
        while(current): 
            print(current.val,end=" --->> ")
            current = current.next 
        print("Null")

    def add_to_back (self,val):
        newNode = SNode(val)
        current = self.head 
        while(current.next): 
            current= current.next
        current.next = newNode 
        return self                     

    def remove_from_front(self):
        removeNode = self.head 
        self.head = self.head.next
        removeNode = None
        return self

    def remove_from_back(self):        
        current = self.head 
        while(current.next): 
            current = current.next 
        removeNode = current.next 
        return self
    








    