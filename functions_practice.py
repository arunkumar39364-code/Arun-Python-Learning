def say_welcome():
    print("Welcome to Python!")

say_welcome()
say_welcome()
def greet_person(person_name):
    print("Hi " + person_name + ", nice to meet you!")

greet_person("arun")
greet_person("speed")

def multiply(num1, num2):
    result = num1 * num2
    return result

answer1 = multiply(5, 3)
print("5 * 3 =", answer1)

answer2 = multiply(10, 4)
print("10 * 4 =", answer2)


def rectangle_area(length, width):
    area = length * width
    return area

my_area = rectangle_area(10, 5)
print("Rectangle area:", my_area)