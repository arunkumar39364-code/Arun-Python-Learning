# Functions in Python
# A function is reusable code

# Define a function
def greet(name):
    print("Hello, " + name + "!")

# Define another function
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

# Use the functions
greet("arun")
greet("speed")

# Math functions
sum_result = add(10, 5)
print("10 + 5 =", sum_result)

diff_result = subtract(10, 5)
print("10 - 5 =", diff_result)

product_result = multiply(10, 5)
print("10 * 5 =", product_result)