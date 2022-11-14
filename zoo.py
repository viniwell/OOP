import random
class Pet:
    global animals
    animals=[]
    def __init__(self,type,name,boredom=random.randint(0,10),food=random.randint(0,10)):
        self.type=type
        self.name=name
        self.boredom=boredom
        self.food=food
        animals.append(self)
    def eating():
        for i in animals:
            i.food+=1
            