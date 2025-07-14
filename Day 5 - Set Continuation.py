'''thisset = {"apple","banana","Cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple","banana","Cherry"}
thisset.discard("apple")
print(thisset)

thisset = {"apple","banana","Cherry"}
thisset.pop()
print(thisset)

thisset = {"apple","banana","Cherry"}
thisset.clear()
print(thisset)'''

thisset = {"apple","banana","Cherry"}
for x in thisset:
    print(x)

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

x = {"apple","banana","Cherry"}
y = {"google","Amz","apple"}
x.intersection_update(y)
print(x)
