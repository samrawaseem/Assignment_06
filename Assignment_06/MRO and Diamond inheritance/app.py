class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Create an object of D
d = D()

# Call show(), observe which method gets called based on MRO
d.show()

print("MRO of class D:", [cls.__name__ for cls in D.__mro__])