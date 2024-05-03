


class Node: 
    def __init__(self,val) -> None:
        self.val = val
        self.next= None
        self.prev = None 

class DoubleLinkList:
    def __init__(self) -> None:
        self.head= None 
        self.tail = None 
        self.size = 0

    def insert_at_head(self,val):
        self.insert_at(0,val)
        return self
    
    def insert_at_tail(self,val):
        self.insert_at(self.size,val)
        return self
    
    def insert_at(self,index,val):
        if index < 0 or index > self.size:
            print(f"Error: index({index}) out of range")
            return self

        newNode = Node(val) 
        if(index == 0): #at the begining
            if self.head == None:
                self.head= newNode
                self.tail = newNode 
            else: 
                self.head.prev = newNode
                newNode.next=self.head
                self.head= newNode    

        elif index == self.size: # at the end 
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail = newNode
        
        else:                   # at index n 
            if index <= self.size/2 :
                temp =self.head
                for i in range(index-1): 
                    temp = temp.next
                
            else:
                temp = self.tail
                for i in range(self.size,index,-1):
                    temp = temp.prev   
 
            newNode.next = temp.next
            temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp      
        self.size = self.size + 1    
        return self    

    def remove_head(self):
        self.remove_at(0)
        return self

    def remove_tail(self):
        self.remove_at(self.size-1)
        return self
    
    def remove_at(self,index):
        if index < 0 or index >= self.size:
            print(f"Error: index({index}) out of range")
            return self
        if index == 0 :
            if self.size == 1 : 
                self.head = None 
                self.tail = None
            else: 
                self.head =self.head.next
                self.head.prev= None
                
        elif index == self.size-1 : 
            self.tail = self.tail.prev
            self.tail.next=None
        else: 
            if index <= self.size/2 :
                temp =self.head
                for i in range(index-1): 
                    temp = temp.next
                
            else:
                temp = self.tail
                for i in range(self.size,index,-1):
                    temp = temp.prev

            removeNode = temp.next
            temp.next = removeNode.next
            removeNode.next.prev = temp 
            removeNode.next= None
            removeNode.prev= None    
        self.size = self.size-1
        return self

    def print_list(self): 
        temp = self.head 
        while temp : 
            print(temp.val,end=" <---> ")
            temp = temp.next
        if self.head != None :     
            print(f"Null    N=({self.size})  head=({self.head.val})  tail=({self.tail.val})")
        else : 
            print(f"Null    N=({self.size})  head=(Null)  tail=(Null)")
        return self  
    
    def print_at(self,index):
        if index < 0 or index >= self.size:
            print(f"Error: index({index}) out of range")
            return self
        if index == self.size-1:
            print(f"<---> {self.tail.val} <---> Null")
        elif index == 0 : 
            print(f"{self.head.val} <---> ")
        else : 
            temp = self.head 
            for i in range(index):
                temp=temp.next
            print(f"<---> {temp.val} <--->")    
        return self
    
   

obj = DoubleLinkList()
obj.insert_at_head(1).print_list()
obj.insert_at_head(2).print_list()
obj.insert_at_head(3).print_list()
obj.insert_at(1,7).print_list()
obj.insert_at_tail(4).print_list()
obj.insert_at_tail(5).print_list()
obj.insert_at_tail(6).print_list()
obj.insert_at(3,7).print_list()
obj.insert_at(5,8).print_list()
obj.remove_head().print_list()
obj.remove_head().print_list()
obj.remove_head().print_list()
obj.remove_tail().print_list()
obj.remove_tail().print_list()
obj.remove_at(2).print_list()
obj.remove_head().print_list()
