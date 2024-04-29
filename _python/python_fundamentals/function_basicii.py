

#Q1 


def Countdown(num):
    newlist=[]

    for i in range(num,-1,-1):
        newlist.append(i)
    return newlist
print("------------------------- Q1")
print("Q1 -> ",Countdown(5))

#Q2 
print("------------------------- Q2")
def print_and_return(ll):
    print(ll[0])
    return ll[1]

x=print_and_return([1,2])
print("Q2 -> ",x)
#Q3
print("------------------------- Q3")
def first_plus_length(ll):
    return ll[0]+len(ll)
a=[1 ,2,3,4,7,8,5,6]
print(a," -> first_plus_length(l) -> ",first_plus_length(a))

#Q4
print("------------------------- Q4")
def values_greater_than_second(ll):
    list_length = len(ll)
    if(list_length <= 2):
        return False
    else: 
        newList = [] 
        count = 0 
        for i in range(list_length): 
            if(ll[1] < ll[i]):
                newList.append(ll[i])
                count = count + 1 
        print("Count",len(newList))
        return newList
a =   [5,2,3,2,1,4]              
print(a," > values_greater_than_second(a) ->")
print(values_greater_than_second(a))
a = [5,2]
print(a," > values_greater_than_second(a) ->",values_greater_than_second(a))

#Q5
print("------------------------- Q5")
def length_and_value(size,num):
    newlist = []
    for i in range(size): 
        newlist.append(num)
    return newlist

print("  length_and_value(4,7) -> ", length_and_value(4,7))  
print("  length_and_value(5,3) -> ", length_and_value(5,3))   








