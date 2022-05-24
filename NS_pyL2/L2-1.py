my_list = [24, "may", 2.22, True, False, None, [3, 4], ['home', 'cat'], tuple("строка"),
           (5, 6, 7.5, -3), {7: 'seven', 8: 'eight'}, {9, 8, 7, 6, 5, 4},
           ({'key': 'red', 'pen': 'blue', 'ball': 3}), ('mum', 'sun'), enumerate('home', 1),
           frozenset('map'), range(11), b'twelve', bytearray(b'thirteen'),
           zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")