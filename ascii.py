import sys
import math
from PIL import Image

# No idea why image rotates when opens but these transformations fix it
im = Image.open('pikachu.png').rotate(90).transpose(Image.FLIP_TOP_BOTTOM).convert('LA').resize((150, 150))
px = im.load()

width = im.size[0]
height = im.size[1]

chars = list(" .,:;irsXA253hMHGS#9B&@")
sections = len(chars)

for w in range(0, width):
    for h in range(0, height):
        c = px[w, h]

        v = c[0]
        a = c[1]

        if a == 255:
            l = int(round((255. - v) / 255 * sections)) - 1

            # print adds a random space and its annoying
            sys.stdout.write(chars[l])
        else:
            sys.stdout.write(' ')
    print ''
