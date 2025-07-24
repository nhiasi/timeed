
from datetime import datetime

from numpy.ma.core import append


class Validation:
    def __init__(self, year, month, day, hour, minute, second):
        #TODO man könnte auch ne liste oder dict übergeben
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
        if self.false_time_list:
            return False
        else:
            return True


    def check_datetime(self):
        try:
            #testet ob es ein realistisches Datum ist
            datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)
            return True
        except TypeError:

            #findet den fehler
            if not (1 < self.month < 12):
                self.false_time_list.append(self.time_list.index(self.month))
            if not (1 < self.day < 34):
                self.false_time_list.append(self.time_list.index(self.day))
            if not (0 <= self.hour < 24):
                self.false_time_list.append(self.time_list.index(self.hour))
            if not (0 <= self.minute < 60):
                self.false_time_list.append(self.time_list.index(self.minute))
            if not (0 <= self.second < 60):
                self.false_time_list.append(self.time_list.index(self.second))
            return False


    def check_input_datetime(self):
        if not self.check_int():
            return self.false_time_list
        if not self.check_datetime():
            return self.false_time_list

        self.check_int()
        self.check_datetime()
        return True, self.false_time_list


    #TODO kann mit list comprehention sehr viel einfacher gemacht werden

if __name__ == '__main__':

    d = Validation(" d", 11, 24, 611, 30, 00)
    #d.check_int()
    #d.check_datetime()
    #print(d.time_list)
    #print(d.false_time_list)

    print(d.check_input_datetime())



