class MyClass:
    class_variable = "I am a class variable"

    def _init_(self, name):
        self.name = name

    def display_namespace(self):
        print(f"Namespace of {self.name}:", vars(self))



obj = MyClass("MyObject")


obj.display_namespace()

print("Class Variable:", MyClass.class_variable)
