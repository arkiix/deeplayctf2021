from random import seed, randint

flag = '*redacted*'
ct = []

for i in flag:
    seed(randint(0, 100000))
    rands = []
    for _ in range(5):
        rands.append(randint(0, 1000))
    ct.append(rands[4] ^ ord(i))
    rands.remove(rands[4])
    print(rands)

print(f'{ct = }')
