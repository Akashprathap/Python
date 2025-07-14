'''thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "1964"
    }
print(thisdict)

x = thisdict["model"]
print(x)

x = thisdict.get("year")
print(x)

thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "1964"
    }
thisdict["year"] = 2025
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print(x,y)'''


'''thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "1964"
    }
if "model" in thisdict:
    print("yes ,'model' is one of the key in the thisdict dictionary")

print(len(thisdict))'''



'''thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "1964"
    }
thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)'''


thisdict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "1964"
    }
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

thisdict4 = dict(brand = "ford", model = "mustang", year = "1999")
print(thisdict4)


