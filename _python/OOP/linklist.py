class Node: 
    def __init__(self,val): 
        self.val = val
        self.next=None 
     

class MyLinkedList(object):

    def __init__(self):
        self.head = None   
        self.size = 0    

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size-1 or self.head == None: 
            return -1 
        else : 
            temp = self.head 
            for i in range(index):
                    temp = temp.next

            return temp.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size: 
            return 
        newNode = Node(val)
        current = self.head
        if(index <= 0):
            newNode.next = current
            self.head = newNode
        else: 
            for i in range(index-1):
                current = current.next

            newNode.next = current.next
            current.next = newNode    

        self.size  = self.size + 1        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        
        if index == 0 : 
            temp = self.head
            self.head = self.head.next 
            temp.next = None
            del temp 
        else: 
            current = self.head
            for i in range(index-1):
                if current.next : 
                    current = current.next
                else: 
                    return  
            if  current.next :                      
                removeNode = current.next 
                current.next = removeNode.next
                removeNode.next = None
                del removeNode
            else: 
                return
        self.size = self.size - 1 
    
    def print_list(self): 
        temp = self.head 
        while temp : 
            print(temp.val,end=" ---> ")
            temp = temp.next

        print("Null")        
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.print_list()
obj.addAtHead(4)
obj.print_list()
obj.get(1)
obj.addAtTail(4)
obj.print_list()
print("get(1)",obj.get(1))

obj.addAtIndex(2,3)
obj.print_list()
obj.addAtIndex(4,66)
obj.print_list()
obj.deleteAtIndex(1)
obj.print_list()
print("get(1)",obj.get(1))