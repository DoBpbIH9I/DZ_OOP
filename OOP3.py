class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    def __init__(self, name, surname, gender):
        self.surname = surname
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __lt__(self, other):
        return self.avg_course_grade() < other.avg_course_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.avg_course_grade()}\n'
                f'Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {','.join(self.finished_courses)}')

    def avg_course_grade(self):
        self.k = []
        for j in self.grades.values():
            self.k.extend(j)
            return sum(self.k)/len(self.k)

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_course_grade(self):
        self.k = []
        for j in self.grades.values():
            self.k.extend(j)
            return sum(self.k)/len(self.k)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.avg_course_grade()}')

    def __lt__(self, other):
        return self.avg_course_grade() < other.avg_course_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

rew = Reviewer('Some','Buddy')
print(rew)

jam = Lecturer('GG', 'WP')
jam.grades = {'Python': [10, 9, 9, 9], 'js': [10,9]}
print(jam)

student = Student('Олег','Брауни','мужик')
student.finished_courses += ['Как не поехать кукухой в изучении программирования','Спасити']
student.courses_in_progress += ['Тихо шифером шурша, едет крыша неспеша','Я не умру в ООП']
student.grades = {'Python': [10, 9, 9, 10], 'js': [10,9]}
print(student)
student1 = Student('Костя','Вафля','мальчик')
student1.finished_courses += ['Я не поехал кукухой в изучении программирования','Спасли']
student1.courses_in_progress += ['Крыша уже уехала','Я умер в ООП']
student1.grades = {'Python': [10, 9, 9, 9], 'js': [10,9]}

