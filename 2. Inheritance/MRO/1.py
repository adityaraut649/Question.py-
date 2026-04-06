class A:
    pass

class B(A):
    def show(self): 
        print("B")

class C(A):
    def show(self): 
        print("C")

class D(B, C):
    pass

d = D()
print(D.__mro__)
print(d.show())

# D -> B -> C -> A