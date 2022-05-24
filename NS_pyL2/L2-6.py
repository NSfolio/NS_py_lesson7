goods = []
features = {'наименование товара': '', 'цена': '', 'кол-во': '', 'ед.измерения': ''}
analytics = {'наименование товара': [], 'цена': [], 'кол-во': [], 'ед.измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')
        f_copy[f] = int(pro) if f in 'цена количество' and pro.isdigit() else pro
        analytics[f].append(f_copy[f])
    goods.append((num, f_copy))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\nТекущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)