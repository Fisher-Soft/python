# # 1.    Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
# # Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# # Представитель каждого класса может умереть, если достигнет определенного возраста
# # или для него не будет еды. Напишите виртуальные методы поедания и определения
# # состояния живого существа (живой или нет, в зависимости от достижения
# # предельного возраста и наличия еды (входной параметр)).
# import random
#
#
# class Alive:
#     def __init__(self, count):
#         self.count = count
#
#     def info(self):
#         print("count:", self.count)
#
#
# class Plants(Alive):
#     def __init__(self, koef_repr, count):
#         super().__init__(count)
#         self.koef_repr = koef_repr
#
#     def grown(self):
#         self.count *= self.koef_repr
#
#     def info(self):
#         print("The amount of plants:", self.count)
#
#     def rabbits_food(self,count_rabbits):
#         self.count -= count_rabbits * 10
#
#     def add_plants(self,count_plants):
#         self.count += count_plants
#
# class Rabbits(Alive):
#     def __init__(self, koef_repr,koef_death, count):
#         super().__init__(count)
#         self.koef_repr = koef_repr
#         self.koef_death = koef_death
#
#     def reproduction(self):
#         self.count *= self.koef_repr
#
#     def death(self):
#         self.count -= int(self.count * self.koef_death)
#
#     def info(self):
#         print("The amount of rabbits:", self.count)
#
#     def take_away(self,count_rabbits):
#         self.count -= count_rabbits
#
#     def be_eatten(self,number):
#         self.count -= number
#
#     def shooted(self,n):
#         self.count -=n
#
#
# class Fox(Alive):
#     def __init__(self, koef_repr,koef_death, count, dinner):
#         super().__init__(count)
#         self.koef_repr = koef_repr
#         self.koef_death = koef_death
#         self.dinner = dinner
#
#     def reproduction(self):
#         self.count *= self.koef_repr
#
#     def death(self):
#         self.count -= int(self.count * self.koef_death)
#
#     def info(self):
#         print("The amount of foxes:", self.count)
#
#     def take_away(self,count_rabbits):
#         self.count -= count_rabbits
#
#     def shooted(self,n):
#         self.count -=n
#
#
# plants = Plants(10, 200)
# rabbits = Rabbits(5,0.2,100)
# foxes = Fox(2,0.1,50,2)
#
# year = 0
# print("The beginning.")
# plants.info()
# rabbits.info()
# foxes.info()
#
# while year < 10:
#     year += 1
#
#     plants.grown()
#     plants.rabbits_food(rabbits.count)
#
#     rabbits.death()
#     rabbits.reproduction()
#
#     foxes.death()
#     foxes.reproduction()
#     rabbits.take_away(foxes.count*foxes.dinner)
#
#     a = random.randint(0,50)
#     rabbits.shooted(a)
#
#     b = random.randint(0,50)
#     foxes.shooted(b)
#
#     print(a,' rabbits were shooted this year.')
#     print(b,' foxes were shooted this year.')
#
#     if plants.count // 10  <= rabbits.count:
#         print("System is not in balace!!! Warning!!!!!!!")
#         print("THere is a lack of plants. Babbits are complaining!")
#         rabbits.info()
#         plants.info()
#         choise = int(input("enter 1 - add plants 2 - take away rabbits:"))
#         if choise == 1:
#             count = int(input("enter count plants:"))
#             plants.add_plants(count)
#         elif choise == 2:
#             count = int(input("enter count rabbits:"))
#             rabbits.take_away(count)
#
#     if rabbits.count // 2  <= foxes.count:
#         print("System is not in balace!!! Warning!!!!!!!")
#         print("THere is a lack of rabbits. Foxes are complaining!")
#         rabbits.info()
#         foxes.info()
#         choise = int(input("enter 1 - add rabbits 2 - take away foxes:"))
#         if choise == 1:
#             count = int(input("enter count rabbits:"))
#             rabbits.count +=count
#         elif choise == 2:
#             count = int(input("enter count foxes:"))
#             foxes.count-=count
#
#     print("Current year is ", year)
#
#     plants.info()
#     rabbits.info()
#     foxes.info()

# task 23-1
# class worker:
#     def __init__(self,FIO,level,salary,position):
#         self.FIO = FIO
#         self.level = level
#         self.salary = salary
# class stzher(worker):
#     def __init__(self,FIO,level,salary,srok,position):
#         worker.__init__(self,FIO,level,salary,position)
#         self.srok = srok
#         self.position = position
#
# class jober(worker):
#     pass
#
# class Chief(worker):
#     pass
#
# class director(worker):
#     pass
#
# x1 = worker('Ivanoff A.V.',1,5000,'Кладовщик')
# x2 = stzher('Petroff V.A.',1,600.5,1,'Секретарь')
# x3 = jober('Sidorov K.S.',2,1200,'Мастер')
# xx = director('Sokoloff B.B.',1,6000,'Директор')
# print('Уровень доступа',x1.FIO,x1.level)
# print('Зарплата',x2.FIO,x2.salary,' его должность',x2.position)

# # task 23-2
# Sities=['Minsk','Brest','Gomel','Moscow','Piter']
# distance = ((0,350,310,730,850),(350,0,560,1234,1456),(310,560,0,833,1234),(730,1456,833,0,700),(850,1456,1234,700,0))
# time1 = ((0,55,47,80,90),(55,0,67,78,103),(47,67,0,99,103),(80,103,90,0,75),(90,123,103,75))
# time2 = ((0,220,190,320,360), (220,0,268,312,412), (88,268,0,400,412), (320,412,360,0,301), (360,492,412,301))
# time3 = ((0,110,96,160,180),(110,0,134,156,206),(44,134,0,200,206),(160,206,180,0,150),(180,246,206,150))
# class GP:
#     def __init__(self,from1,to2):
#         self.from1 = from1
#         self.to2 = to2
#
#     def get_d(self):
#         return distance[Sities.index(self.from1)][Sities.index(self.to2)]
#
# class Jet(GP):
#     def __init__(self,from1,to2,dol_per_km):
#         GP.__init__(self,from1,to2)
#         self.dol_per_km = dol_per_km
#
#     def get_t(self):
#         return time1[Sities.index(self.from1)][Sities.index(self.to2)]
#
# class train(GP):
#     def __init__(self,from1,to2,dol_per_km):
#         GP.__init__(self,from1,to2)
#         self.dol_per_km = dol_per_km
#
#     def get_t(self):
#         return time2[Sities.index(self.from1)][Sities.index(self.to2)]
#
# class cars(GP):
#     def __init__(self,from1,to2,dol_per_km):
#         GP.__init__(self,from1,to2)
#         self.dol_per_km = dol_per_km
#
#     def get_t(self):
#         return time3[Sities.index(self.from1)][Sities.index(self.to2)]
#
# xx1 = input('Введите начальный пункт:')
# xx2 = input('Введите конечный пункт:')
# gp1 = GP(xx1,xx2)
# j1 = Jet(xx1,xx2,0.17)
# t1 = train(xx1,xx2,0.07)
# a1 = cars(xx1,xx2,0.09)
# print(f'Расстояние между пунктами {gp1.get_d()} km.')
# print(f'Время полёта {j1.get_t()} min.')
# print(f'Стоимость полёта {j1.get_d()*j1.dol_per_km} долларов.')
#
# print(f'Время поездом {t1.get_t()} min.')
# print(f'Стоимость поездом {t1.get_d()*t1.dol_per_km} долларов.')
#
# print(f'Время на авто {a1.get_t()} min.')
# print(f'Стоимость на авто {a1.get_d()*a1.dol_per_km} долларов.')

# import random
# import sqlite3
# conn = sqlite3.connect("task1.db")
# conn.commit()
# cursor = conn.cursor()
#
# cursor.execute("""
#    CREATE TABLE IF NOT EXISTS tbl(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    int1 INTEGER,
#    int2 INTEGER)
# """)
# conn.commit()
# kz = random.randint(3,20)
# for i in range(kz):
#     a = random.randint(0,9)
#     b = random.randint(0,9)
#     cursor.execute("""INSERT INTO tbl VALUES(NULL,?,?)""", (a,b))
#     conn.commit()
#
# cursor.execute("""SELECT * FROM tbl""")
# data = cursor.fetchall()
# s = 0
# n = 0
# for i in data:
#     s = s + i[1] + i[2]
#     n = n + 2
#
# if int(s/n)>int(n/2):
#     print('deleting')
#     cursor.execute("""DELETE FROM tbl WHERE id = 4""")
#     conn.commit()
#
# cursor.execute("""SELECT * FROM tbl""")
# data = cursor.fetchall()
# for i in data:
#     print(*i)
#
# import sqlite3
# conn = sqlite3.connect("task2.db")
# conn.commit()
# cursor = conn.cursor()
#
# cursor.execute("""
#    CREATE TABLE IF NOT EXISTS tbl1(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    txt TEXT)
# """)
# conn.commit()
#
# cursor.execute("""
#    CREATE TABLE IF NOT EXISTS tbl2(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    intg INTEGER)
# """)
# conn.commit()
# st = input('Введите список:')
# lst = list(st.split())
#
# for i in range(len(lst)):
#     if lst[i][0].isalpha():
#         cursor.execute("""INSERT INTO tbl1 VALUES(NULL,?)""", (lst[i],))
#         cursor.execute("""INSERT INTO tbl2 VALUES(NULL,?)""", (len(lst[i]),))
#         conn.commit()
#     else:
#         if (int(lst[i]))%2 == 0:
#             cursor.execute("""INSERT INTO tbl2 VALUES(NULL,?)""", (lst[i],))
#             conn.commit()
#         else:
#             cursor.execute("""INSERT INTO tbl1 VALUES(NULL,?)""", ('нечётное', ))
#             conn.commit()
#
# cursor.execute("""SELECT * FROM tbl2""")
# data = cursor.fetchall()
# k = 0
# for i in data:
#     k = k + 1
#
# if k>5:
#     print('deleting')
#     cursor.execute("""DELETE FROM tbl1 WHERE id = 1""")
#     conn.commit()
# else:
#     print('updating')
#     cursor.execute("""
#         UPDATE tbl1
#         SET txt = 'hello'
#         WHERE id = 1
#     """)
#
# cursor.execute("""SELECT * FROM tbl1""")
# data = cursor.fetchall()
# for i in data:
#     print(*i)
#
# cursor.execute("""SELECT * FROM tbl2""")
# data = cursor.fetchall()
#
# for i in data:
#     print(*i)
