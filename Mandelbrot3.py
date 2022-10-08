from PIL import Image
from PIL import ImageOps
import cmath
from progress.bar import Bar

results = []
size = int(input("What size do you want the picture to be? "))
if input('Print (r)ow by row or as a (p)rogress bar? ') == 'p':
    progress = True
else:
    progress = False


def mandelbrot(z, c):
    return z ** 2 + c

output = Image.new('RGB', (size, size))
pixels = output.load()
outcolr = int(input("Outside colour r: "))
outcolg = int(input("Outside colour g: "))
outcolb = int(input("Outside colour b: "))
incolr = int(input("Inside colour r: "))
incolg = int(input("Inside colour g: "))
incolb = int(input("Inside colour b: "))
mancolr = int(input("Mandelbrot colour r: "))
mancolg = int(input("Mandelbrot colour g: "))
mancolb = int(input("Mandelbrot colour b: "))
iterations = int(input("--> "))
scale = 255 / iterations
print("Creating Image")
if progress:
    bar = Bar('Rows completed', max=size // 2 + 1, suffix='%(percent).1f%%, ETA: %(eta)d, Running time: %(elapsed)d, Rows remaining: %(index)d/%(max)d')
for i in range(-size // 2 + 1, 1):
    for j in range(-size // 2 + 1, size // 2 + 1):
        z = complex()
        c = complex(j / (size // 4), i / (size // 4))
        for iteration in range(iterations + 1):
            if cmath.polar(z)[0] > 2:
                break
            z = mandelbrot(z, c)
        iteration = iterations - iteration
        scalar = (iteration / iterations) ** 35
        if iteration != 0:
            pixels[size // 2 - j, size // 2 - i] = (int(scalar * outcolr + (1 - scalar) * incolr), int(scalar * outcolg + (1 - scalar) * incolg), int(scalar * outcolb + (1 - scalar) * incolb))
            pixels[size // 2 - j, size // 2 + i] = (int(scalar * outcolr + (1 - scalar) * incolr), int(scalar * outcolg + (1 - scalar) * incolg), int(scalar * outcolb + (1 - scalar) * incolb))
        else:
            pixels[size // 2 - j, size // 2 - i] = (mancolr, mancolg, mancolb)
            pixels[size // 2 - j, size // 2 + i] = (mancolr, mancolg, mancolb)
    if progress:
        bar.next()
    else:
        print(i)
output = ImageOps.mirror(ImageOps.flip(output))
output = output.save(f"photos/Mandelbrot3,{size}x{size}colours({outcolr},{outcolg},{outcolb}),({incolr},{incolr},{incolr}),({mancolr},{mancolr},{mancolr}).png")
