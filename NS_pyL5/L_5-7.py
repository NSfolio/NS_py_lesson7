import json
with open('text_7.json', 'w', encoding='utf-8') as write_f, open('text_7', encoding="utf-8") as f_obj:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    f_up = [i for i in profit.values() if i > 0]
    result = [profit, {'average_profit': round(sum(f_up) / len(f_up))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
