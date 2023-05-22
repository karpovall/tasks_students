def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """

    final = ""
    for i in range(len(message)):
        a = ord(message[i])
        if 96 < a < 123:
            a += n - 97
            a %= 26
            final += chr(a + 97)
        elif 64 < a < 91:
            a += n - 65
            a %= 26
            final += chr(a + 65)
        else:
            final += chr(a)
    return final
