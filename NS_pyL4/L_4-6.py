from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        # repeat_list = [el for el in islice(cycle(my_list), num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"


print(unexpected(input("List starting at - "), input('from to - '), input('Number of repetition -')))
