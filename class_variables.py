class student:

    start_year = 2026
    num_stu = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_stu += 1

    def study(self):
        print(f"{self.name} is studying")

    def play(self):
        print(f"{self.name} is playing")


class college:

    num_college = 0
    def __init__(self, cname, cplace, ctype,cyear):
        self.cname = cname
        self.cplace = cplace
        self.ctype = ctype
        self.cyear = cyear
        self.num_college += 1
        

class batch1(student, college):

    num_stu_batch1 = 0

    def __init__(self, student_obj, college_obj):
        self.student = student_obj
        self.college = college_obj
        self.timing = "Morning"
        self.have_books = True

        batch1.num_stu_batch1 += 1

class batch2(student, college):

    num_stu_batch2 = 0
     
    def __init__(self, student_obj, college_obj):
        self.student = student_obj
        self.college = college_obj
        self.timing = "Evening"
        self.have_books = False
        batch2.num_stu_batch2 += 1


college1 = college("NIT", "Punjab", "Govt." ,1990)
college2 = college("LPU", "Punjab", "Private", 1995)

student1 = student("Rahul", 19)
student2 = student("Ashok", 22)

s1 = batch1(student1, college1)
s2 = batch2(student2, college2)





    

    