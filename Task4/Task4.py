# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num_quarter = input('Введите номер четверти от 1 до 4: ')
num_quarter = int(num_quarter)
if num_quarter == 1:
    print ('x > 0 and y > 0')
if num_quarter == 2:
    print ('x < 0 and y > 0')
if num_quarter == 3:
    print ('x < 0 and y < 0')
if num_quarter == 4:
    print ('x > 0 and y < 0')
if num_quarter < 1 or num_quarter > 4:
    print ('Введен неверный номер четверти')
