'''thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "Cherry")
print(thistuple[2])
print(thistuple[0])

thistuple = ("apple", "banana", "Cherry")
thistuple[1] = "blackcurrent"
print(thistuple)

thistuple = ("apple", "banana", "Cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "Cherry")
for x in range(len(thistuple)):
    print(thistuple[x])

thistuple = ("apple", "banana", "Cherry", "guava", "watermelon")
for i in range(0,4):
    print(thistuple[i])

thistuple = ("apple", "banana", "Cherry", "guava", "watermelon")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

tuple1 = ("a",96,"b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "Cherry", "guava", "watermelon")
mytuple = fruits * 2
print(mytuple)

thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.count(1)
print(x)

thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.index(6)
print(x)

thistuple = ("apple", "banana", "Cherry")
if "apple" in thistuple:
    print("yes, 'apple' is in the fruit tuple")

thistuple = ("apple",)
print(type(thistuple))

tuple1 = ("apple", "banana", "Cherry")
tuple2 = (1,5,7,9,3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 55, "male")
print(tuple1)

thistuple = ("apple", "banana", "Cherry")
print(type(thistuple))

thistuple = ("apple", "banana", "Cherry")
del thistuple
print(thistuple)

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "Cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "Cherry","orange","kiwi", "avocado", "melon")
print(thistuple[3:6])

thistuple = ("apple", "banana", "Cherry","orange","kiwi", "avocado", "melon")
print(thistuple[:1])

thistuple = ("apple", "banana", "Cherry","orange","kiwi", "avocado", "melon")
print(thistuple[3:])

thistuple = ("apple", "banana", "Cherry","orange","kiwi", "avocado", "melon")
print(thistuple[-3:-1])


x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "avocado"
x = tuple(y)
print(x)

thistuple = ("appple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("appple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("appple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)

fruits = ("appple", "banana", "cherry")
print(fruits)

fruits = ("appple", "banana", "cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

thistuple = ("appple", "banana", "cherry", "strawberry","blueberry","rasberry")
(green,yellow,*red) = thistuple
print(green)
print(yellow)
print(red)

thistuple = ("appple", "banana", "cherry","mango","orange","pineapple")
(green,*tropic,red) = thistuple
print(green)
print(tropic)
print(red)'''


            



