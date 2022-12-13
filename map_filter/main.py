menu = ["latte", "cappuccino", "espresso", "americano", "mocha", "macchiato"]


def get_coffee(coffee):
    if coffee[0] == "m":
        return coffee
    else:
        return None


for item in map(get_coffee, menu):  # map() executes the function on each item in the list and returns a map object
    # with None values in the same list
    print(item)

print("\n")
for item in filter(get_coffee, menu):  # filter() executes the function on each item in the list and returns a filter
    # object with only the values that return True not None values
    print(item)


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)
