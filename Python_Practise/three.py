#a = 33
#b = 200

#if a>b:
 #   print("a is greter than b")
#else :
 #   print("b is greater than a")  

#print("------------------------")

 # a = 33
#b = 200

#if not a>b:
    #print("sachintha lakshan")
#else :
    #print("lakshan sachintha")    

#print("----------LOOPS--------")

#i = 1
#while i < 100:
    #i+=1
    
    #if(i%10==0):
       # continue
    #print(i)     

#print("------------Functions----------------")       
#print("\n")
#def lakshan():
 #   print("My name is sachintha lakshan")

#lakshan()    

#def my_func():
   # print("my name is lakshan sachintha munasinghe")

#my_func()
#print("\n")

#def my_lak(age =0,name ="enter your name !"):
    #print("My name is :",name," My age is :",age)

#my_lak(23,"lakshan")
#my_lak()

#print("-----------------------")

#def nam_func(names):
    #for x in names:
       # print(x)

#nam = ["lakshan","sachintha","munasinghe"]
#nam_func(nam)                 

#print("-----------------------------")

#print("What is your age ?")
#age = input()
#print("your age is : ",age)

#print("lakshan"+"sachintha")

#var = "123"
#print(type(var))

#print(type(3.0))

#names = ["lakshan","sachintha","munasinghe","rajapaksha"]

#for x in names:
 #   print(x)

#print("print fist 100 numbers in python by for loop")

#for i in range(1,101):
#    print(i)
  
#arr1 = ["red","blue","yellow"]
#arr2 = ["apple","orange","cherry"]

#for x in arr1:
#   for y in arr2:
#        print(x,y)

#def lakshan(name,age):
#    print("my name is :",name," my age is ",age)


#lakshan("lakshan",23)

#def my_function(**kid):
#    print("His last name is " + kid["lname"])  

#my_function(fname = "lakshan",lname = "sachintha")          

#def my_func(country = "sri lanka",name = "xzoy"):
#    print("my name is :",name," My country is :",country)


#my_func()
#my_func("lakshan","new zealand")
#my_func("sachintha","India")
#my_func()

#def raky(food):
#    for x in food:
#        print(x)
#fruits = ["banana","apple","orange","jhd"]
#raky(fruits) 

#def lakshan(x):
 #   return 5*x

#print(lakshan(23))    

#def lakshan(x):
#    print(x)

#lakshan(x=34)

#print("Python Array")

#cars = ["BMW","Benz","toyota","wva"]

#for x in cars:
#    cars[1] ="lakshan"
#    print(x)

#x = len(cars)

#print(x)

#cars.append("sachintha")

#print(cars)

print("Clases and Object")

class Myclass:
    x = 34

p1 = Myclass()
p2 = Myclass()
print(p1.x)
print(p2.x)

print("-------------------")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Lakshan",23)
print(p1.name)
print(p1.age)        
   
print("---------__str__()------------")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("lakshan",23)

print(p1)

print("----------lakshan------------")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+self.name+" Your age is "+self.age)

p1 = Person("Lakshan",23)
p1.myfunc()




