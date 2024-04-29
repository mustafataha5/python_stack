

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print("Before : ",x)
x[1][0] = 15
print("After : ",x)

print("Before : ",students)
students[0]['last_name'] ='Bryant'
print("After : ",students)

print("Before : ",sports_directory)
sports_directory['soccer'][0] ='Andress'
print("After : ",sports_directory)
print("Before : ",z)
z[0]['y'] = 30
print("After : ",z)


def iterateDictionary(my_list): 
    for my_dict in my_list: 
        for key,value in my_dict.items(): 
            print(key,"-",value,end=" , ")
        print("") 

def iterateDictionary2(key_name, my_list):
    print("----->>> Key :",key_name)
    for my_dict in my_list: 
            if str(key_name) in my_dict : 
                print(my_dict[str(key_name)])
            else:
                 print(f"Error : key { {key_name} } is not found in this dictionary" )    

def printInfo(my_dict): 
     for key in my_dict:
          print("-----------------") 
          print(len(my_dict[key])," ",key) 
          for ele in my_dict[key]:
               print(ele)
                 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

