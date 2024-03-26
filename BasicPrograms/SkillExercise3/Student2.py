class Student:
    def _init_(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Attributes and their values:")
        print(f"student_id: {self.student_id}")
        print(f"student_name: {self.student_name}")
        print()

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)
            print(f"{attribute_name} removed successfully.")
        else:
            print(f"{attribute_name} does not exist in the attributes.")


student1 = Student(student_id=1, student_name="John Doe")


student1.display_attributes()


student1.student_class = "Class A"


student1.display_attributes()

# Removing the 'student_name' attribute
student1.remove_attribute("student_name")

# Displaying attributes after removal
student1.display_attributes()