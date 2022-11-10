#Определяем класс студенов

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#Студенты выставляют оценки лекторам

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Вывод информации о студентах

    def __str__(self):

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.avg_rat = sum(map(sum, self.grades.values())) / grades_count
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.avg_rat}\nКурсы в процессе обучения: {courses_in_progress_string}\nЗавершенные курсы: {finished_courses_string}'
        return some_student

#Сравнение оценок студентов

    def __lt__(self, other):
       if not isinstance(other, Student):
            print('Ошибка')
            return
       return self.avg_rat < other.avg_rat


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    #def __int__(self, name, surname):
        #super().__init__(self, name, surname)
    grades = {}

# Вывод информации о лекторах
    def __str__(self):

        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.avg_rat = sum(map(sum, self.grades.values())) / grades_count
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rat}'
        return some_lecturer

# Сравнение оценок лекторов

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.avg_rat < other.avg_rat

class Reviewer(Mentor):

#Проверяющие выстовляют оценки студентам

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
#Вывод информации о проверяющих

    def __str__(self):
        some_rewiewer = f'Имя: = {self.name}\nФамилия: = {self.surname}\n'
        return some_rewiewer


 #Студенты
best_student = Student('Ruoy', 'Eman', 'м')
best_student.courses_in_progress += ['Python', 'math', 'Java']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Peter', 'Parker', 'м')
some_student.courses_in_progress += ['Java', 'Python']
some_student.finished_courses += ['Введение в программирование']

#Лекторы
cool_lec = Lecturer('Some', 'Buddy')
cool_lec.courses_attached += ['Python', 'math', 'Java']


some_lecturer = Lecturer('Alex', 'Ivanov')
some_lecturer.courses_attached += ['Python', 'Введение в программирование']

#Проверяющие

cool_reviewer = Reviewer('Joy', 'Lil')
cool_reviewer.courses_attached += ['Python', 'Введение в программирование']
cool_reviewer.courses_attached += ['math']

some_reviewer = Reviewer('Lina', 'Smit')
some_reviewer.courses_attached += ['Введение в программирование']
some_reviewer.courses_attached += ['Java']



best_student.rate_lecturer(cool_lec, 'Python', 5)
best_student.rate_lecturer(some_lecturer , 'Введение в программирование', 10)
some_student.rate_lecturer(cool_lec, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Java', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 7)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Введение в программирование', 5)

some_reviewer.rate_hw(best_student, 'Java', 10)
some_reviewer.rate_hw(best_student, 'Введение в программирование', 5)


some_reviewer.rate_hw(some_student, 'Java', 8)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 7)
some_reviewer.rate_hw(some_student, 'Python', 9)



some_student.grades = {'Введение в программирование': [3, 10], 'Python': [4, 8]}
best_student.grades = {'Python': [6, 10]}




print(best_student.grades)
print(some_student.grades)
print(cool_lec.grades)
print(some_lecturer.grades)

print(some_student)
print(best_student)
print(some_reviewer)
print(cool_reviewer)
print(some_lecturer)
print(cool_lec)

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{some_student.name} {some_student.surname} < {best_student.name} {best_student.surname} = {best_student > some_student}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{some_lecturer.name} {some_lecturer.surname} < {cool_lec.name} {cool_lec.surname} = {some_lecturer > cool_lec}')
print()


  # для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);

students_list = [best_student, some_student]

def student_rating(students_list, course_name):

    sum_all = 0
    count_all = 0
    for st in students_list:
       if course_name in st.grades.keys():

            sum_all += st.avg_rat
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

#для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).


lecturers_list = [some_lecturer, cool_lec
                  ]
def lecturer_rating(lecturers_list, course_name):

    sum_all = 0
    count_all = 0
    for lec in lecturers_list:
       if course_name in lec.grades.keys():

            sum_all += lec.avg_rat
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all



print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(students_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturers_list, 'Python')}")
print()

