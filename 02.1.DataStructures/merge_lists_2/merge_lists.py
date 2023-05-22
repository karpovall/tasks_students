import heapq
import typing as tp


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    final = []
    heap: list[tuple[int, int, int]] = []
    for i in range(0, len(seq)):
        if seq[i]:
            heapq.heappush(heap, (seq[i][0], i, 0))
    while heap:
        a = heapq.heappop(heap)
        final.append(a[0])
        if a[2] != len(seq[a[1]]) - 1:
            heapq.heappush(heap, (seq[a[1]][a[2] + 1], a[1], a[2] + 1))
    return final
