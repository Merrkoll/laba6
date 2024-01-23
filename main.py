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
        self.__specs = []
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
    return

def create_student():
    return


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
            pass
        elif choose == "2":
            pass
        elif choose == "3":
            pass
        elif choose == "4":
            pass
        elif choose == "5":
           pass
        elif choose == "6":
            pass
        elif choose == "7":
            pass
        else:
            pass

if __name__ == "__main__":
 menu()