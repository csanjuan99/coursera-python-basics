class MyClass:
    a = 1
    print("Hello from MyClass")  # This will print when the class is loaded

    def hello(self):  # self is a reference to the object, if not used, the method will not be able to access the
        # instances object's attributes
        print("Hello from MyClass.hello()")

    pass  # I don't want to write anything here just yet
