class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))


student = Student("Dhanashri", [85, 90, 78])
student.display()