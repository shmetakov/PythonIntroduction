from itertools import count


def get_numbers_list(start_number, finish_number=10):
    new_list = []
    for number in count(start_number):
        new_list.append(number)

        if number == finish_number:
            break

    return new_list
