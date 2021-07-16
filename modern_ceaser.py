import string

ALPHABET = string.ascii_lowercase + '_{}'

def shuffle(plain, key):
    index = ALPHABET.index(key) % len(plain)
    return plain[index:] + plain[:index]

def encrypt(plain, key):
    plain = shuffle(plain, key)
    cipher = ''
    for c, i in enumerate(plain):
        index = (ALPHABET.index(i) + ALPHABET.index(key) * c) % len(ALPHABET)
        cipher += ALPHABET[index]
    return cipher

key = '*redacted*'
flag = '*redacted*'

assert len(key) == 1 and key in ALPHABET

enc = encrypt(flag, key)

print(f'{enc = }')

#enc = 'ueojddwlqyjtxvzbzqhyyetulan_wgfjg'
