#1
def a():
    return 5
print(a()) # 5 
#output:
# 5 
print("-------------------------------")
#2
def a():
    return 5
print(a()+a()) # 10 
#output:
# 10
print("-------------------------------")
#3
def a():
    return 5
    return 10
print(a()) #5
#output
# 5
print("-------------------------------")
#4
def a():
    return 5
    print(10)
print(a()) #5
#output:
# 5
print("-------------------------------")
#5
def a():
    print(5) # 5 
x = a()  # will print 5 from the function 
print(x) #x = None so nothing will print
#output:
# 5
# None
print("-------------------------------")
#6
def a(b,c):
    print(b+c)  
#print(a(1,2) + a(2,3)) # a(1,2) will print 3 reutrun None ,a(2,3) will print 5 return None (None+None)=None
# 3 
# 5 
# case Error (None+None) 
print("-------------------------------")
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) #25
#output:
# 25
print("-------------------------------")
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7

print(a()) # print 100 and return 10 and print 10 
#output:
# 100 
# 10 
print("-------------------------------")
#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #7
print(a(5,3)) #14
print(a(2,3) + a(5,3)) #21
#output:
# 7
# 14
# 21 
print("-------------------------------")
#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))#8
#output:
# 8
print("-------------------------------")
#11
b = 500
print(b) #500
def a():
    b = 300
    print(b)# 300
print(b)#500
a()
print(b)#500
#output:
# 500 
# 500 
# 300 
# 500
print("-------------------------------")
#12
b = 500
print(b) #500
def a():
    b = 300
    print(b) # 300
    return b
print(b)# 500 
a()
print(b)# 500 
#output:
# 500 
# 500 
# 300 
# 500
print("-------------------------------")

#13
b = 500
print(b) # 500 
def a():
    b = 300
    print(b) # 300
    return b
print(b)# 500 
b=a()
print(b) # 300
#output:
# 500 
# 500 
# 300 
# 300
print("-------------------------------")
#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#output:
# 1 
# 3 
# 2 
print("-------------------------------")
#15
def a():
    print(1) # 1
    x = b() 
    print(x) # 5 
    return 10
def b():
    print(3) #3
    return 5
y = a()
print(y) # 10
#output:  
# 1 
# 3
# 5
# 10



















 