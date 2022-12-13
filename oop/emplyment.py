class Employee:
    def __init__(self, name, last):
        self.name = name
        self.salary = last


class Supervisor(Employee):
    def __init__(self, name, last, password):
        super().__init__(name, last)  # call parent constructor
        self.password = password


class Chef(Employee):
    def leave_request(self, days):
        return "May I have {} days off?".format(days)


if __name__ == "__main__":
    adrian = Supervisor("Adrian", "A", "apple")
    emily = Chef("Emily", "E")
    juno = Chef("Juno", "j")

    print(emily.leave_request(4))
    print(adrian.password)
    print(emily.name)
