class person(object):
    def __init__(self,name,age,city,gender ):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
    def eat(self,food):
        print(self.name +" is eating " + food)

    def talk( self , sentence):
        print( sentence)


