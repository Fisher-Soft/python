# # print(17/2*3+2)
# # print(2+17/2*3)
# # print(19%4+15/2*3)
# # print((15+6)-10*4)
# # print(17/2%2*3**3)
# # Next task
# print(17/2*(3+2))
# print((2+17)/2*3)
# print(19%(4+15)/2*3)
# print(((15+6)-10)*4)
# print(17/2%(2*3**3))
# print("рублей осталось ",11-1.5*3)
# a = 2
# b = 5
# print("У Анны ",a," яблока, у Пола ",b)
# r = 7 # ребро куба
# print("Объём куба = ",r**3," , площадь его поверхности = ", r**2)
# z = int(input("Введите количество суток:"))
# print(z,"суток =",z*24,"часов =",z*24*60,"минут =",z*24*60*60,"секунд")
# # task 8
# a, b = map(int, input("enter a b:").split())
# print('Можно отрезать ',(a//30)*(b//30),"квадратов")
# task 9
# n = int(input())
# print(n//3600,"часов")
# n = n - (n//3600)*3600
# print(n//60,"минут")
# n = n - (n//60)*60
# print(n,"секунд")
# X1 = int(input("Input X1:"))
# Y1 = int(input("Input Y1:"))
# X2 = int(input("Input X2:"))
# Y2 = int(input("Input Y2:"))
# if (X1==X2) or (Y1==Y2):
#     print("Ладья бьёт")
# else:
#     # print("не бьёт")
# task 1
# a = int(input("Введите число:"))
# if (a % 10)==3:
#     print(True)
# else:
#     print(False)
# task 2
# a, b, c = map(int, input("enter a b c:").split())
# if a<0 or b<0 or c<0:
#     print(True)
# else:
#     print(False)
# task 3
# n, k = map(int, input("enter n k:").split())
# if (k%2) == (n%2):
#     print("True")
# else:
#     print("False")
# task 4
# X = int(input("enter X:"))
# if (X%3) == 0 and (X%10 == 5):
#     print("True")
# else:
#     print("False")
# task 5
# a, b, c = map(int, input("enter a b c:").split())
# d = 0
# if a%2 == 0:
#     d = d+1
# if b%2 == 0:
#     d = d +1
# if c%2 == 0:
#     d = d + 1
# print("Количество чётных чисел:",d)
# task 6
# X = int(input("enter X:"))
# X2 = X%10
# X1 = X//10
# if X1+X2 > 9:
#     print("Да")
# else:
#     print("Нет")
# task 7
# X = int(input("enter X:"))
# if X<1000:
#     print("Введите корректное число!")
#     exit(0)
# X4 = X%10
# X = X//10
# X3 = X%10
# X = X//10
# X2 = X%10
# X = X//10
# if X4==X3==X2==X:
#     print("Да")
# else:
#     print("Нет")
# task 8
# X = int(input("Введите год:"))
# if (X%4)==0 and (X%100) != 0 and (X%400) != 0:
#     print("Високосный")
# else:
#     print("Не високосный")
# # task 10
# x1, y1, x2, y2 = map(int, input("enter x1 y1 x2 y2:").split())
# if (x1+x2+y1+y2)<4 or (x1+x2+y1+y2)>32:
#     print("Введите корректное число!")
#     exit(0)
# if (x1+y1)%2 == (x2+y2)%2:
#     print("два поля одного цвета")
#
# else:
#     print("два поля разного цвета")
# if (x1 == x2) or (y1 == y2) or (x1 + y1) == (x2 + y2) or ((x2 - x1) == (y2-y1)):
#     print("Ферзь угрожает!")
# else:
#     print("Ферзь не угрожает!")
# task 10-c
# x1, y1, x2, y2 = map(int, input("enter x1 y1 x2 y2:").split())
# if (x1+x2+y1+y2)<4 or (x1+x2+y1+y2)>32:
#     print("Введите корректное число!")
#     exit(0)
# if (x1 == x2) or (y1 == y2):
#     print("Ладья бъёт пешку!")
# else:
#     print("Ладья не бъёт пешку!")
# if ((x2 + 1 == x1) and (y2 == y1-1)) or ((x2 + 1 == x1) and (y2 == y1+1)):
#     print("Пешка бъёт ладью!")
# else:
#     print("Пешка не бъёт ладью!")
# str = input("Введите строку:")
# if str == str[::-1]:
#     print("Слово - перевёртыш")
# else:
#     print("Слово - не перевёртыш")
# task 3-1
# str = input("Введите строку:")
# print(str[2])
# print(str[-2])
# print(str[0:5:1])
# print(str[0:len(str)-2:1])
# print(str[0::2])
# print(str[1::2])
# print(str[::-1])
# print(str[::-2])
# print(len(str))
# task 3-2
# str = input("Введите строку:")
# if str[0] == str[-1]:
#     print("Верно")
# else:
#     print("Не верно")
# task 3-3
# str = input("Введите строку:")
# print(str[1:4])
# task 3-4
# str = "яблоко"
# print(str[1:5])
# print(str[3::])
# task 3-5
# str = "*"
# print(str*5)
# task 3-6
# str = input("Введите строку:")
# if str == str[::-1]:
#     print("Слово - перевёртыш")
# else:
#     print("Слово - не перевёртыш")
# task 3-7
# str = input("Введите строку:")
# if str.count("f") == 1:
#     print(str.index("f"))
# elif str.count("f") > 1:
#     print(str.index("f"))
#     print(str.count("f"))
# task 3-8
# str = input("Введите строку:")
# if str.count("f") == 1:
#     print("-1")
# elif str.count("f") == 0:
#     print("-2")
# if str.count("f") > 1:
#     print(str.find("f",str.index("f")+1))
# task 3-9
# str = input("Введите строку:")
# str2 = str.replace("1","one")
# print(str2)
#task 3-10
# str = input("Введите строку:")
# print((str.lower().count("g") + str.lower().count("c"))/len(str)*100)
#task 3-11
# str = input("Введите строку:")
# print(str.replace("."," "))
# N1 = int(str[0:3])
# N2 = int(str[4:7])
# N3 = int(str[8:9])
# N4 = int(str[10:11])
# print(N1+N2+N3+N4)
# s = input()
# s1 = ''
#
# for i in range(0,len(s)):
#     if (s[i] != 'b') or (s[i] == 'b' and not s[i+1].isnumeric()):
#         s1=s1+s[i]
# print(s1)
# task 4-1
# for i in range(20):
#     print("10")
# task 4-2
# a = 2
# b = 5
# for i in range(a,b+1):
#     print(i)
# task 4-3
# N = 6
# for i in range(1,N):
#     print(i*i*i,end=" ")
# task 4-4
# for i in range(-100,101):
#     print(i,end=" ")
# task 4-5
# a = 6
# for i in range(1,a*10+1):
#     if i%2 == 0:
#         print(i)
# # task 4-6
# S = 0
# for i in range(100,501):
#     S = S + i
# print(S)
# task 4-7
# M = 1
# for i in range(5,21):
#     M = M * i
# print(M)
# task 4-8
# n = 5
# F = 1
# for i in range(1,n+1):
#     F = F * i
# print(F)

# # task 4-10
# s=input("Введите строку:")
# s1=""
# for i in range(len(s)):
#     if s[i] not in s1:
#         s1=s1+s[i]
# print(s1)
# # task 4-11
# s=input("Введите строку:")
# s1=""
# for i in range(len(s)):
#     if s[i] != " ":
#         s1=s1+s[i]
#     else:
#         if int(s1)%2 == 0:
#             print(s1,end=" ")
#         s1=""

# task 4-12
# s=input("Введите строку:")
# s=s.lower()
# s1=""
# s2=""
# for i in range(len(s)):
#     if s1=="":
#         s1=s[i]
#         continue
#     if s[i]==s1[-1]:
#         s1=s1+s[i]
#     if (s[i] != s1[-1]) and (s1 !=""):
#         s2=s2+s1[-1]+str(len(s1))
#         s1=s[i]
# s2=s2+s1[-1]+str(len(s1))
# print(s2)

# #task 4-9
# s=input("Введите текст:")
# s1=""
# for i in range(len(s)-1):
#     if s[i] != " " and s[i+1] == " ":
#         s1=s1+s[i]
# if s[-1] != " ":
#     s1 = s1 + s[-1]
# for i in range(len(s1)):
#     if (s1.count(s1[i]) > 1) and (s1.rfind(s1[i]) == i):
#         print(f"На букву {s1[i]} заканчивается {s1.count(s1[i])} слов(а).")
# task 5-1
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1
# task 5-2
# n = int(input())
# sum = 0
# i = 0
# while i<= n:
#     if i%2 == 0:
#         sum = sum + i
#     i = i +1
# print(sum)

# task 5-3
# n = input("Введите натуральное число:")
# pr = 1
# for elem in n:
#     if int(elem)%2 == 0 and elem != "0":
#         pr=pr*int(elem)
# print (pr)

# task 5-8
# n = input("Введите натуральное число:")
# min = int(n[-1])
# for i in range(len(n)):
#     if min> int(n[i]):
#         min = int(n[i])
# print(min)
# task 5-9
# list = []
# max = 0
# while True:
#     number = int(input("enter number:"))
#     if number < 0:
#         break
#     else:
#         list.append(number)
# for i in range(len(list)):
#     if max < list[i]:
#         max = list[i]
# print(max)

# task 5-10
# list = []
# flag = True
# while True:
#     number = int(input("enter number:"))
#     if number < 0:
#         break
#     else:
#         list.append(number)
# for i in range(len(list)-1):
#     if list[i] != list[i+1]:
#         flag = False
# print(flag)
# task 5-11
# a = int(input("Введите а:"))
# b = int(input("Введите b:"))
# a1 = a
# b1 = b
# count = 0
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# nod = a + b
# nok = (a1 * b1 // nod)
# print("Число кусков торта =",nok)

# task 5-9-2
# s = ""
# s1 = ""
# max = 0
# while True:
#     number = int(input("enter number:"))
#     if number < 0:
#         break
#     else:
#         s=s+str(number)+" "
# for i in range(len(s)):
#     if s[i] != " ":
#         s1=s1+s[i]
#     else:
#         if max < int(s1):
#             max = int(s1)
#         s1=""
# print(max)
# n=int(input())
# s1=""
# for i in range(1,n+1):
#     s=str(i)
#     if s[-1] in ["2","3","4"]:
#         s1='ы'
#     if s[-1] in ["5","6","7","8","9","0"]:
#         s1=''
#     if s[-1] == "1":
#         s1='а'
#     if i in [11,12,13,14]:
#         s1=""
#     s1="коров"+s1
#     print("На лугу",i,s1)
# def fiba(i):
#     if i==1 or i==2:
#         return i
#     else:
#         return fiba(i-1)+fiba(i-2)
#
#
# print(fiba(7))
# print(chr(145))
# print(ord("z"))

# task 6-1
# n = int(input("Введите n:"))
# for i in range(1,11):
#     print(f"{i} x {n} =",(i*n))
# task 6-2
# i = 1
# p = 1
# while i<=10:
#     num = int(input(f"Введите {i}-ое число:"))
#     i = i + 1
#     if num != 0:
#         p=p*num
# print("Произведение равно",p)
# task 6-3
# n = int(input("Введите n:"))
# while n>0:
#     print(str(n)*n)
#     n = n -1
# task 6-4
# str1 = input("Введите трёхзначное число :")
# print("Сумма цифр равна:",int(str1[-1])+int(str1[-2])+int(str1[-3]))
# task 6-5
# n = int(input("Введите n:"))
# for i in range(1,n+1):
#     k = 0
#     for j in range(1,n+1):
#         if i % j == 0:
#             k = k+1
#     print(i,"+"*k)
# task 6-6
# a = int(input("a="))
# b = int(input("b="))
# for i in range(a,b+1):
#     k = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             k = k+1
#     if k == 2:
#         print(i)
# task 6-7
# for i in range(100,999):
#     s = str(i)
#     if (s[-1] == s[-2]) or (s[-1] == s[-3]) or (s[-2] == s[-3]):
#         continue
#     print(i)
# task 6-8
# s = input("Введите строку символов:")
# print(s[0],end="")
# for i in range(1,len(s)):
#     if s[i-1] != "*":
#         print(s[i],end="")
# task 6-9
# s = input("Введите строку символов:")
# s1=s[0]
# for i in range(1,len(s)):
#     if s[i - 1] == ",":
#         s1=s1+" "+s[i]
#     else:
#         s1=s1+s[i]
# s2=s1[0]
# for i in range(1,len(s1)):
#     if (s1[i] == " ") and (s2[-1] == " "):
#         continue
#     else:
#         s2=s2+s1[i]
# print(s2)
# task 6-10
# z=0
# for i in range(2,999):
#     k = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             k = k+1
#     if k == 2:
#         print(i)
#         z = z + 1
#     if z>=100:
#         exit(0)
# task 6-11
# n = int(input("n="))
# for i100 in range(0,n):
#     for i20 in range(0,n):
#         for i10 in range(0,n):
#             for i5 in range(0,n):
#                 for i1 in range(1,n+1):
#                     z = i1+i5*5+i10*10+i20*20+i100*100
#                     if z == n:
#                         print()
#                         if i100>0:
#                             for q in range(1,i100+1):
#                                 print("100 +",end=" ")
#                         if i20>0:
#                             for q in range(1, i20 + 1):
#                                 print("20 +", end=" ")
#                         if i10>0:
#                             for q in range(1, i10 + 1):
#                                 print("10 +", end=" ")
#                         if i5>0:
#                             for q in range(1,i5+1):
#                                 print("5 +",end=" ")
#                         if i1>0:
#                             for q in range(1,i1+1):
#                                 print("1 + ",end=" ")



# print("a" + "x" if "123".isdigit() else "y" +"b")
#
# for i in range(1,10):
#     i-=5
# print(i)

# i = 0
# while i < 10:
#     i+=1
# i-=10
# print(i)

# for i in range(5):
#     if i % 2 ==0:
#         continue
#     print(i)


# task 1
# a = input("Введите семизначное число:")
# ch = 0
# nech = 0
# s = 0
# pr = 1
# for i in range(7):
#     s = s + int(a[i])
#     if int(a[i]) % 2 == 0:
#         ch = ch +1
#     else:
#         nech = nech +1
# if ch > nech:
#     print("Сумма всех цифр =",s)
# else:
#     pr = int(a[0])*int(a[2])*int(a[5])
#     print("Произведение 1, 3 и 6 цифр=",pr)

# task 4
# from random import randint
# resalt = 0
# n = input("Введите искомую цифру:")
# kol = input("Введите количество чисел:")
# for i in range(int(kol)):
#     new = randint(0, 100)
#     print (new,end=" ")
#     resalt = resalt + str(new).count(n)
# print()
# print(f"Цифра {n} встречается {resalt} раз")

# task 2
# text = input("Введите текст:")
# text.lower()
# vg = 0
# vs = 0
# allg = ""
# for i in range(len(text)):
#     if text[i] in ('a', 'e', 'i', 'o', 'u', 'y'):
#         allg = allg + text[i]
#         vg = vg +1
#     else:
#         vs = vs+1
# if vg == vs:
#     print("Количество гласных и согласных равно. Гласные: ",allg)
# else:
#     print("Гласных ",vg," согласных ",vs)


# task 5
# st = input("Введите строку:")
# fl = False
# num = ""
# for i in range(len(st)):
#     if st[i].isdigit():
#         fl = True
#         num = num+st[i]
#     elif fl:
#         print(num)
#         fl = False
#         num = ""
# if num !="":
#     print(num)

# # task 3
# from random import randint
# z = 0
# for i in range(7):
#     print(f"{i+1}-я итерация.")
#     a1 = input("Введите первое число в диапазоне от 1 до 20:")
#     a2 = input("Введите второе число в диапазоне от 1 до 20:")
#     para1 = int(a1) + int(a2)
#     new1 = randint(1, 20)
#     new2 = randint(1, 20)
#     print("Случайная пара:",new1,new2)
#     if i == 3:
#         n1 = new1
#         n2 = new2
#     para2 = new1 + new2
#     if para1 > para2:
#         z = z +1
# if z > 0:
#     print(f"Пара с клавиатуры была больше случайной пары {z} раз")
# else:
#     print("Случайные числа четвёртой итерации:", n1,n2)


# from random import randint
# l = []
# for i in range(10):
#     l.append(randint(1, 20))
#     print(l[i])
# l.sort()
# print(l)
# l.reverse()
# print(l)

# task 8-1
# sp = [1,2,3,4,5,6,7,8,9]
# for i in sp:
#     if i % 2 == 0:
#         print(i)

# task 8-2
# sp1 = [9,8,7,66,5,44,33,22]
# sp2 = [21,32,43,54,65,76,87]
# sp1.sort()
# for i in sp1:
#     if i not in sp2:
#         print(i)
#         exit(0)
# print("There is not.")

# task 8-3
# sp = []
# k = int(input("k="))
# for i in range(1,k+1):
#     el = input("Введите "+str(i)+"-й элемент:")
#     sp.append(el)
# kol = 0
# for i in range(0,k-1):
#     if sp[i]>sp[i+1]:
#         kol = kol + 1
# print(kol)

# task 8-4
# st = input("Введите строку:")
# sp = []
# sp.append(st[0])
# for i in range(1,len(st)):
#     if st[i] not in sp:
#         sp.append(st[i])
# print(*sp)

# task 8-5
# from random import randint
# sp = []
# sp2 = []
# for i in range(10):
#     sp.append(randint(1,99))
# print("Исходный список:",sp)
# i = 0
# for i in range(len(sp)):
#     sp2.append(sp[i])
#     if sp[i] % 2 == 0:
#         st = str(sp[i])
#         st2 = st[::-1]
#         sp2.append(int(st2))
# print("Новый список:",sp2)

# task 8-6
# from random import randint
# sp = []
# for i in range(10):
#     sp.append(randint(1,99))
# print("Исходный список:",sp)
# for i in sp:
#     print("Элемент",i," встречается в списке",sp.count(i)," раз(a)")

# task 8-7
# from random import randint
# sp = []
# spp = []
# spo = []
# sp0 = []
# for i in range(15):
#     sp.append(randint(-99,99))
# print("Исходный список:",sp)
# for i in sp:
#     if i <0:
#         spo.append(i)
#     if i>0:
#         spp.append(i)
#     if i==0:
#         sp0.append(i)
# sp.clear()
# sp.extend(spp)
# sp.extend(spo)
# sp.extend(sp0)
# print("Обработанный список:",sp)

# task 8-8
# from random import randint
# sp = []
# spp = []
# for i in range(10):
#     sp.append(randint(0,9))
# print("Исходный список:",sp)
# for i in sp:
#     spp.append(i)
#     if sp.count(i) == 1:
#         spp.append(i)
# print("Обработанный список:",spp)


# task 8-9
import random
from random import randint
# sp = [1,3,5,7,9,2,4,6,8,10]
# sp1 = []
# sp2 = []
# spf = []
# print("Исходный список:",sp)
# for i in sp:
#     if i % 2 == 0:
#         sp2.append(i)
#     else:
#         sp1.append(i)
# i = 0
# while i<len(sp2):
#     spf.append(sp2[i])
#     spf.append(sp1[i])
#     i = i +1
# print("Обработанный список:",spf)

# # task 8-10
# sp = []
# sp2 = []
# i = 0
# st=""
# while True:
#     s = input("Введите команду:")
#     if s !='.':
#         sp.append(s)
#     else:
#         break
# i = 0
# for j in range(len(sp)):
#     if "POST" in sp[j]:
#         st=sp[j]
#         st=st[5:]
#         sp2.append(st)
#         i = i +1
#     if "DELETE" in sp[j]:
#         del sp2[i-1]
#         i = i -1
#     if "GET" in sp[j]:
#         print(sp2[i-1])

# newlist = [x for x in range(10,100) if x%2==1]
# print(newlist)
# newlist = [x*x for x in range(1,11)]
# print(newlist)
# newlist = [x for x in range(100,1000) if x%3==0 and x%5 ==0]
# print(newlist)

# a, b, c = map(int, input("enter a b c:").split())
# newlist = [x**c for x in range(a,b+1)]
# print(*newlist)
# kol = 0
# sp = [1,1,1,2,3,3,4,5,6,7,8,9,9]
# for i in range(len(sp)):
#     if sp.index(sp[i])==i:
#         kol = kol + 1
# print(kol)

# s = input("Введите списое чисел:")
# s = s.split()
# k = 0
# if len(s)==1:
#     print(s[0])
#     exit(0)
# for i in range(len(s)):
#     if i == 0:
#         k = int(s[-1])+int(s[1])
#     elif i == len(s)-1:
#         k = int(s[i-1])+int(s[0])
#     else:
#         k = int(s[i-1])+int(s[i+1])
#     print(k,end=" ")

# s = input("Введите список чисел:")
# s = s.split()
# for i in range(len(s)-1):
#     for j in range(i+1,len(s)):
#         if abs(int(s[i]))<abs(int(s[j])):
#             s[i], s[j] = s[j], s[i]
# print(s)

# s = input("Введите список строк:")
# s = s.split()
# for i in range(len(s)-1):
#     for j in range(i+1,len(s)):
#         if len(s[i])<len(s[j]):
#             s[i], s[j] = s[j], s[i]
# print(s)

# s = input("Введите список слов:")
# s = s.split()
# for i in range(len(s)-1):
#     for j in range(i+1,len(s)):
#         if s[i].count("a") < s[j].count("a"):
#             s[i], s[j] = s[j], s[i]
# print(s)

# s = input("Введите список чисел:")
# s2 = s.split()
# for i in range(len(s2)):
#     if s2.index(s2[i])==i and s2.count(s2[i])>1:
#         print(s2[i], end=" ")

# s = input("Введите список чисел:")
# s2 = s.split()
# i = 0
# while i<len(s2):
#     s2.insert(i+1,"0")
#     i = i +2
# print(*s2)

# n = int(input("n="))
# k = 0
# for i in range(1,n):
#     for j in range(0,i):
#         print(i,end=" ")
#         k = k +1
#         if k==n:
#             exit(0)

# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# if sum(A) > sum (B):
#     print("A>")
# else:
#     print("B>")
# min1 = min(A)
# min2 = min(B)
# print(A.index(min1))
# print(B.index(min2))

# Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
# import random
# k = tuple([random.randint(0,9) for _ in range(10)])
# print(k,sum(k))
#
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
#            'и', 'и', 'т', 'т', 'а', 'и', 'и',
#            'и', 'и', 'и', 'т', 'и')
# all = len(long_word)
# t = int(long_word.count('т'))/all
# a = int(long_word.count('а'))/all
# i = int(long_word.count('и'))/all
# print(t*100,a*100,i*100)

# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))

# task 10-1
# t = [random.randint(0,100) for i in range(20)]
# tp = tuple(t)
# print(tp)
# for i in range(10):
#     k = tp[i]
#     s = 1
#     for j in range(2,k):
#         if k%j==0:
#             s = s + j
#     if s == k:
#         print(k)

# task 10-2
# tp = (23, 45, 'masha', 'dasha', 67, 89, 'kasha')
# t = []
# for elem in tp:
#     if type(elem)==str:
#         t.append(elem[::-1])
#     elif type(elem) == int:
#         t.append(elem*2)
# print(tuple(t))

# task 10-3
# t = [random.randint(0,100) for i in range(20)]
# tp = tuple(t)
# print("Разность =",max(tp)-min(tp))

# task 10-4
# s = input("Введите список чисел:")
# s2 = tuple(s.split())
# min1 = s2.index(min(s2))
# max1 = s2.index(max(s2))
# print(abs(min1-max1)-1)

# task 10-5
# t = [random.randint(-10,10) for i in range(20)]
# tp = tuple(t)
# print(tp)
# k = 0
# if tp[0]<0:
#     znak = -1
# else:
#     znak = 1
# for i in range(1,20):
#     if tp[i]*znak<0:
#         k = k + 1
#         znak = - znak
# print(k)

# task 10-6
# t = [random.randint(2,100) for i in range(20)]
# tp = tuple(t)
# print(tp)
# for elem in tp:
#     k = 0
#     for j in range(1,elem+1):
#         if elem%j == 0:
#             k = k + 1
#     if k == 2:
#         print(elem,end=" ")

# task 10-7
# s = input("Введите список чисел:")
# s2 = tuple(s.split())
# min1 = s2.index(min(s2))
# max1 = s2.index(max(s2))
# if min1 > max1:
#     a = min1
#     b = max1
# else:
#     a = max1
#     b = min1
# ss = 0
# for j in range(b+1,a):
#     ss = ss + int(s2[j])
# print(ss)

# task 10-8
# t = [random.randint(-10,10) for i in range(10)]
# tp = tuple(t)
# print(tp)
# if tp[1]>=tp[0]:
#     znak = 1
# else:
#     znak = -1
# max2 = k = 2
# for i in range(2,10):
#     if (tp[i]>=tp[i-1] and znak == 1) or (tp[i]<=tp[i-1] and znak == -1):
#         k = k+1
#     if (znak == 1 and tp[i]<tp[i-1]) or (znak == -1 and tp[i]>tp[i-1]):
#         znak = - znak
#         if max2 < k:
#             max2 = k
#         k = 2
# print(max(max2,k))

# task 10-9
# t = [random.randint(-10,10) for i in range(10)]
# tp = tuple(t)
# print(tp)
# for i in range(len(tp)-1):
#     flag = False
#     for j in range(i+1,len(tp)):
#         if tp[i]==tp[j]:
#             flag = True
#     if flag:
#         print(tp[i])

# car = {
#   "BMW": ["320i","X5","X6"],
#   "Tesla": ["S1","T1","TT"]
# }
# print(list(car["BMW"])[0], list(car["BMW"])[-1])
# print(list(car["Tesla"])[0], list(car["Tesla"])[-1])

# car = {
#     "BMW": 2,
#     "Tesla": 3,
#     "Priora": 4
# }
# p=1
# for i in car:
#    p=p*car[i]
# print(p)
#
# product = {
#     "melon": [200, 6.22],
#     "water": [500, 5.52],
#     "apple": [100, 6.21],
#     "cheese": [5, 52.52],
#     'butter': [20, 3.61]
# }
# summa = 0
# while True:
#     name_product = input("enter name product or exit:")
#     if name_product == "exit":
#         break
#     if name_product in product:
#         print('You can buy',product[name_product][0])
#         ss = int(input("How many do you want:"))
#         if ss>product[name_product][0]:
#             print('I am sorry, we do not have enough.')
#         else:
#             summa = summa+ss*product[name_product][1]
#             product[name_product][0] = product[name_product][0] - ss
#     else:
#         print(f"no product name {name_product}")
#
# print("It costs",summa)

# task 11-1
# school = {
#     "9a": 28,
#     "9b": 30,
#     "9v": 29,
#     "9m": 26,
#     '9f': 25
# }
# print(school)
# kl = input("Введите класс:")
# if kl not in school:
#     print("Не корректный ввод.")
#     exit(0)
# n = input("Введите количество учащихся")
# school[kl]=n
# print(school)
# kl = input("Введите новый класс:")
# n = input("Введите количество учащихся")
# school[kl]=n
# print(school)
# kl = input("Введите расформированный класс:")
# if kl in school:
#     school.pop(kl)
# print(school)
# su = sum(list(school.values()))
# print("Общее количество учащихся 9 классов в школе:",su)

# task 11-2
# school = {
#      "большой": "огромный",
#      "маленький": "мизерный",
#      "добрый": "душевный",
#      "влажный": "мокрый",
#      "робкий": "застенчивый"
# }
# print(school)
# sl = input("Введите слово:")
# if sl in school.keys():
#     print(school[sl])
# elif sl in school.values():
#     for i,j in school.items():
#         if j==sl:
#             print(i)
# else:
#     print("Нет подходящего слова.")

# task 11-3
# sp = {}
# while True:
#     st = input("Введите запрос:")
#     if st == ".":
#         exit(0)
#     if " " in st:
#         st2 = st.split()
#         sp[st2[0]]=st2[1]
#     else:
#         print(sp[st])

# task 11-4
# sp = {}
# while True:
#     st = input("Введите строку:")
#     if st == ".":
#         break
#     st2 = st.split()
#     st3 = ' '.join(st2[2:])
#     sp[st2[0]] = st3
# m = int(input("Введите количество запросов:"))
# for i in range(m):
#     st4 = input(f"Введите {i+1}-й запрос:")
#     if st4 in sp:
#         print(st4,"это",sp[st4])
#     else:
#         print("Не найдено")

# task 11-5
# st = input("Введите строку:")
# st = st.lower()
# st1 = list(st.split())
# for i in range(len(st1)):
#     if st1.index(st1[i])==i:
#         print(st1[i],st1.count(st1[i]))

# task 11-6
# sp = {}
# while True:
#     st = input("Введите запрос:")
#     if st == ".":
#         exit(0)
#     st2 = st.split()
#     if " " in st:
#         if st2[0] not in sp:
#             sp[st2[0]]=st2[1]
#         else:
#             lt = sp[st2[0]] + ","+st2[1]
#             sp[st2[0]] = lt
#     if st2[0] not in sp:
#         print("Не найдено")
#     if len(st2)==1:
#         print(sp[st2[0]])

# task 12-1
# s = input("Введите список чисел:")
# l = s.split()
# st = set(l)
# print("Различных чисел в списке",len(st))

# task 12-2
# s1 = input("Введите первый список чисел:")
# l1 = s1.split()
# s2 = input("Введите второй список чисел:")
# l2 = s2.split()
# st1 = set(l1)
# st2 = set(l2)
# print (len(st1.intersection(st2)),"чисел/числа содержится одновременно как в первом списке, так и во втором.")

# task 12-3
# s1 = input("Введите первый список чисел:")
# l1 = s1.split()
# s2 = input("Введите второй список чисел:")
# l2 = s2.split()
# st1 = set(l1)
# st2 = set(l2)
# print ("Все числа, которые не содержатся одновременно в этих двух списках:",*st1.symmetric_difference(st2))

# task 12-4
# s = input("Введите начальный список чисел:")
# l = s.split()
# st = set(l)
# print(st)
# while True:
#      s2 = input("Введите очередное число:")
#      if s2 in st:
#           print("Yes")
#      else:
#           print("No")
#           st.add(s2)

# task 12-5
# s = input("Введите список элементов:")
# l = s.split()
# st = set(l)
# print(len(l)-len(st))

# task 12-6
# st = set()
# s4 = set()
# n = int(input("n:"))
# num = int(input("Число:"))
# for i in range(1,n+1):
#      st.add(i)
# print(*st)
# k = 1
# while True:
#      s2 = input("Enter guess:")
#      s3 = s2.split()
#      s4.clear()
#      for i in s3:
#           s4.add(int(i))
#      if num in s4:
#           if len(s4) == 1:
#               print(f"YES: {s2} is correct. You answered on the {k}-th try.")
#               break
#           else:
#                st.clear()
#                st = st.union(s4)
#                s5 = list(st)
#                s5.sort()
#                print("YES:",*s5)
#
#      else:
#           st.symmetric_difference_update(s4)
#           s5 = list(st)
#           s5.sort()
#           print("NO:",*s5)
#      k = k + 1

#task 13-1
# import random
# lst = [[random.randint(1,7) for _ in range(5)] for _ in range(5)]
# max = -1
# print(lst)
# for i in range(5):
#      flag = True
#      summa = 0
#      for j in range(5):
#           if lst[i][j]%2==1:
#                summa += abs(lst[i][j])
#           else:
#                flag = False
#      if max < summa and flag:
#           max = summa
# if max==-1:
#      print("Нет подходящей строки.")
# else:
#      print(max)



#task 13-2
# n = int(input("Введите n:"))
# lst = [['.' for _ in range(n)] for _ in range(n)]
# for i in range(n):
#      lst[int(n//2)][i]='*'
#      lst[i][int(n // 2)] = '*'
#      lst[i][i] = '*'
#      lst[n-i-1][i] = '*'
# for i in range(n):
#      for j in range(n):
#           print(lst[i][j],end=" ")
#      print()

#task 13-3
# n = int(input("Введите n:"))
# m = int(input("Введите m:"))
# lst1 = []
# lst = []
# for i in range(n):
#      for j in range(m):
#           if (i+j)%2==0:
#                lst1.append('.')
#           else:
#                lst1.append('*')
#      print(lst1)
#      lst.append(lst1)
#      lst1.clear()

#task 13-5
# lst = [[(i+1)**(j+1) for i in range(5)] for j in range(4)]
# for i in range(4):
#      for j in range(5):
#           print(lst[i][j],end=" ")
#      print()

#task 13-6
# import random
# n = int(input("Введите n:"))
# lst = [[random.randint(1,9) for _ in range(n)] for _ in range(n)]
# print(lst)
# for i in range(n):
#      s = ''
#      for j in range(n):
#           s=s+str(lst[i][j])
#      if s == s[::-1]:
#           print("YES")
#           exit(0)
# print("NO")

#task 13-7
# try:
#      x = (1, 2, 5, 7)
#      x = x / 2
#      print(x)
# except Exception as e:
#     print(e)
#     print(type(e))
# finally:
#     print("Повнимательнее!")

# #task 13-8
# lst = [[(i+1)**(j+1) for i in range(5)] for j in range(4)]
# try:
#      print(lst[6][7])
# except IndexError:
#     print("К сожалению вы вышли за рамки.")

# #task 13-9
# s = "Маша"
# try:
#      s=s+13
# except TypeError:
#     print("К сожалению мы не можем это сделать.")

# task 13-10
# a,b,c = map(int,input("Введите стороны треугольника a,b,c:").split())
# try:
#      if a==0 or b==0 or c==0:
#           raise ArithmeticError
# except ArithmeticError:
#      print("Сторона не может быть нулевой.")
#      exit(0)
# p = (a+b+c)/2
# s=(p*(p-a)*(p-b)*(p-c))**(1/2)
# print("Площадь равна:",s)

# task 13-11
# import random
# n = random.randint(3,10)
# lst=[random.randint(0,10) for _ in range(n)]
# print(lst)
# while True:
#      m = int(input("Введите элемент в списке:"))
#      try:
#           lst.remove(m)
#      except ValueError:
#           print("Такого элемента нет в списке.")
#           raise TypeError
#           break

# task 13-15
# import random
# n = random.randint(2,5)
# m = random.randint(2,5)
# lst = [[random.randint(1,9) for _ in range(n)] for _ in range(m)]
# print(lst)
# for i in range(n):
#      for j in range(m):
#           print(lst[j][i], end=" ")
#      print()

#task 13-16
# n = int(input("Введите n:"))
# k=0
# for i in range(n):
#      s = ''
#      for j in range(n):
#           k = k + 1
#           if i%2==0:
#                s = s + str(k) + " "
#           else:
#                s = str(k)+" "+s
#      print(s)
#
# task 14-1-6
# f = open('file.txt','w',encoding="utf-8")
# for i in range(6):
#      str1 = input('Введите '+str(i+1)+'-ю строку:')
#      f.write(str1+'\n')
# f.close()
# f = open('file.txt','a',encoding="utf-8")
# for i in range(3):
#      str1 = input('Введите дополнительную '+str(i+1)+'-ю строку:')
#      f.write(str1+'\n')
# f.close()
# f = open('file.txt','r',encoding="utf-8")
# sm = 0
# for ln in f:
#      sm += len(ln)-1
# print("Количество символов = ",sm)
# f.close()
# f = open('file.txt','r',encoding="utf-8")
# sp = []
# for ln in f:
#      ln2 = ln.replace("\n",'')
#      sp.append(ln2)
# print(sp)
# f.close()
# f = open('file.txt','r',encoding="utf-8")
# for ln in f:
#      ln2 = ln.replace("\n",'!')
#      print(ln2)
# f.close()
# mx = 0
# k = 0
# k2 = 0
# st2=''
# f = open('file.txt','r',encoding="utf-8")
# for ln in f:
#      st = f.readline()
#      k +=1
#      if mx<len(ln)-1:
#           mx=len(ln)-1
#           k2 = k
#           st2=ln
# print(f'Длина самой большой строки {mx}. Её номер {k2}. Это строка:',end=" ")
# print(st2)

# task 14-7
# st2 = []
# st = input('Введите 10 чисел через пробел:')
# f = open('input.txt','w',encoding="utf-8")
# f.write(st)
# f.close()
# p = 1
# f = open('input.txt','r',encoding="utf-8")
# st2 = list(f.readline().split())
# for el in st2:
#      p = p * int(el)
# f2 = open('output.txt','w',encoding="utf-8")
# f2.write(str(p))
# f.close()
# f2.close()

# task 14-8
# f = open('file.txt','r',encoding="utf-8")
# f2 = open('file2.txt','w',encoding="utf-8")
# f3 = open('file3.txt','w',encoding="utf-8")
# k = 0
# for ln in f:
#      k = k + 1
#      if k%2==0:
#           f2.write(ln)
#      else:
#           f3.write(ln)
# f.close()
# f2.close()
# f3.close()

# task 14-9
# f1 = open('file.txt','r',encoding="utf-8")
# f2 = open('file2.txt','r',encoding="utf-8")
# k = 0
# flag = False
# for el1 in f1:
#      el2 = f2.readline()
#      k +=1
#      if el1 != el2:
#           flag = True
#           print(f"Отличается в {k} строке")
#           break
# if not flag:
#      print("Файлы не отличаются.")
# f1.close()
# f2.close()

# task 14-10
# f2 = open('file3.txt','w',encoding="utf-8")
# while True:
#      st = input("Введите номер рейса, пункт назначения, время вылета (через пробел\ точка - выход):")
#      if st == '.':
#           break
#      else:
#           f2.write(st+'\n')
# f2.close()
# st2 = input("Введите пункт назначения:")
# f2 = open('file3.txt','r',encoding="utf-8")
# for el in f2:
#      if st2 in el:
#           st3=list(el.split())
#           print(st3[0], st3[2])
# f2.close()

# task 14-11
# f2 = open('file4.txt','w',encoding="utf-8")
# while True:
#      st = input("Введите ФИО студента и четыре оценки(через пробел\ точка - выход):")
#      if st == '.':
#           break
#      else:
#           f2.write(st+'\n')
# f2.close()
# f2 = open('file4.txt','r',encoding="utf-8")
# for el in f2:
#      st3=list(el.split())
#      srb = (int(st3[3]) + int(st3[4]) + int(st3[5]) + int(st3[6]))/4
#      if srb >7:
#           print(st3[0], st3[1], st3[2])
# f2.close()
# task 14-12
# f2 = open('file5.txt','r',encoding="utf-8")
# f3 = open('file6.txt','w',encoding="utf-8")
# lst = []
# lst2 = []
# for el in f2:
#      s = 0
#      for j in range(len(el)-1):
#           s = s + int(el[j])
#      lst.append(s)
#      lst2.append(el.replace('\n',''))
#      lst.sort()
# for i in range(len(lst)):
#      for j in range(len(lst2)):
#           st = lst2[j]
#           s = 0
#           for k in range(len(st)):
#                s = s + int(st[k])
#           if s == lst[i]:
#                f3.write(st+" ")
# f2.close()
# f3.close()

# task 14-13
# st1 = ''
# st2 = ''
# st3 = ''
# f = open('13.txt','r',encoding="utf-8")
# st = f.readline()
# i = 0
# while i<len(st):
#     if st[i].isalpha() and i ==0:
#         st1 = st[i]
#     if st[i].isalpha() and i !=0:
#         st3 = st3 + st1*int(st2)
#         st2 = ''
#         st1 = st[i]
#     if st[i].isdigit():
#         st2 = st2 + st[i]
#     i = i + 1
# st3 = st3 + st1*int(st2)
# print(st3)
# f.close()

# n,k = map(int,input('n,k:').split())
# lst2 = []
# lst = [[(i+1)*(j+1) for i in range(n)] for j in range(n)]
# nn = 0
# for i in range(n):
#     for j in range(n):
#         if lst[i][j] == k:
#             nn+=1
# print(nn)

# import random
# n = int(input('n='))
# lst = list(input('Value:').split())
# lst2 = lst.copy()
# lst2.sort()
# if int(lst2[0])>n:
#     print('-1')
#     exit(0)
# max = 0
# for i in range(10000000):
#     k = random.randint(1,999999)
#     if '0' in str(k):
#         continue
#     str1 = str(k)
#     s = 0
#     for j in range(len(str1)):
#        s = s + int(lst[int(str1[j])-1])
#     if (s<=n) and (max<k):
#         max = k
# print(max)
#
# n = int(input('n='))
# lst = list(input('Value:').split())
# lst2 = lst.copy()
# lst2.sort()
# if int(lst2[0])>n:
#     print('-1')
#     exit(0)
# nn = n//int(lst2[0])
# n2=n3=n4=n5=n6=n7=n8=n9=1
# if nn>=2:
#     n2=10
# if nn>=3:
#     n3=10
# if nn>=4:
#     n4=10
# if nn>=5:
#     n5=10
# if nn>=6:
#     n6=10
# if nn>=7:
#     n7=10
# if nn>=8:
#     n8=10
# if nn>=9:
#     n9=10
# max = 0
# str1 = ''
# k = 0
# lst.append('0')
# for i1 in range(0,n9):
#     for i2 in range(0,n8):
#         for i3 in range(n7):
#             for i4 in range(n6):
#                 for i5 in range(n5):
#                     for i6 in range(n4):
#                         for i7 in range(n3):
#                             for i8 in range(n2):
#                                 for i9 in range(1,10):
#                                     k = i9+i8*10+i7*100+i6*1000+i5*10000+i4*100000+i3*1000000+i2*10000000+i1*100000000
#                                     if '0' in str(k):
#                                         continue
#                                     s = int(lst[i1-1])+int(lst[i2-1])+int(lst[i3-1])+int(lst[i4-1])+int(lst[i5-1])+int(lst[i6-1])+int(lst[i7-1])+int(lst[i8-1])+int(lst[i9-1])
#                                     # print(k,s,end=' ')
#                                     if (s<=n) and (max<k):
#                                         max = k
# print(max)
# task 1
# s = input('Введите элементв списка через пробел:')
# lst = list(s.split())
# for i in range(len(lst)):
#     if lst.count(lst[i])==1:
#         print(lst[i],end=' ')

# task 2
# s = input('Введите список чисел через пробел:')
# lst = list(s.split())
# lst2 = []
# s = 0
# k = 0
# for i in range(len(lst)):
#     k = lst.count(lst[i])//2
#     if lst[i] not in lst2 and k >0:
#         s = s + k
#         k = 0
#         lst2.append(lst[i])
# print(s)

# task 3
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# c1 = list(C_1)
# c2 = list(C_2)
# if sum(c1)>sum(c2):
#     print('Сумма больше в кортеже - C_1')
# else:
#     print('Сумма больше в кортеже - C_2')
# min1 = min(c1)
# min2 = min(c2)
# max1 = max(c1)
# max2 = max(c2)
# for i in range(len(c1)):
#     if c1[i] == min1:
#         print('Порядковый номер минимального элемента в С_1:',i)
#     if c1[i] == max1:
#         print('Порядковый номер максимального элемента в С_1:', i)
# for i in range(len(c2)):
#     if c2[i] == min2:
#         print('Порядковый номер минимального элемента в С_2:',i)
#     if c2[i] == max2:
#         print('Порядковый номер максимального элемента в С_2:', i)

# task 4
# str = 'An apple a day keeps the doctor away'
# dct = {}
# for i in range(len(str)):
#     k = str.count(str[i])
#     dct.update({str[i]: k})
# for i,g in dct.items():
#     print(i,g)

# task 6
# s1 = input('Введите первый список чисел через пробел:')
# s2 = input('Введите второй список чисел через пробел:')
# ss1 = set(s1.split())
# ss2 = set(s2.split())
# c = ss1.intersection(ss2)
# print(len(c))

# task 7
# a = 10
# b = 0
# try:
#     a = b / c
# except Exception as e:
#     print(e)
#     print(type(e))
# finally:
#     print("Повнимательнее! Делить на ноль - это не модно")

# task 8
# f2 = open('file4.txt','w',encoding="utf-8")
# while True:
#      st = input("Введите ФИ студента и оценку за контрольную (через пробел\ точка - выход):")
#      if st == '.':
#           break
#      else:
#           f2.write(st+'\n')
# f2.close()
# f2 = open('file4.txt','r',encoding="utf-8")
# srb = 0
# k = 0
# for el in f2:
#      st3=list(el.split())
#      srb = srb + int(st3[2])
#      k = k + 1
#      if int(st3[2])<3:
#           print(st3[0], st3[1])
# f2.close()
# print('Средний балл = ',srb/k)

# task 5
dic = {'торт': ['состав', 5, 10],
       'пирожное': ['состав', 12, 20],
       'маффин': ['состав', 7, 30],
       'булочка': ['состав', 5, 7],
       }
while True:
    s = input('Введите команду (описание, цена, количество, всё информацию, покупка:')
    if 'описание' in s:
        for i,j in dic.items():
            print(i,j[0])
    if 'цена' in s:
        for i,j in dic.items():
            print(i,j[1])
    if 'количество' in s:
        for i,j in dic.items():
            print(i,j[2])
    if 'всё информацию' in s:
        for i,j in dic.items():
            print(i,j)
    if 'покупка' in s:
        break
ss = 0
while True:
    s = input('Введите название и количество через пробел (n - выход из программы):')
    if 'n' in s:
        print('Цена выбранных товаров:',ss)
        print('До свидания')
        print('Остаток:',dic)
        break
    lst = list(s.split())
    if int(lst[1])>int(dic[lst[0]][2]):
        print('К сожалению нет достаточного количества товара.')
    else:
        ss = ss + int(dic[lst[0]][1])*int(lst[1])
        dic[lst[0]][2] = int(dic[lst[0]][2]) - int(lst[1])

