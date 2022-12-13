class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


if __name__ == '__main__':
    child = Child('John', 20)
    print(child.get_name())
    print(child.get_age())
