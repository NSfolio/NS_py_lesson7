def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода данных: \nx должен быть больше 0\ny должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения x в степень = {round(result, 6)}'
    except ValueError:
        return "Программа работает только с числами."

number1 = input('Введите действительное положительное число, x = ')
number2 = input('Введите целое отрицательное число, y = ')

print(my_func2(number1, number2))
