


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
        self.lenght = self.lenght+1
        return self

    def print_values(self):
        current = self.head 
        while(current): 
            print(current.val,end=" --->> ")
            current = current.next 
        print(f"Null     (N={self.lenght})")
        
        return self

    def add_to_back (self,val):
        newNode = SNode(val)
        current = self.head 
        while(current.next): 
            current= current.next
        current.next = newNode 
        self.lenght = self.lenght+1
        return self                     

    def remove_from_front(self):
        if not self.head: 
            return self
        removeNode = self.head 
        self.head = self.head.next
        removeNode = None
        self.lenght = self.lenght-1
        return self

    def remove_from_back(self):
        if not self.head: 
            return self
        elif self.head.next == None : 
            self.head= None
        else :        
            current = self.head 
            while(current.next):
                if(current.next.next == None):
                    break 
                current = current.next 
            removeNode = current.next 
            current.next= None
        self.lenght = self.lenght-1
        return self
    
    def remove_val(self, val):
        current = self.head 
        if not self.head: 
            return self
        if(current.val == val ):
            self.remove_from_front()
        else: 
            while(current.next):
                if(current.next.val==val):
                    break 
                current = current.next
            if current.next.val ==val:    
                removeNode=current.next
                current.next = removeNode.next
                removeNode.next = None    
                self.lenght = self.lenght-1
        return  self   

    def insert_at(self, val, n):
        
        if n >= self.lenght or n < 0: 
            return self
        
        if n==0 : 
            self.add_to_front(val)
        else: 
            newNode= SNode(val)
            current = self.head
            for i in range(n-1):
                current = current.next

            newNode.next = current.next
            current.next = newNode
            self.lenght = self.lenght+1
        
        return  self        




obj = SList() 
obj.remove_val(2).print_values()
obj.add_to_front(1).print_values()
obj.add_to_front(2).print_values()
obj.add_to_front(3).print_values()

obj.add_to_back(4).print_values()
obj.add_to_back(5).print_values()
obj.insert_at(6,3).print_values()
obj.insert_at(7,3).print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
obj.remove_from_front().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()
# obj.remove_from_back().print_values()






    