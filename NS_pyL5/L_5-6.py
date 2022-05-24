with open('text_6', 'r', encoding='utf-8') as text_file:
    for s in text_file:
        new_str = "".join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')
