def lab41():
    try:
        a = int(input("Введите число"))
        b = a % 3
    except ValueError:
        print("введено не число")
    if b == 0 and a != 0:
        print("Число делиться на 3")
    elif a == 0:
        print("введен 0")
    else:
        print("Число не делиться на 3")

def lab42():
    try:
        a = int(input("Введите число"))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен 0')
    except ValueError:
        print('Введено не число!')
    else:
        print('Результат деления 100 на введенное число: ', b)

def lab43():
    date = input('Впишите дату в виде 02.11.2022 ').split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Mагия')
    else:
        print('НЕ МАГИЯ')

def lab44():
    a = (input('Введите номер билета'))
    a1 = len(a)
    b = int(a1 / 2)
    sum1 = 0
    sum2 = 0

    if a1 % 2 == 0:
        for i in range(b):
            sum1 += int(a[i])
        for j in range(b, a1):
            sum2 += int(a[j])
        if sum1 == sum2:
            print('Ваш билет счастливый')
        else:
            print('Ваш билет обычный')
    else:
        print('Ваш билет нечетный')
    print(sum1, sum2)

lab41()
lab42()
lab43()
lab44()

