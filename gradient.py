from PIL import Image
from random import randint

flag = '*redacted*'

for c, i in enumerate(flag):
    img = Image.new("RGB", (32, 32), (0, 0, (255 // len(flag)) * c))
    img.save(fr'flag\{i}_{randint(0, 999)}.png')
