
class Animal: 
    def __init__(self,name,age,health,happiness) -> None:
        self.name = name 
        self.age = age 
        self.health =health
        self.happiness = happiness
    
    def display_info (self):
        print(f"Name: {self.name}   ,Health: {self.health}   ,Happiness: {self.happiness}")    
        return self
    
    def feed (self):
        self.happiness = self.happiness +10
        self.health = self.health + 10
        return self

class Lion(Animal):
    def __init__(self, name, age=1, health=40, happiness=40,type = "African-Lion") -> None:
        super().__init__(name, age, health, happiness)
        self.type = type

    def feed(self):
        self.happiness =  self.happiness + 5
        self.health = self.health + 7   
        return self
    
    def display_info (self):
        print(f"Name: {self.name}   ,Type:  {self.type}   ,Health: {self.health}   ,Happiness: {self.happiness}")
        return self
class Tiger(Animal): 
    def __init__(self, name, age=1, health=70, happiness=60,isWhite=False) -> None:
        super().__init__(name, age, health, happiness)
        self.isWhite = isWhite
    def display_info (self):
        print(f"Name: {self.name}   ,IsWhite:  {self.isWhite}   ,Health: {self.health}   ,Happiness: {self.happiness}")    
        return self
    
    def feed(self):
        self.happiness =  self.happiness + 8
        self.health = self.health + 12  
        return self
    
class Bear(Animal):
    def __init__(self, name, age=1, health=70, happiness=60,type="Black-Brown") -> None:
        super().__init__(name, age, health, happiness)
        self.tpye =  type

    def feed(self):
        self.happiness =  self.happiness + 8
        self.health = self.health + 12  
        return self
    
    def display_info (self):
        print(f"Name: {self.name}   ,Type:  {self.type}   ,Health: {self.health}   ,Happiness: {self.happiness}")
        return self
    
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name,isWhite=False):
        self.animals.append( Tiger(name,isWhite=isWhite) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah",isWhite=True)
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
