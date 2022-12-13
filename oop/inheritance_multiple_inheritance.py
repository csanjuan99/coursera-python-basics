class A:
    pass


# class B inherits from class A
class B(A):
    pass


# Multiple inheritance
class C:
    a = 1


class D:
    b = 2


class E(C, D):
    pass


# Create an instance of class E
e = E()
print(e.a, e.b)


# Multi-level inheritance

class F:
    a = 1


class G(F):
    a = 2


class H(G):
    pass


h = H()
print(h.a)  # The output is 2 because H derives from the immediate super class of H, which is G;
