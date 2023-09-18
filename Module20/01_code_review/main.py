students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def instersting(student_list):
    interest = []
    summ = 0
    for i_key, i_value in student_list.items():
        interest += i_value['interests']
        summ += len(i_value['surname'])
    return set(interest), summ


user_list = []
for i_index, i_age in students.items():
    user_id = i_index, i_age['age']
    user_list.append(user_id)
print('Список пар "ID студента — возраст":', user_list)

intesting_list, surname_len = instersting(students)
print('Полный список интересов всех студентов:', intesting_list)
print('Общая длина всех фамилий студентов:', surname_len)

# зачтено
