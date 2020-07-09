import numpy as np


def generate_file(qty_strings):
    file = open('test_file.txt', 'w')
    for i in range(qty_strings):
        file.write(str(np.random.random()))
        file.write('\n')
    file.close()


qty_last_string = int(input('Enter qty strings in file: '))
generate_file(qty_last_string)