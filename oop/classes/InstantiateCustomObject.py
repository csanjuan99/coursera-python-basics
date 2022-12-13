class MyFirstClass:
    index = "Author-Book"
    print(f"Who wrote this?")

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(f"{philosopher} wrote {book}")


if __name__ == "__main__":
    my_object = MyFirstClass()
    my_object.hand_list("Aristotle", "The Nicomachean Ethics")
