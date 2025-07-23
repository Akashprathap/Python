#Python Modules

'''import module
module.greeting("AKASH")'''

'''import module
a = module.person1["age"]
print(a)'''

'''import module as md
a = md.person1["name"]
print(a)'''

'''from module import greeting
print(greeting("Akash"))
print(person1["age"])
print(person1["name"])'''

'''import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2025,11,30)
print(y)
print(y.strftime("%B"))'''


#JSON

'''import json
x = '{"name":"John","age":30,"city":"Dublin"}'
y = json.loads(x)
print(y["age"])

import json
x = {
    "name":"John",
    "age":30,
    "city":"Dublin"
    }
y = json.dumps(x)
print(y)

import json
print(json.dumps({"name":"John","age":30}))
print(json.dumps(["apple","banana"]))
print(json.dumps("hello"))'''



'''import json
x = {
    "name":"John",
    "age":30,
    "city":"Dublin",
    "Married" : True,
    "Divorced" : False,
    "Children" : ("Ann","Belly"),
    "pets": None,
    "cars" : [
        {"Model": "BMW 320", "mpg": 27.5},
        {"Model": "Ford", "mpg": 24.1}
        ]
    }
print(json.dumps(x))
print(json.dumps(x, indent=4, separators = (".","=")))
print(json.dumps(x, indent=4, sort_keys = True))'''

#RegEx

'''import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if(x):
    print("YES! we have a match!")
else:
    print("NO match")'''


'''import re
str = "The rain in Spain"
x = re.findall("ai",str)
x = re.findall("Portugal",str)
print(x)
if(x):
    print("yes")
else:
    print("No")


import re
str = "The rain in Spain"
x = re.search("\s",str)
print("The first whitespace:", x.start())



import re
str = "The rain in Spain"
x = re.split("\s",str)
print(x)
y = re.split("\s",str,1)
print(y)

import re
str = "The rain in Spain"
x = re.sub("\s","9",str,2)
x = re.search("ai",str)
print(x)'''

import re
str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.span())
print(x.string)
print(x.group())



#PIP

import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

