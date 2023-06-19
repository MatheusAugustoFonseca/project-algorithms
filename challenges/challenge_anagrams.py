def sorting(string):
    if len(string) <= 1:
        return string

    pivot = string[len(string) // 2]
    left = [x for x in string if x < pivot]
    mid = [x for x in string if x == pivot]
    right = [x for x in string if x > pivot]

    return sorting(left) + mid + sorting(right)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # raise NotImplementedError
    if len(first_string) == 0 and len(second_string) == 0:
        return first_string, second_string, False

    lower_first = list(first_string.lower())
    lower_second = list(second_string.lower())

    sorted_first = "".join(sorting(lower_first))
    sorted_second = "".join(sorting(lower_second))

    return (sorted_first, sorted_second, sorted_first == sorted_second)


print(is_anagram("aan", "ana"))
print(is_anagram("pedra", "perdaaa"))
print(is_anagram("", ""))
