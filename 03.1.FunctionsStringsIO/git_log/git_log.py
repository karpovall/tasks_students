import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    a = inp.readline()
    while a:
        t = ""
        t += a[:7:]
        k = 0
        v = ""
        for i in range (len(a)):
            if k == 4:
                v += a[i]
            elif a[i] == '\t':
                k += 1
        t += '.'*(74-len(v))
        t += v
        out.write(t)
        a = inp.readline()



