hello = "World"


def reverse_string(string):
    return string[::-1]

def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string_recursive(string[1:]) + string[0]


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string_recursive("hello"))
