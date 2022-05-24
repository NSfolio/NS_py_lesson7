with open("text_2", "r", encoding='utf-8') as f_obj:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
              for count, line in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк - {len(useful)}.", sep="\n")
