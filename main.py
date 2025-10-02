class TooBigNumber(Exception):
    pass

try:
    a = int(input())
    b = int(input())
    if a > 100000 or b > 100000:
        raise TooBigNumber
    print(a / b)
except ValueError:
    print('Вводите только числа!')
except TooBigNumber:
    print('Вы ввели сильно большое число')
except ZeroDivisionError:
    print('Делить на 0 нельзя!')
except Exception:
    print('Возникла какая-то ошибка!')
finally:
    print('Хорошего дня!')