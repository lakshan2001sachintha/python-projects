a = 33
b = 200

if a>b:
    print("a is greter than b")
else :
    print("b is greater than a")  

print("------------------------")

a = 33
b = 200

if not a>b:
    print("sachintha lakshan")
else :
    print("lakshan sachintha")    

print("----------LOOPS--------")

i = 1
while i < 100:
    i+=1
    
    if(i%10==0):
        continue
    print(i)     

print("------------Functions----------------")       
print("\n")
#def lakshan():
 #   print("My name is sachintha lakshan")

#lakshan()    

def my_func():
    print("my name is lakshan sachintha munasinghe")

my_func()
print("\n")

def my_lak(age =0,name ="enter your name !"):
    print("My name is :",name," My age is :",age)

my_lak(23,"lakshan")
my_lak()

print("-----------------------")

def nam_func(names):
    for x in names:
        print(x)

nam = ["lakshan","sachintha","munasinghe"]
nam_func(nam)                  

