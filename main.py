kurs_obj = []
student_obj = []
specs = []


class Student:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"

class Spec:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"



class Kurs:
    def __init__(self, namekurs):
        self.__namekurs = namekurs
        self.__specs= []
        self.__students = []
    @property
    def namekurs(self):
        return self.__namekurs

    @property
    def specs(self):
        return self.__specs

    @property
    def students(self):
        return self.__students
    def make_specs(self, specs):
        self.specs.append(specs)

    def make_student(self, student):
        self.students.append(student)

    def __str__(self):
        spec_str = f"Специальность: {self.specs}" if self.specs else "Специальность не объявлена"
        students_str = "\n".join(str(student) for student in self.students)
        return f"Курс: {self.namekurs}\n{spec_str}\nСтуденты:\n{students_str}"


def create_kurs():
    namekurs = input("Введите номер курса: ")
    return Kurs(namekurs)


def create_spec():
    name = input("Введите название специальности: ")
    return Spec(name)


def create_student():
    while True:
        surname = input("Введите фамилию студента: ")
        if surname.isalpha():
            break
        else:
            print("Ошибка. Фамилия должна состоять из букв. Введите корректную фамилию. ")

    while True:
        name = input("Введите имя cтудента: ")
        if name.isalpha():
            break
        else:
            print("Ошибка. Имя должно состоять из букв. Введите корректное имя. ")

    while True:
        age = input("Введите возраст студента: ")
        try:
            age = int(age)
            break
        except ValueError:
            print("Ошибка: Возраст должен быть числом. Попробуйте снова.")
    return Student(name, surname, age)


def menu():
    kurs_obj = None
    while True:
        print("Главное меню:")
        print("1. Создать курс.")
        print("2. Создать специальность(количество - неограничено).")
        print("3. Создать студента.(количество - неограничено)")
        print("4. Вывести информацию о студенте.")
        print("5. Вывести информацию о специальности.")
        print("6. Вывести информацию о курсе.")
        print("7. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            kurs_obj = create_kurs()
            print("Курс создан.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "2":
            if kurs_obj != None:
                spec_obj = create_spec()
                kurs_obj.make_specs(spec_obj)
                print("Специальность создана.")
            else:
                print("Сначала создайте курс.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "3":
            if kurs_obj != None:
                student_obj = create_student()
                kurs_obj.make_student(student_obj)
                print("Студент создан.")
            else:
                print("Сначала создайте курс.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "4":
            if kurs_obj and kurs_obj.students:
                for i, student in enumerate(kurs_obj.students, start=1):
                    print(f"{i}. {student}")
            else:
                print("Нет студентов или курс не создан.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "5":
            if kurs_obj and kurs_obj.specs:
                for i, spec in enumerate(kurs_obj.specs, start=1):
                    print(f"{i}. {spec}")
            else:
                print("Нет специальностей или курс не создан.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "6":
            if kurs_obj:
                print(kurs_obj)
            else:
                print("Курс не создан.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choose == "7":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
 menu()