class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            print(f"{self.name} has been paid {str(self.amount)}")  # should be return
        else:
            print(f"{self.name} has not been paid")  # should be return


if __name__ == "__main__":
    nathan = Payslips("Nathan", "no", 1000)
    # nathan.pay()
    nathan.status()
    roger = Payslips("Roger", "no", 2000)
    roger.pay()
    roger.status()
