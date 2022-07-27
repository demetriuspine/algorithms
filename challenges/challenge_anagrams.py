def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    lowered_first_string = first_string.lower()
    lowered_second_string = second_string.lower()

    # https://www.delftstack.com/howto/python/python-string-to-list/
    first_string_list = list(lowered_first_string)

    # https://www.delftstack.com/howto/python/python-string-to-list/
    second_string_list = list(lowered_second_string)

    for letter in first_string_list:
        if letter in second_string_list:
            # https://delftstack.com/howto/python/delete-element-from-list-by-value/
            second_string_list.remove(letter)
        else:
            return False

    if len(second_string_list) == 0:
        return True

    else:
        return False
