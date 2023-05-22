def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """

    final = []
    a, b = 0, 0
    if not lst_a:
        return lst_b
    if not lst_b:
        return lst_a
    while a < len(lst_a) and b < len(lst_b):
        if lst_a[a] <= lst_b[b]:
            final.append(lst_a[a])
            a += 1
        else:
            final.append(lst_b[b])
            b += 1
    if a == len(lst_a) and b != len(lst_b):
        for i in range (b, len(lst_b)):
            final.append(lst_b[i])
    if b == len(lst_b) and a != len(lst_a):
        for i in range(a, len(lst_a)):
            final.append(lst_a[i])
    return final


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """

    return sorted(lst_a + lst_b)

