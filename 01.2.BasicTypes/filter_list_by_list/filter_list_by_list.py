import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """

    final: list[int] = []
    a, b = 0, 0
    if not lst_b or not lst_a:
        return list[int] (lst_a)
    while a < len(lst_a):
        if lst_a[a] > lst_b[b]:
            if b < len(lst_b) - 1:
                b += 1
            else:
                final.extend(lst_a[a:])
                break
        if lst_a[a] == lst_b[b]:
            a += 1
            if a == len(lst_a):
                break
            if b < len(lst_b) - 1:
                b += 1
            else:
                final.extend(lst_a[a:])
                break
        if lst_a[a] < lst_b[b]:
            final.append(lst_a[a])
            a += 1
    return final
