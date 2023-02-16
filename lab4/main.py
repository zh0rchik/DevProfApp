import csv
import datetime

#https://proproprogs.ru/python_oop/magicheskie-metody-getitem-setitem-delitem

class Record():
    idx = datetime.datetime.now().strftime("%d%H%M%S")
    def __init__(self, idx):                                     # конструктор
        self.idx = idx     # генерация id

    def get_id(self):
        return self.idx

class RecordHospital(Record):
    name_patient = ""
    name_doctor = ""
    reason = ""
    time = "00:00"
    def __init__(self, idx:int, name_patient:str, name_doctor:str, reason:str, time:int):
        self.idx = super().__init__(idx)
        self.name_patient = name_patient
        self.name_doctor = name_doctor
        self.reason = reason
        self.time = time

    def __repr__(self):                           # Выводит параметры объекта, его текстовое представление
        return(f"class: RecordHospital\n\tidx={self.idx}\n\tname_patient={self.name_patient}\n\t"
               f"name_doctor={self.name_doctor}\n\treason={self.reason}\n\ttime={self.time}")

    def __setattr__(self, key, value):           # устанавливает значение атрибута указанного объекта по его имени
        self.__dict__[key] = value

    @staticmethod                                # Статический метод - метод, который не использует self
    def get_format(seconds):                     # Статический метод для получения фомата минута:секунда из секунд
        minutes = str(seconds // 60)
        seconds = str(seconds % 60)

        if int(minutes) < 10:
            minutes = '0' + minutes
        if int(seconds) < 10:
            seconds = '0' + seconds

        return f"{minutes}:{seconds}"

class Data():
        cursor = 0
        file_path = ""
        data = []

        def __init__(self, path: str):
            self.file_path = path
            self.data = self.parse(self.file_path)

        def __repr__(self):
            return f"Data({[rm.__repr__() for rm in self.data]})"

        def add_new_record(self, name_patient: str, name_doctor: str, reason: str, time: int):
            new_record = RecordHospital(0, name_patient, name_doctor, reason, time)
            with open(self.file_path, "a") as tabel_file:
                writer = csv.DictWriter(tabel_file, fieldnames=['id', 'name_p', 'name_d', 'reason', 'time'])
                writer.writerow()

        def my_generator(self):
            self.cursor = 0

            while self.cursor < len(self.data):
                yield self.data[self.cursor]
                self.cursor += 1

        @staticmethod
        def parse(path: str):
            mydicts = []
            with open(path, "r") as tabel_file:
                reader = csv.DictReader(tabel_file, fieldnames=['id', 'name_p', 'name_d', 'reason', 'time'])
                for record in reader:
                    (idx, name_p, name_d, reason, time) = record
                    mydicts.append(RecordHospital(idx, name_p, name_d, reason, time))

            return mydicts

if __name__ == "__main__":
    d = Data("C:\\Users\\georg\\OneDrive\\Рабочий стол\\lab3\\lab3.csv")
    print(d.__str__())
    d.add_new_record(input("ФИО пациента: "), input("ФИО врача: "), input("Причина обращения: "), int(input("Время приёма: ")))
    print(d.__str__())