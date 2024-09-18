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

lakshan = ["sachintha","madhushan","pinsara","aasdd"]

i = 0

while i < len(lakshan):
    print(lakshan[i])

    i = i + 1

#List sort

newli = [122,3,4,5,6,777,89]

newli.sort()
print(newli)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()
print(thislist)

print("-------------------------")

thislist.sort(reverse=True)
print(thislist)

print("-----------------------------")

arryli = [1,2,3,4,5,6,7]

for x in arryli:
    print(x)

print("----------------------------")

arryli.sort(reverse=True)
for x in arryli:
    print(x)

print("---------------------------")

listr = ["apple","banana","cherry","lakshan","man"]

saclak = listr.copy()

print(saclak)
print(listr)

print("------------------")

list1 = ["a","b","c","d"]
list2 = [1,2,3,4]

for i in list2:
    list1.append(i)
   
print(list1)

#another way

list3 = ["orange","banana","apple","grapes"]
list4 = [1,2,3,4,5]

list3.extend(list4)
print(list3)


