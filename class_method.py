#class method = allow operations related to the class itself


class student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total students is {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else :
            return f"total gpa is {cls.total_gpa/cls.count:.2f}"

student1 = student("halku", 8)
student2 = student("thor", 7)

print(student.get_count())
print(student.get_avg_gpa())