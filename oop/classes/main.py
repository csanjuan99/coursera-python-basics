from MyClass import MyClass
from math import pi

# Create an instance of MyClass
my_object = MyClass()  # This will print "Hello from MyClass"

# Print the object's memory address in hex format (0x...)
# print(my_object)

# Print the object's attributes
print(my_object.a)  # print the object's attribute a

# Call the object's method
my_object.hello()  # print "Hello from MyClass.hello()"

# print(math.pi)

# for x in range(1, 4):
#   print(int(str((float(x)))))

sample_dict = {1: "Coffe", 2: "Tea", 3: "Juice"}
for x in sample_dict:
    print(x)




def d():
    color = "green"

    def e():
        nonlocal color
        color = "yellow"

    e()
    print("Color: " + color)
    color = "red"


color = "blue"
d()
