lecturer_list = []
students_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.course_list and grade_lecturer <= 10:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grade_lecturer]
        else:
            return 'Ошибка'

    def grade_average_hw(self):
        if not self.grades:
            return 0
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        return round(sum(grades_list) / len(grades_list), 1)

    def add_course(self, course_name):
        self.finished_courses.append(course_name)

    def __gt__(self, another):
        if self.grade_average_hw() == 0 or another.grade_average_hw() == 0:
            return 'Нельзя сравнивать'
        else:
            return self.grade_average_hw() < another.grade_average_hw()


    def all_grades_stud(self, course, students_list):
        all_grades_student = []
        for student in students_list:
            if not course in student.grades:
                print(f'Студент {student.name} не учится на курсе: {course}')
            elif not course in student.grades:
                print(f'У студента {student.name} нет оценок за курс: {course}')
            else:
                for grad in student.grades[course]:
                    all_grades_student.append(grad)
        if len(all_grades_student) == 0:
            return 'Ошибка, у студентов нет оценок!'
        else:
            return f'Средняя оценка всех студентов за лекции в рамках курса {course}: {round(sum(all_grades_student) / len(all_grades_student), 1)}'



    def __str__(self):
        average_grade = self.grade_average_hw()
        return f"Имяя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_grade:.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
        lecturer_list.append(self)

    def average_grade_lecture(self):
        if not self.grades_lecturer:
            return 0
        grades_list = []
        for grade in self.grades_lecturer.values():
            grades_list.extend(grade)
            return round(sum(grades_list) / len(grades_list), 1)


    def __gt__(self, another):
        if self.average_grade_lecture() == 0 or another.average_grade_lecture() == 0:
            return 'Нельзя сравнивать'
        else:
            return self.average_grade_lecture() > another.average_grade_lecture()

    def all_grades_lec(lecturer_list, course):
        all_grades_lecturer = []
        for lecturer in lecturer_list:
            if not course in lecturer.grades_lecturer:
                print(f'Преподаватель {lecturer.name} не ведет лекции по курсу: {course}')
            elif not course in lecturer.grades_lecturer:
                print(f'У преподавателя {lecturer.name} нет оценок за курс: {course}')
            else:
                for grad in lecturer.grades_lecturer[course]:
                    all_grades_lecturer.append(grad)
        if len(all_grades_lecturer) == 0:
            return 'Ошибка, у преподавателей нет оценок!'
        else:
            return f'Средняя оценка всех лекторов за лекции в рамках курса {course}: {round(sum(all_grades_lecturer) / len(all_grades_lecturer), 1)}'





    def __str__(self):
        average_grade = self.average_grade_lecture()
        return f"Имяя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.add_course('Python')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades['Python'] = [10, 8, 9, 9]
best_student.grades['Git'] = [7, 8, 9, 10]
best_student.grades['Введение в программирование'] = [7, 8, 9, 10]
best_student.grade_average_hw()

best_student2 = Student('Dan', 'Name', 'your_gender')
best_student2.add_course('Python')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']
best_student2.grades['Git'] = [6, 6, 3, 2]
best_student2.grades['Введение в программирование'] = [7, 8, 9, 10]


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Reviewer('Bob', 'Mat')
cool_mentor2.courses_attached += ['C++']

cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor2.rate_hw(best_student2, 'C++', 6)
cool_mentor2.rate_hw(best_student2, 'C++', 7)
cool_mentor2.rate_hw(best_student2, 'C++', 8)

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python', 'Git']
lecturer.grades_lecturer['Python'] = [10, 8, 9, 9]
lecturer.grades_lecturer['Git'] = [7, 8, 9, 10]

lecturer2 = Lecturer('Yin', 'Oliver')
lecturer2.courses_attached += ['Git']
lecturer2.grades_lecturer['Git'] = [5, 8, 9, 9]


print(best_student)
print("")
print(best_student2)
print("")
print(lecturer)
print("")
print(cool_mentor)
print("")
print(Student.__gt__(best_student2, best_student))
print("")
print(Lecturer.__gt__(lecturer, lecturer2))
print("")
print(Lecturer.all_grades_lec(lecturer_list, 'Git'))
print("")
print(Lecturer.all_grades_lec(lecturer_list, 'Python'))
print("")
print(Student.all_grades_stud(best_student, 'Python', students_list))
print("")
print(Student.all_grades_stud(best_student2, 'Git', students_list))