# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

def is_wrong_year(num_year):
    return not (num_year % 4 != 0 or (num_year % 100 == 0 and num_year % 400 != 0))


while True:
    string = input('ВВедите номер месяца и номер года: ')
    try:
        month, year = map(int, (string.split()))
        if month <= 0 or year <= 0:
            raise ValueError("Номер должен быть положительным целым")
        if month > 12:
            raise ValueError("Номер месяца не должен превышать 12")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e.__class__)
    else:
        number_of_days_list = (31, 28 + is_wrong_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        number_of_days = number_of_days_list[month-1]
        print(number_of_days)
        break
