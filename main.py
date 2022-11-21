import os,sys,time,base64
from math import log10





def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

def encrypt(msg: str, key: str) -> bytes:
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 325))
    return base64.b85encode(str(''.join(encryped)).encode("utf_32_be"))


def decrypt(encrypted: bytes, key: str) -> str:
    encrypted = base64.b85decode(encrypted).decode('utf_32_be')
    msg = []
    for i, c in enumerate(encrypted):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 325))
    return ''.join(msg)


def main():
    if len(sys.argv) < 2:
        main2()
        exit()
    key = sys.argv[3]
    plain = sys.argv[2]
    print(key)
    print(plain)
    if sys.argv[1] == "enc":
        x=encrypt(plain, key)
        print(x)
        exit()
    elif sys.argv[1] == "dec":
        y=decrypt(plain, key)
        print(y)
        exit()


def main2():
    key="main3212"
    plain="manoxi3"
    x=encrypt(plain, key)
    y=decrypt(x, key)
    z=y==plain
    print(x)
    print(y)
    print(z)



if __name__ == "__main__":
    main()
