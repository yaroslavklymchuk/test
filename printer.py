def print_last(qty_strings):
    file = open('test_file.txt', 'r')
    last_digits = file.readlines()[-qty_strings:]
    for digit in last_digits:
        print(digit.strip())


qty_strings_to_print = int(input('Enter a qty rows to print from file: '))
print_last(qty_strings_to_print)