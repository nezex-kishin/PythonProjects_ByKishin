class Building:
    year = None
    city = None
    def __init__(self, year, city):
        self.year = year
        self.city = city
    def get_info(self):
        print(f'Год:{self.year}\nГород:{self.city}')

class School(Building):
    pupils = None
    def __init__(self,pupils,year,city):
        super(School, self).__init__(year,city)
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print('Кол-во учеников:',self.pupils)

class House(Building):
    pass
class Shop(Building):
    pass


school = School(300,2014,'Moscow')
school.get_info()

