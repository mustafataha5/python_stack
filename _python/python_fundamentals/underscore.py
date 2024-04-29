class Underscore:
    def map(self, iterable, callback):
        new_list=[]
        for i in iterable:
            new_list.append(callback(i))
        return new_list    
        
        # your code here
    def find(self, iterable, callback):
        # your code here
        new_list = [] 
        for i in iterable: 
            if(callback(i)):
                new_list.append(i)
        return new_list        
    
    def filter(self, iterable, callback):
        # your code
        new_list=[]
        for i in iterable:
            if(callback(i)):
                new_list.append(i)
        return new_list
        
    def reject(self, iterable, callback):
        # your code
        new_list=[]
        for i in iterable:
            if(not callback(i)):
                new_list.append(i)
        return new_list
        
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
# should return [2, 4, 6] after you finish implementing the code above
print(_.map([1,2,3], lambda x: x*2) )# should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]

