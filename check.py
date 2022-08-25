# 1.    Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
# Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# Представитель каждого класса может умереть, если достигнет определенного возраста
# или для него не будет еды. Напишите виртуальные методы поедания и определения
# состояния живого существа (живой или нет, в зависимости от достижения
# предельного возраста и наличия еды (входной параметр)).
class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)


class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr

    def grown(self):
        self.count *= self.koef_repr

    def info(self):
        print("The amount of plants:", self.count)

    def rabbits_food(self,count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self,count_plants):
        self.count += count_plants

class Rabbits(Alive):
    def __init__(self, koef_repr,koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("The amount of rabbits:", self.count)

    def take_away(self,count_rabbits):
        self.count -= count_rabbits

    def be_eatten(self,number):
        self.count -= number


class Fox(Alive):
    def __init__(self, koef_repr,koef_death, count, dinner):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
        self.dinner = dinner

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("The amount of foxes:", self.count)

    def take_away(self,count_rabbits):
        self.count -= count_rabbits


plants = Plants(10, 200)
rabbits = Rabbits(5,0.2,100)
foxes = Fox(2,0.1,50,2)

year = 0
print("The beginning.")
plants.info()
rabbits.info()
foxes.info()

while year < 10:
    year += 1

    plants.grown()
    plants.rabbits_food(rabbits.count)

    rabbits.death()
    rabbits.reproduction()

    foxes.death()
    foxes.reproduction()
    rabbits.take_away(foxes.count*foxes.dinner)


    if plants.count // 10  <= rabbits.count:
        print("System is not in balace!!! Warning!!!!!!!")
        print("THere is a lack of plants. Babbits are complaining!")
        rabbits.info()
        plants.info()
        choise = int(input("enter 1 - add plants 2 - take away rabbits:"))
        if choise == 1:
            count = int(input("enter count plants:"))
            plants.add_plants(count)
        elif choise == 2:
            count = int(input("enter count rabbits:"))
            rabbits.take_away(count)

    if rabbits.count // 2  <= foxes.count:
        print("System is not in balace!!! Warning!!!!!!!")
        print("THere is a lack of rabbits. Foxes are complaining!")
        rabbits.info()
        foxes.info()
        choise = int(input("enter 1 - add rabbits 2 - take away foxes:"))
        if choise == 1:
            count = int(input("enter count rabbits:"))
            rabbits.count +=count
        elif choise == 2:
            count = int(input("enter count foxes:"))
            foxes.count-=count

    print("Current year is ", year)

    plants.info()
    rabbits.info()
    foxes.info()




