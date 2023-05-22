def mount(a: list[int]):

    if not a:
        return False
    k, max1 = False, a[0]
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            k = True
        if a[i] < a[i+1] and k:
            return False
    if max(a) != a[0] and k:
        return True
    return False
