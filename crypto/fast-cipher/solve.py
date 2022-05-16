M = 2**1024


def f(x):
    # this is a *fast* function
    return (
        4 * x**4 + 8 * x**8 + 7 * x**7 + 6 * x**6 + 3 * x**3 + 0x48763
    ) % M


def encrypt(pt, key):
    ct = []
    for c in pt:
        ct.append(c ^ (key & 0xFF))
        key = f(key)
    return bytes(ct)


if __name__ == "__main__":
    target = '6c0ec840f88d4cd7fcc6d5c6d1dafcc1cad7d0fcc2d1c6fcd6d0c6c7fccfcccfde'
    b = bytes.fromhex(target)
    for key in range(0, 256):
        plains = []
        for i in b:
            p = i ^ (key & 0xFF)
            plains.append(p)
            key = f(key)
            # print(i)
        print(bytes(plains))
