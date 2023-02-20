from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age: int):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_voice(self):
        pass

    @abstractmethod
    def get_information(self):
        pass