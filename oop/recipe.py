class Recipe:
    def __new__(cls: type[Self]) -> Self:  # method to create a new empty object
        pass

    # def __init__(self) -> None:  # method to initialize the object with values, this is a constructor
    #     pass

    def __init__(self, dish, items, cooking_time) -> None:
        self.dish = dish
        self.items = items
        self.cooking_time = cooking_time

    def contents(self):
        print(f"{str(self.dish)} contains {str(self.items)} and takes {str(self.cooking_time)} minutes to cook.")


if __name__ == "__main__":
    pasta = Recipe("Pasta", ["Pasta", "Tomato Sauce", "Cheese"], 30)
    pizza = Recipe("Pizza", ["Pizza Dough", "Tomato Sauce", "Cheese"], 20)
    pasta.contents()
    pizza.contents()
