class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
    
    def avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else 'Нет'}\n")
    
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_grade():.1f}\n")
    
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

def avg_hw_grade(students, course_name):
    total = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return total / count if count > 0 else 0

def avg_lecture_grade(lecturers, course_name):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return total / count if count > 0 else 0

student1 = Student('Ольга', 'Алёхина', 'Ж')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 9, 10], 'Git': [8, 9]}

student2 = Student('Иван', 'Петров', 'М')
student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Основы HTML']
student2.grades = {'Python': [8, 7, 9], 'Java': [10, 9]}

lecturer1 = Lecturer('Анна', 'Смирнова')
lecturer1.courses_attached = ['Python', 'Java']

lecturer2 = Lecturer('Дмитрий', 'Кузнецов')
lecturer2.courses_attached = ['Python', 'Git']

reviewer1 = Reviewer('Мария', 'Иванова')
reviewer1.courses_attached = ['Python', 'Git']

reviewer2 = Reviewer('Алексей', 'Соколов')
reviewer2.courses_attached = ['Python', 'Java']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Java', 9)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Java', 9)

student1.rate_lecture(lecturer2, 'Python', 7)
student1.rate_lecture(lecturer2, 'Git', 8)
student2.rate_lecture(lecturer2, 'Python', 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(f"Студент1 лучше Студента2? {student1 > student2}")
print(f"Лектор1 лучше Лектора2? {lecturer1 > lecturer2}")

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка за ДЗ по курсу Python: {avg_hw_grade(students_list, 'Python'):.1f}")
print(f"Средняя оценка за ДЗ по курсу Git: {avg_hw_grade(students_list, 'Git'):.1f}")
print(f"Средняя оценка за ДЗ по курсу Java: {avg_hw_grade(students_list, 'Java'):.1f}")

print(f"Средняя оценка за лекции по курсу Python: {avg_lecture_grade(lecturers_list, 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу Git: {avg_lecture_grade(lecturers_list, 'Git'):.1f}")
print(f"Средняя оценка за лекции по курсу Java: {avg_lecture_grade(lecturers_list, 'Java'):.1f}")