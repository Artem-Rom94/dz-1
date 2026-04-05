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
                f"Завершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else 'Нет'}")
    
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
                f"Средняя оценка за лекции: {self.avg_grade():.1f}")
    
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Проверка
reviewer = Reviewer('Some', 'Buddy')
print(reviewer)
print()

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached = ['Python']
student = Student('Ольга', 'Алёхина', 'Ж')
student.courses_in_progress = ['Python']
student.rate_lecture(lecturer, 'Python', 9)
student.rate_lecture(lecturer, 'Python', 10)
print(lecturer)
print()

student1 = Student('Ruoy', 'Eman', 'M')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 9, 10], 'Git': [8, 9]}
print(student1)