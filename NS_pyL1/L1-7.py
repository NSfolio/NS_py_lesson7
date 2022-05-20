start = int(input('Введите сколько километров пробежали сегодня: '))
finish = int(input('Введите желаемое количество километров для пробежки каждый день: '))
i = 1
while start <= 100:
    print(i, '-й день:', start)
    i += 1
    start = start + (start * 0.1)
    if start >= finish:
        break

print('finish')
