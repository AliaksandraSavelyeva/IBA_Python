# Вариант 6
# Создать класс Abiturient: id, Фамилия, Имя, Отчество,
# Адрес, Телефон, Оценки.
# Создать список объектов. Вывести:
# a)	список абитуриентов, у которых сумма баллов выше заданной;

class Abiturient:
    #конструктор
    def __init__(self, stud_id, last_name, first_name, patronim, address, phone, grades):
        self.id = stud_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronim = patronim
        self.address = address
        self.phone = phone
        self.grades = grades

    def get_stud_id(self):
        return self.id

    def set_stud_id(self, stud_id):
        self.id = stud_id

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_patronim(self):
        return self.patronim

    def set_patronim(self, patronim):
        self.patronim = patronim

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_grades(self):
        return self.grades

    def set_grades(self, grades):
        self.grades = grades


student_1 = Abiturient('1', 'Иванов', 'Иван', 'Иванович', 'ул. Первая, 1-23', '80172569845', '8.7')
student_2 = Abiturient('2', 'Петров', 'Пётр', 'Петрович', 'ул. Вторая, 2-33', '80172125789', '6.1')
student_3 = Abiturient('3', 'Александров', 'Александр', 'Александрович', 'ул. Третья, 3-41', '80172332560', '7.5')
student_4 = Abiturient('4', 'Алексеев', 'Алексей', 'Алексеевич', 'ул. Четвёртая, 6-20', '80172777898', '4.4')

stud_list = [student_1, student_2, student_3, student_4]

gradeLevel = input('Введите минимальный средний балл: \n')
print("Студенты со средним баллом выше заданного:")
for student in stud_list:
    if student.get_grades() >= gradeLevel:
        print(
            student.get_stud_id() + " - Фамилия: " + student.get_last_name() + ", имя: " + student.get_first_name()
            + ", отчество " + student.get_patronim() + ", адрес: " + student.get_address() + ", телефон: "
            + student.get_phone() + ", средний балл: " + student.get_grades() + ".")
