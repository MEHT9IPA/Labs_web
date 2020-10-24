# используется для сортировки
from operator import itemgetter


class Student:
    """Школьник"""

    def __init__(self, id, name, rating, class_id):
        self.id = id
        self.name = name
        self.rating = rating
        self.class_id = class_id

class Class:
    """Класс"""

    def __init__(self, id, number):
        self.id = id
        self.number = number


class StudClass:
    """
    'StudClass' для реализации
    связи многие-ко-многим
    """

    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id


# Школяры
students = [
    Student(1, 'Якубов', 14.88, 2),
    Student(2, 'Власов', 2, 1),
    Student(3, 'Аникин', 13.37, 2),
    Student(4, 'Троцкий', 3, 1),
    Student(5, 'Ленин', 19.17, 3),
    Student(6, 'Сталин', 19.45, 3),
    Student(7, 'Абдуллаев', 42.0, 2),
    Student(8, 'Горбачёв', 1.991, 1)
]

# Классы
classes = [
    Class(1, 5),
    Class(2,228),
    Class(3,420)
]

studsclasses = [
    StudClass(1,2),
    StudClass(1,4),
    StudClass(1,8),
    StudClass(2,1),
    StudClass(2,3),
    StudClass(2,7),
    StudClass(3,5),
    StudClass(3,6)
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(s.name, s.rating, c.number)
                   for s in students
                   for c in classes
                   if s.class_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.number, sc.class_id, sc.student_id)
                         for c in classes
                         for sc in studsclasses
                         if c.id == sc.class_id]

    many_to_many = [(s.name, student_name)
                    for student_name, student_id, class_id in many_to_many_temp
                    for s in students if s.id == class_id]

    print('Задание B1')
    res_11 = list(filter(lambda x: x[0].startswith('А'), one_to_many))
    print(res_11)
    
    print('\nЗадание B2')
    res_12_unsorted = []
    for c in classes:
        meow = list(filter(lambda i: i[2] == c.number, one_to_many))
        if len(meow) > 0:
            count = [rating for _, rating, _ in meow]
            count_min = min(count)
            res_12_unsorted.append((c.number, count_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)
    

if __name__ == '__main__':
    main()






