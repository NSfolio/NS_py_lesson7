revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

rent = (revenue / costs * 1)
print('рентабельность', rent, '%')

person = int(input('Введите численность сотрудников: '))
pers_pay = (revenue - costs) / person
print(pers_pay)
