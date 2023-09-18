class Student:
    def __init__(self, name, numb_group, estimates):
        self.name = name
        self.numb_group = numb_group
        self.estimates = sum(estimates) / len(estimates)

    def __str__(self):
        return str(("Студент: {} Группа: {} Средний Балл: {}".format(
            self.name, self.numb_group, self.estimates
        )
        ))


def addStudent():
    name = input('Введите ФИ: ')
    numb_group = input('Введите номер группы: ')
    print('Введите последние 5 оценок')
    estimates = []
    for i in range(5):
        score = int(input())
        estimates.append(score)

    return name, numb_group, estimates


students = []

for _ in range(10):
    student = Student(*addStudent())
    students.append(student)
students.sort(key=lambda x: x.estimates, reverse=True)
for i_stud in students:
    print(i_stud)

# зачтено
