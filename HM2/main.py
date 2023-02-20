from Animal import *

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_voice(self):
        print("Meow")

    def get_information(self):
        print(f"Cat: \n\tname: {self.get_name()}\n\tage: {self.get_age()}\n"
              f"\tФакт о кошках: всего существует 33 основных кошачьих породы.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_voice(self):
        print("Woof")

    def get_information(self):
        print(f"Dog: \n\tname: {self.get_name()}\n\tage: {self.get_age()}\n"
              f"\tФакт о собаках: собачьи ошейники с шипами придумали древние греки — \n"
              f"\tтак они спасали своих питомцев от удушения волками")


class Duck(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_voice(self):
        print("Quack-quack")

    def get_information(self):
        print(f"Duck: \n\tname: {self.get_name()}\n\tage: {self.get_age()}\n"
              f"\tФакт об утках: утки умеют нырять на глубину более 6 метров для добычи пищи.")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_voice(self):
        print("Moo")

    def get_information(self):
        print(f"Cow: \n\tname: {self.get_name()}\n\tage: {self.get_age()}\n"
              f"\tФакт о коровах: люди одомашнили коров около 8 тысяч лет назад.")

cat = Cat(input("Имя: "), int(input("Возраст: ")))
print(cat.get_name())
cat.set_name(input("Смените имя: "))
cat.get_information()

dog = Dog(input("Имя: "), int(input("Возраст: ")))
print(dog.get_name())
dog.set_name(input("Смените имя: "))
dog.get_information()

duck = Duck(input("Имя: "), int(input("Возраст: ")))
print(duck.get_name())
duck.set_name(input("Смените имя: "))
duck.get_information()

cow = Cow(input("Имя: "), int(input("Возраст: ")))
print(cow.get_name())
cow.set_name(input("Смените корове имя: "))
cow.get_information()