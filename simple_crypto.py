from random import randint

flag = '*redacted*'
add = randint(0, 50)

cipher_text = [ord(i) + add for i in flag]

print(f'{cipher_text = }')

#cipher_text = [125, 131, 120, 126, 146, 138, 140, 135, 74, 137, 118, 74, 120, 145, 144, 118, 122, 137, 144, 135, 139, 71, 148]