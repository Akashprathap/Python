#set

thisset = {"apple","banana","cherry"}
print(thisset)

thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)

thisset = {"apple","banana","cherry"}
print("banana" in thisset)

thisset = {"apple","banana","cherry"}
thisset.add("mango")
print(thisset)

thisset = {"apple","banana","cherry"}
thisset.update(["kiwi","melon","grapes"])
print(thisset)
