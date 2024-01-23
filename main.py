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
    def __init__(self):
        return

    def __str__(self):
        return


def create_kurs():
    return


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