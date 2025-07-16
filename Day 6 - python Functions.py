'''def my_function():
    print("hello from the function")
my_function()'''

'''def my_function(fname):
    print(fname + "welcome")
my_function("emil")
my_function("john")'''


'''def my_function(country = "Norway"):
    print("I am from " + country)
my_function("sweden")
my_function("india")
my_function()
my_function("Brazil")'''

'''def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)'''


'''def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(9))'''

'''def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num = 5
print("The factorial of ", num, "is", factorial(num))'''

def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\n Recursion Example result")
tri_recursion(6)
