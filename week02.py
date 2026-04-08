def greet(name):
    print("Hello, " + name)
greet("Ivan")

def describe (name, age):
    print ("My name is " + name + " and I am " + str(age) + " years old.")
describe ("Ivan", 27)

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
print(is_adult(27))
