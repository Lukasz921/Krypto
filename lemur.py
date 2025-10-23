from PIL import Image

flag = Image.open('flag.png')
lemur = Image.open('lemur.png')
pixels1 = flag.load()
pixels2 = lemur.load()

for x in range(flag.width):
    for y in range(flag.height):
        pixel1 = list(pixels1[x,y])
        pixel2 = list(pixels2[x,y])
        pixels1[x, y] = (
            pixel1[0] ^ pixel2[0],
            pixel1[1] ^ pixel2[1],
            pixel1[2] ^ pixel2[2]
        )
flag.save('output.png')