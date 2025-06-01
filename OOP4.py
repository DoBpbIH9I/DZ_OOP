# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).

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
        self.average_rating = float()
        self.grades = {}




    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __lt__(self, other):
        return self.avg_course_grade() < other.avg_course_grade()

    def avg_course_grade(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return self.average_rating

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.avg_course_grade()}\n'
                f'Курсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}')



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
        self.average_rating = float()
        self.l = float()
        self.grades = {}

    def avg_course_grade(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return self.average_rating

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.avg_course_grade()}')

    def __lt__(self, other):
        return self.avg_course_grade() < other.avg_course_grade()



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n' 
                f'Фамилия: {self.surname}')


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Жорик','Ващпе','Мужикотавр')
student2 = Student('Фрея','Крис','Феечка_Винкс')

student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [10, 9, 9, 8], 'js': [10,9]}
student2.grades = {'Python': [10, 4, 9, 2], 'js': [8,1]}
lecturer1 = Lecturer('Гендальф','Умный')
lecturer2 = Lecturer('Дамблдор','Сверхумный')
reviewer1 = Reviewer('Око','Корень')
reviewer2 = Reviewer('Глаз','Третий')
lecturer1.courses_attached +=['Python']
lecturer2.courses_attached +=['Python']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']
student1.rate_lector(lecturer1,'Python',10)
student2.rate_lector(lecturer1,'Python',7)
student1.rate_lector(lecturer2,'Python',8)
student2.rate_lector(lecturer2,'Python',9)
reviewer1.rate_hw(student1,'Python', 9)
reviewer2.rate_hw(student1,'Python', 10)
reviewer1.rate_hw(student2,'Python', 9)
reviewer2.rate_hw(student2,'Python', 9)


print(f'{lecturer1}\n\n{lecturer2}\n')
print(f'Перечень студентов:\n{student1}\n\n{student2}')

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 > student2}')
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer1 > lecturer2}')
students = [student1, student2]

lecturers = [lecturer1, lecturer2]


def student_rating(students, course_name):
    sum_all = 0
    count_all = 0
    for stud in students:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturers, course_name):
    sum_all = 0
    count_all = 0
    for drop in lecturers:
        if drop.courses_attached == [course_name]:
            sum_all += drop.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(students, 'Python')}")
print()
# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturers, 'Python')}")
