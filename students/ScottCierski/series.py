import sys

def sum_series(nth_value, first_value = 0, second_value = 1):
    """This function returns the nth value of an integer sequence, wherein each integer is the sum of the previous two."""

    # Convert inputs to int
    nth_value = int(nth_value)
    first_value = int(first_value)
    second_value = int(second_value)

    #  Exit if nth_value is negative
    if nth_value < 0:
        print('Only positive values are allowed.')
        return None
    else:
        sum_list = [first_value, second_value]
        print sum_list
        for i in range(nth_value):
            # add current two values, and append sum to end of sum_list
            current_sum = first_value + second_value
            sum_list.append(current_sum)

            # Shift values
            first_value = second_value
            second_value = current_sum

    print '+++'
    print sum_list
    print sum_list[nth_value]
    return sum_list[nth_value]

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    print a, b, c
    sum_series(a, b, c)