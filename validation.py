
from datetime import datetime

class Validation:
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

        self.time_list = [year, month, day, hour, minute, second]
        self.false_time_list = []

    def check_int(self):
        for valu in self.time_list:
            if not isinstance(valu, int):
                self.false_time_list.append(self.time_list.index(valu))
        if  self.false_time_list:
            return True, self.false_time_list
        else:
            return False

    def check_datetime(self):
        datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)

    #TODO kann mit list comprehention sehr viel einfacher gemacht werden

if __name__ == '__main__':

    d = Validation(2025, 7, 21, 11, 30, 00)
    d.check_int()
    d.check_datetime()
    print(d.time_list)
    print(d.false_time_list)

