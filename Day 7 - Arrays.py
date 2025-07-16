cars = ["BMW","FORD","VOLVO"]
for x in cars:
    print(x)

cars = ["BMW","FORD","VOLVO"]
cars.sort()
print(cars)

cars = ["BMW","FORD","VOLVO"]
cars.reverse()
print(cars)

cars = ["BMW","FORD","VOLVO","FORD"]
print(cars.count("FORD"))

cars = ["BMW","FORD","VOLVO"]
Bikes = ["Yamaha","Bajaj","Honda"]
cars.extend(Bikes)
print(cars)

cars = ["BMW","FORD","VOLVO"]
cars.insert(3,"Honda")
print(cars)
