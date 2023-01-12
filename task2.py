# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
 
n = int(input("Введите число: "))
spisok = [n]
 
def nature(spisok):
    fl = 0
    for i in range(spisok[-1] // 2, 1, -1):
        if spisok[len(spisok)-1] % i == 0:
            spisok.append(i)
            spisok[-2] = spisok[-2] // i              
            fl += 1
    if fl != 0:
        nature(spisok)
 
nature(spisok)
    
print(spisok)
 