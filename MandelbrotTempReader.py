from PIL import Image
from twilio.rest import Client

def read(ocr, ocg, ocb, icr, icg, icb, mcr, mcg, mcb):
    Image.MAX_IMAGE_PIXELS = 32001 ** 2
    temp = Image.open("MandelbrotTemplate32001,5000,cor.png")
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
        #     send(str(i))
    output.save(f"NFTs/MandelbrotTemp32001({ocr},{ocg},{ocb}),({icr},{icg},{icb}),({mcr},{mcg},{mcb}),35,5000.png")
    # send("Image completed")


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


read(0, 0, 0, 255, 255, 255, 0, 0, 0)
