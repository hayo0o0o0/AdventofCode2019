def int_code(sequence):
    split_sequence = sequence.split(',')

    split_sequence[1] = '12'
    split_sequence[2] = '2'

    int_array = list(map(int, split_sequence))
    length_array = len(int_array)
    for x in range(0, length_array, 4):
        if x+3 <= length_array:
            process_opt_code(x, int_array)

    print(', '.join(str(x) for x in int_array))


def process_opt_code(position, array):
    parameter1 = array[position+1]
    parameter2 = array[position+2]
    result_parameter = array[position + 3]
    opt_code = array[position]
    if opt_code == 1:
        array[result_parameter] = array[parameter1] + array[parameter2]
    elif opt_code == 2:
        array[result_parameter] = array[parameter1] * array[parameter2]
    return


with open("input.txt") as fp:
    for line in fp:
        if line != "":
            int_code(line)
