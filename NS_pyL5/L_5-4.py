rus_dic = {"one": 'один', "two": 'два', "three": 'три', "four": 'четыре'}

with open('text_4ru', 'w', encoding='utf-8') as new_file:
    with open('text_4', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])
