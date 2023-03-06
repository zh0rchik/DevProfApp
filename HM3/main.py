class Mydatetime():
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, timestep):
        self.year = 1970

        self.second = timestep % 60
        timestep -= self.second

        self.minute = timestep % 3600 // 60
        timestep -= self.minute

        self.hour = timestep % 86400 // 3600
        timestep -= self.hour

        self.day = timestep // 86400 + 1

        self.year, self.day = self.get_year(self.day, self.year)
        self.month, self.day = self.get_month(self.day, self.year, self.days_in_months)

    def __str__(self):
        return(f'{self.year}-{self.month}-{self.day} '
               f'{self.hour}:{self.minute}:{self.second}')

    @staticmethod
    def get_year(days, year):
        year = 1970
        while days > 365:
            if (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
                days -= 365
            else:
                days -= 366
            year += 1
        return year, days

    @staticmethod
    def get_month(day, year, days_in_month):
        month = 1
        for i in days_in_month:
            if day > i:
                if i < 30:
                    if not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                        i += 1
                day -= i
                month += 1
            else:
                break

        return month, day


if __name__ == "__main__":
    TASK_1 = True   # Решить задачу №1
    TASK_2 = False   # Решить задачу №2

    if TASK_1:
        mdt = Mydatetime(int(input()))
        print(mdt.__str__())
    if TASK_2:
        arr = list(map(int, input().split(' ')))
        min_value = arr[0]
        for i in range(1, len(arr)):
            if min_value > arr[i]:
                min_value = arr[i]

        print(min_value)