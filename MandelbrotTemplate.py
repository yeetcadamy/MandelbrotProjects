from PIL import Image
import cmath
from twilio.rest import Client

size = int(input())
output = Image.new("RGB", (size, size // 2 + 1), (0, 0, 0))

def mandelbrot(z, c):
    return z ** 2 + c


def send(val):
    account_sid = 'AC34e7ad9e631e1e388d1394ac67696500'
    auth_token = '40948bc6168047618a87cfaf1fcbbb3f'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f'{val}',
        from_='+447723141017',
        to='+447557022993'
    )
    print(message.sid)


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
    # if i % 10000 == 0:
        # send(str(i))


output.save(f"MandelbrotTemplate{size}.png")
