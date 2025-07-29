from student import Student

class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates_list = ", ".join(str(s) for s in self.classmates)
        return f"{self.student}, учится на курсе {self.student.course} вместе с: {classmates_list}"