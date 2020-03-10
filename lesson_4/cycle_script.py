from itertools import cycle


def get_new_list(old_list, finish_number=10):

    i = 0
    new_list = []
    for j in cycle(old_list):
        new_list.append(j)

        if i == finish_number:
            break

        i += 1

    return new_list


