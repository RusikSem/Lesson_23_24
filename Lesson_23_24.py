# Задание 3
# Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле должен быть
# обратным по отношению к порядку строк в заданном файле.

#
# def file_gen(name, length):
#     name = name + '.txt'
#     f = open(name, 'wt')
#     for i in range(length + 1):
#         f.write(str(i) + '\n')
#
#     f.close()


# f = open('example3.txt', 'wr')
# l = f.readines()
# f.close()
#
# l.reverse()
#
# f = open('example3.txt', 'wt')
# f.writelines(l)
# f.close()


# Задание 4 Дан текстовый файл. Добавить в него строку из
# двенадцати звездочек (************), поместив ее после
# последней из строк, в которых нет запятой. Если таких
# строк нет, то новая строка должна быть добавлена после
# всех строк имеющегося файла.
# Результат записать в другой файл.


# f = open('example3.txt', 'rt')
# f1 = open('example3r.txt', 'wt')
# flag = False
#
#
# l = f.readines()
# l.reverse()
# for i in range(len(l)):
#     if (',' not in l[i]) and i != 0:
#         l.insert(i, '************\n')
#         flag = True
#         break
# if not flag:
#     l.insert(0, '************\n')
# l.reverse()
# f1.writelines(l)
# f1.close()
# f.close()


# file_gen('example4', 20)
# f = open('example4.txt','rt')
# f1 = open('example4r.txt','wt')
# flag = False
# # a = f.readline()
# # while a:
# #     if ',' in a:
# #
# l = f.readines()
# l.reverse()
# for i in range(len(l)):
#     if (',' not in l[i]) and (',' in l[i+1]):
#         l.insert(i,'************\n')
#         flag = True
#         break
# if not flag:
#     l.insert(0, '************\n')
# l.reverse()
# f1.writelines(l)
# f1.close()
# f.close()


# file_gen('example4', 20)
#
# f = open('example5.txt', 'at')
# for i in range(30, 51):
#     f.write(str(i))
#     f.write('\n')
# f.close()


# a = 4
# b = 0
# try:
#     c = a / b
# except:
#     c = 0
# print(c)


# a = 4
# b = 's'
# try:
#     c = a / b
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#     c = 0
# except TypeError:
#     print('TypeError')
#     c = 0
# else:
#     print(c)
# finally:
#     print('Finish')


# a, s, d = map(int, input().split())
# c = a + s + d
# print(c)


# try:
#     a = int(input())
#     s = int(input())
#     d = int(input())
#     s = a + s + d
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#
# except TypeError:
#     print('TypeError')
#
# except ValueError:
#     print('ValueError')
#
# finally:
#     print('Finish')
