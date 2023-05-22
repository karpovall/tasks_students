import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """

    result: list[tuple[str, int]] = []
    for key, value in dct.items():
        full_key = "{}.{}".format(prefix, key) if prefix else key
        if type(value) != dict:
            result.append((full_key, value))
        else:
            result.extend(traverse_dictionary_immutable(value, full_key))
    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """

    for key, value in dct.items():
        full_key = "{}.{}".format(prefix, key) if prefix else key
        if type(value) != dict:
            result.append((full_key, value))
        else:
            traverse_dictionary_mutable(value, result, full_key)


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """

    result: list[tuple[str, int]] = []
    st = [(dct, "")]
    while st:
        dct, prefix = st.pop()
        for key, value in dct.items():
            full_key = "{}.{}".format(prefix, key) if prefix else key
            if type(value) != dict:
                result.append((full_key, value))
            else:
                st.append((value, full_key))
    return result
