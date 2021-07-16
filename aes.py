from Crypto.Cipher import AES
from random import choice
import string

BLOCK_SIZE = 16

def pad(plain):
    return plain + '0' * (BLOCK_SIZE - (len(plain) % BLOCK_SIZE))

def generate_key():
    dictionary = string.ascii_lowercase[23:]
    key = [choice(dictionary) for _ in range(16)]
    return ''.join(key).encode()

def encode(plain, key):
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(pad(plain).encode())
    return cipher

key = generate_key()
flag = '*redacted*'
cipher = encode(flag, key)

print(f'{cipher = }')

#cipher = b'ZD\x8de1\x87\xad\xac\xf4\x93\x85\xe7\x1f\xbe\x0c\xd3_\xd9\x94\xd4\xdb\xf3\xc8\x1d\xb9[\xd8\x8a\xfb\x13?\x19'
