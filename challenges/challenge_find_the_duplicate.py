def find_duplicate(nums):
    """Faça o código aqui."""
    # raise NotImplementedError

    try:
        nums.sort()

        for i in range(len(nums) - 1):
            verify_array(nums[i])

            if nums[i] == nums[i + 1]:
                return nums[i]

        return False

    except TypeError:
        return False


def verify_array(nums):
    if nums < 0:
        raise TypeError
    if not isinstance(nums, int):
        raise TypeError


# teste_one = []
# print(find_duplicate(teste_one))
