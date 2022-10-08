from PIL import Image
import cmath

size = int(input("Enter the side length that you want for the template: ))
output = Image.new("RGB", (size, size // 2 + 1), (0, 0, 0))

def mandelbrot(z, c):
    return z ** 2 + c


pixels = output.load()
for i in range(-size // 2 + 1, size // 2 + 1):
    for j in range(-size // 2 + 1, 1):
        z = complex()
        c = complex(i / (size // 4), j / (size // 4))
        its = 1000
        for iters in range(1001):
            z = mandelbrot(z, c)
            if cmath.polar(z)[0] >= 2:
                break
            its -= 1
        if its == -1:
            its += 1
        try:
            pixels[size // 2 + i, size // 2 + j] = (0, its // 255, its % 255)
        except IndexError:
            print(size // 2 + i, size // 2 + j, i, j)
            quit()
    if i % 100 == 0:
        print(i)


output.save(f"MandelbrotTemplate{size}.png")
