#Class and objects

'''class myclass:
    x = 5
print(myclass)'''

'''class myclass:
    x=5
p1 = myclass()
print(p1.x)'''

'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("John",34)
print(p1.name)
print(p1.age)'''

'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+ self.name)
        print("and my age is",self.age)
P1 = person("john",34)
P1.myfunc()'''

#modify
'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is ", self.name)
        print("age",self.age)
p1 = person("John",34)
p1.age = 44
print(p1.age)'''

#del

'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is ", self.name)
p1 = person("jacob",45)
del p1
print(p1)'''

#child class

'''class person:
    def __init__(self,fname,iname):
        self.firstname = fname
        self.lastname = iname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    pass
x = student("Mike","Oslen")
x.printname()'''

#Add init function

'''class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self, fname,lname):
        person.__init__(self,fname,lname)
x = student("mike","oslen")
x.printname()'''




#Add


'''class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
        self.year = 2019
x = student("mike","oslen")
x.printname()
print(x.year)'''


'''
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        person.__init__(self,fname,lname)
        self.gradyear = year
x = student("mike","oslen","2019")
x.printname()
print(x.gradyear)'''


class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        person.__init__(self,fname,lname)
        self.gradyear = year
    def welcome(self):
        print("welcome", self.firstname,self.lastname, "to the class",self.gradyear)
x = student("mike","osllen",2019)
x.welcome()
