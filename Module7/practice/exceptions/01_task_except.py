# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
f = True
while f:
    string = input("print data in format MxN to get count of M-Squares")
    try:
        if string.find('x') < 0:
            raise ImportError("В строке должен быть х")
        n, m = map(int, string.split('x'))

    except ValueError as e:
        print("M и N должны быть целыми числами")
    except ImportError as e:
        print(e)
    except Exception as e:
        print(e.__class__)
        print(e)
    else:
        count = n // m
        f = False

print(count)

