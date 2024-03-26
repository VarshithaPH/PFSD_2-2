class Parent:
    def function1(self):
        print("This is function 1")


class Child(Parent):
    def function2(self, a):
        print("This is function 2")
        print(a)
    b = 20


y = Child()
y.function1()
y.function2(10)
print(y.b)
