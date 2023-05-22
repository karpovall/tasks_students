import typing as tp


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """

    a, b, c, d = 0, 0, 0, 0
    a = text.count("\n")
    x = 0
    if text:
        if text[0] != ' ' and text[0] != '\n':
            b = 1
    for i in range(len(text) - 1):
        if text[i + 1] != ' ' and text[i + 1] != '\n' and (text[i] == ' ' or text[i] == '\n'):
            b += 1
    c = len(text)
    for i in range(len(text)):
        if text[i] != '\n':
            x += 1
        else:
            x = 0
        if x > d:
            d = x
    t: dict[str, int] = {}
    if flags is None or 'm' in flags or not flags:
        t['chars'] = c
    if flags is None or 'l' in flags or not flags:
        t['lines'] = a
    if flags is None or 'L' in flags or not flags:
        t['longest_line'] = d
    if flags is None or 'w' in flags or not flags:
        t['words'] = b
    return t

