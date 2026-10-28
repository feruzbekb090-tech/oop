# class: Student
# attributes: first_name, last_name, age
# methods: show_info: "men oquvchiman"


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_info(self):
        print("Men oquvchiman")


student1 = Student("Ali", "Valiyev", 19)
student1.show_info()
