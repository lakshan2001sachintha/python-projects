#Lists ////////////////////////////
mylist = ["apple","banana","cherry"]
print(mylist," and type is :",type(mylist))

mylist[0] = "lakshan"
print(mylist)

print(len(mylist))

nums = [1,2,3,4,5,6]
print(nums," and type is :",type(nums))

onelist = ["smith","nick","lakshan","ishan","karan","rajapaksha"]
print(onelist[1:5])

if "bhashitha" in onelist:
    print("Yes 'bhashitha' is in the list")
else:
    print("No")

print("-----------------------------")

onelist[2:4] = ["vishmi","nethsara"]
print(onelist)

print("-----------------------------")

onelist.insert(3,"kaveen")
print(onelist)

onelist.append("bananananan")
print(onelist)

print("-----------------------------")

num1 = [1,2,3,4,5,6]
num2 = [7,8,9,10,11,12]

num1.extend(num2)
print(num1)

print("-----------------------")

twolist = ["apple","banana","woodapple"]
twolist.insert(2,"lakshan")
print(twolist)

for x in twolist:
    print(x)

for i in range(len(twolist)):
    print(i)