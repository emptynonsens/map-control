import pandas as pd

def list_from_word(word, lenght_of_list):
    new_list = []
    for i in range (0, lenght_of_list):
        new_list.append(f'{word} nr {i}')
    return new_list

popup_list = list_from_word('Popup', 10)
tooltip_list = list_from_word('Tooltip', 10)

data = {'Coordinates':
                [
                [52.713687, 14.173617],
                [51.158228, 15.615368],
                [52.592207, 11.532914],
                [52.474376, 13.439628],
                [51.083143, 17.002753],
                [51.912275, 8.970807],
                [53.443154, 9.939069],
                [49.771696, 8.513013],
                [47.186006, 8.142508],
                [52.160384, 20.962613]
                ],
           'Popup':
                popup_list,
           'Tooltip':
                tooltip_list}

                