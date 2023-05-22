import heapq
import typing as tp


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    heap: list[tuple[int, int]] = []
    for i in range(len(input_streams)):
        st = input_streams[i].readline().strip()
        if st:
            heapq.heappush(heap, (int(st), i))
    if not heap:
        output_stream.write(b'\n')
    while heap:
        a = heapq.heappop(heap)
        output_stream.write(b'%d\n' % a[0])
        st = input_streams[a[1]].readline().strip()
        if st:
            heapq.heappush(heap, (int(st), a[1]))


