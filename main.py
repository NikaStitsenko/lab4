def 41():
    a = int(input("Введите число"))
    if a % 3 == 0:
        print("Число делиться на 3")
    else:
        print("Число не делиться на 3")

def 42():
    try:
        a = int(input("Введите число"))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен 0')
    except ValueError:
        print('Введено не число!')
    else:
        print('Результат деления 100 на введенное число: ', b)

def 43():
    a = input('Впишите дату в виде 02.11.2022 ').split('.')
    b = int(a[0])
    c = int(a[1])
    if b * c == int(a[2][2:]):
        print('Mагия')
    else:
        print('НЕ МАГИЯ')

def 44():
    a = int(input('Введите номер билета'))
    a1 = int(len(a))
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
