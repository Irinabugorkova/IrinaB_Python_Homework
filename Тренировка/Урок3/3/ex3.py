from student import Student
from course_group import CourseGroup

student_main = Student("Иван", "Петров", 20, 3)
classmate1 = Student("Алексей", "Сидоров", 21, 3)
classmate2 = Student("Мария", "Иванова", 19, 3)


group = CourseGroup(student_main, [classmate1, classmate2])

print(group)
