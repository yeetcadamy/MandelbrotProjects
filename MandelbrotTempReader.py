from PIL import Image

def read(ocr, ocg, ocb, icr, icg, icb, mcr, mcg, mcb, sze):
    Image.MAX_IMAGE_PIXELS = sze ** 2
    temp = Image.open(f"MandelbrotTemplate{sze}.png")
    print("Template loaded")
    output = Image.new("RGB", (32001, 32001), (0, 0, 0))
    tempPixels = temp.load()
    outPixels = output.load()
    for i in range(0, 32001):
        for j in range(0, 16001):
            curr = tempPixels[i, j][1] * 255 + tempPixels[i, j][2]
            if curr != 0:
                scalar = (curr / 5000) ** 35
                outPixels[i, j] = (int(scalar * ocr + (1 - scalar) * icr), int(scalar * ocg + (1 - scalar) * icg), int(scalar * ocb + (1 - scalar) * icb))
                outPixels[i, 32000 - j] = (int(scalar * ocr + (1 - scalar) * icr), int(scalar * ocg + (1 - scalar) * icg), int(scalar * ocb + (1 - scalar) * icb))
            else:
                outPixels[i, j] = (mcr, mcg, mcb)
                outPixels[i, 32000 - j] = (mcr, mcg, mcb)
        if i % 100 == 0:
            print(i)
        # if i % 10000 == 0:
    output.save(f"NFTs/MandelbrotTemp32001({ocr},{ocg},{ocb}),({icr},{icg},{icb}),({mcr},{mcg},{mcb}),35,5000.png")

    

read(input("Enter the red value of the pixels on the border of the image: "), input("Enter the green value of the pixels on the border of the image: "), input("Enter the blue value of the pixels on the border of the image: "), input("Enter the red value of the pixels on the border of the mandelbrot: "), input("Enter the green value of the pixels on the border of the mandelbrot: "), input("Enter the blue value of the pixels on the border of the mandelbrot: "), input("Enter the red value of the pixels inside the mandelbrot: "), input("Enter the green value of the pixels inside the mandelbrot: "), input("Enter the blue value of the pixels inside the mandelbrot: "), input("Enter the side length of the template file: "))
