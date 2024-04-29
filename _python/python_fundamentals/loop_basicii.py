#Q1 
print("Q1 -----------------------")
def biggie_size(ll):
    for i in range(len(ll)) :
        
        if(ll[i] > 0):
            ll[i]="big"
       
    return ll
print([-1, 3, 5, -5] ," -> biggie_size( [-1, 3, 5, -5]) -> ",biggie_size( [-1, 3, 5, -5]) )

#Q2
print("Q2 -----------------------")
def count_positives(ll):
    count= 0 
    for i in range(len(ll)):
        if ll[i] > 0 : 
            count =count + 1
    ll[-1] = count 
    return ll

ll = [-1,1,1,1]
print(f" count_positives({ll}) -> ",count_positives(ll))  
ll = [1,6,-4,-2,-7,-2]
print(f" count_positives({ll}) -> ",count_positives(ll)) 

#Q3
print("Q3 -----------------------")
def sum_total(ll):
    sum = 0
    for i in  ll : 
        sum = sum + i 
    return sum         

ll = [1,2,3,4]
print(f" sum_total({ll}) -> ",sum_total(ll))  
ll = [6,3,-2]
print(f" sum_total({ll}) -> ",sum_total(ll))  

#Q4
print("Q4 -----------------------")
def average(ll): 
     return sum_total(ll)/len(ll)

ll = [1,2,3,4]
print(f" average({ll}) -> ",average(ll))  
ll = [6,3,-2]
print(f" average({ll}) -> ",average(ll))  

#Q5 
print("Q5 -----------------------")
def length(ll):
    count =  0 
    for i  in ll : 
        count = count +1 
    return count 
ll = [37,2,1,-9]
print(f" lenght({ll}) -> ",length(ll))  
ll = []
print(f" lenght({ll}) -> ",length(ll))  

#Q6 
print("Q6 -----------------------")
def Minimize(ll):

    if(length(ll)==0):
        return False
    min = ll[0]
    for e in ll : 
        if(e < min):
            min = e 

    return min         

ll = [37,2,1,-9]
print(f" Minimize({ll}) -> ",Minimize(ll))  
ll = []
print(f" Minimize({ll}) -> ",Minimize(ll)) 


#Q7
print("Q7 -----------------------")
def Maximize(ll):

    if(length(ll)==0):
        return False
    max = ll[0]
    for e in ll : 
        if(e > max):
            max = e 

    return max   
ll = [37,2,1,-9]
print(f" Maximize({ll}) -> ",Maximize(ll))  
ll = []
print(f" Maximize({ll}) -> ",Maximize(ll)) 

#Q8
print("Q8 -----------------------")
def ultimate_analysis(ll):
    my_dict={}
    if len(ll) == 0:
        return False
    my_dict['sumTotal'] = sum_total(ll)
    my_dict['average'] = average(ll)
    my_dict['minimum'] = Minimize(ll)
    my_dict['maximum'] = Maximize(ll)
    my_dict['length'] = length(ll)

    return my_dict
ll = [37,2,1,-9]
print(f" ultimate_analysis({ll}) -> ",ultimate_analysis(ll))
ll = [1,2,3,4]
print(f" ultimate_analysis({ll}) -> ",ultimate_analysis(ll))    
ll = []
print(f" ultimate_analysis({ll}) -> ",ultimate_analysis(ll)) 
#Q9
print("Q9 -----------------------")
def reverse_list(ll):
    p1 = 0
    p2 = len(ll)-1

    while(p1 < p2):
        ll[p1],ll[p2] = ll[p2],ll[p1]
        p1 = p1+1 
        p2 = p2-1 
    return ll     
ll = [37,2,1,-9,1]
print(f" reverse_list({ll}) -> ",reverse_list(ll))
ll = [1,2,3,4]
print(f" reverse_list({ll}) -> ",reverse_list(ll))    
ll = []
print(f" reverse_list({ll}) -> ",reverse_list(ll))


