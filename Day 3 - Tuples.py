thistuple = ("apple", "banana", "cherry")
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
