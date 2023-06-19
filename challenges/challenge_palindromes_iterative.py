def is_palindrome_iterative(word):
    """Faça o código aqui."""
    # raise NotImplementedError
    if len(word) == 0:
        return False
    elif not isinstance(word, str):
        return False

    left_side = 0
    right_side = len(word) - 1

    while left_side < right_side:
        if word[left_side] != word[right_side]:
            return False
        left_side += 1
        right_side -= 1
    return True

    # if len(word) == 0:
    #     return False
    # elif not isinstance(word, str):
    #     return False
    # elif low_index >= high_index:
    #     return True
    # elif word[low_index] != word[high_index]:
    #     return False
    # return is_palindrome_recursive(word, low_index + 1, high_index - 1)
