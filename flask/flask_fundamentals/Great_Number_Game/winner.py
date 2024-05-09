class Winner:
    def __init__(self,name,count) -> None:
        self.name= name 
        self.count = count

    def getWin(self):
        return ""+self.name+"  "+self.count    