num = list(input("Введите число: "))

for i in range(1, len(num), 2):
    num[i - 1], num[i] = num[i], num[i - 1]

print(num)

