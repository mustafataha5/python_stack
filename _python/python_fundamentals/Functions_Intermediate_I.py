import random
def randInt(min= 0  , max=  100 ):
    if max < 0 : 
        print(f"Error :max < 0 --> {max} < 0 ")
        return None 
    elif(min > max): 
        print(f"Error: min > max --> {min} > {max} ")
        return None

    else : 
        num = random.random()*(max-min) + min
        num = round(num)
        return num

#should print a random integer between 0 to 100
print(randInt()) 		
# should print a random integer between 0 to 50
print(randInt(max=50))
# should print a random integer between 50 to 100
print(randInt(min=50)) 
#should print a random integer between 50 and 500	    
print(randInt(min=50, max=500))    
print(randInt(min=1000, max=500)) 
print(randInt(max=-1)) 