'''thislist = ["apple","banana", "Cherry"]
print(thislist)
print(thislist[1])
print(thislist[2])
print(thislist[0])

thislist = ["apple", "banana", "Chery", "Avocado"]
thislist[1] = "guava"
thislist[3] = "watermelon"
print(thislist)

thislist = ["apple","banana", "Cherry"]
for x in thislist:
    print(x)

thislist = ["apple","banana", "Cherry"]
if "banana" in thislist:
    print("yes, 'banana' is a fruit in this list")

thislist = ["apple","banana", "Cherry"]
print(len(thislist))

thislist = ["apple","banana", "Cherry"]
thislist.append("grapes")
print(thislist)

thislist.insert(2, "orange")
print(thislist)'''

thislist = ["apple","banana", "Cherry"]
thislist.remove("Cherry")
print(thislist)

thislist = ["apple","banana", "Cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple","banana", "Cherry"]
del thislist[0]
print(thislist)

thislist = ["apple","banana", "Cherry"]
del thislist

thislist = ["apple","banana", "Cherry"]
thislist.clear()
print(thislist)


thislist = ["apple","banana", "Cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple","banana", "Cherry"]
mylist = list(thislist)
print(mylist)

