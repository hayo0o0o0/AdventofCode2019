def int_code(sequence):
    for i in range(99):
        for y in range(99):
            split_sequence = sequence.split(',')

            int_array = list(map(int, split_sequence))
            int_array[1] = i
            int_array[2] = y
            length_array = len(int_array)-1
            for x in range(0, length_array, 4):
                if x + 3 <= length_array:
                    process_opt_code(x, int_array)
                if int_array[0] == 19690720:
                    print("The inputs needed to obtain the output of 19690720 are " + str(i) + " and " + str(y))
                    break


def process_opt_code(position, array):
    opt_code = array[position]
    parameter1 = array[position+1]
    parameter2 = array[position+2]
    result_parameter = array[position + 3]

    if opt_code == 1:
        array[result_parameter] = array[parameter1] + array[parameter2]
    elif opt_code == 2:
        array[result_parameter] = array[parameter1] * array[parameter2]
    return


with open("input.txt") as fp:
    for line in fp:
        if line != "":
            int_code(line)
