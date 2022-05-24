print('Введите данные для записи в файл \nДля завершения оставьте пустую строку\n...')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != "":
        my_file.write(f"{line}\n")
