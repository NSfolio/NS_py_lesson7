revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

print('выручка больше издержек', revenue - costs > 0)
print('издержки больше выручки', revenue - costs < 0)
