# https://i.pinimg.com/236x/08/42/9a/08429a51d6feb998525ac0f42b3c1c4d.jpg
import qrcode
def makeqrcode(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")


makeqrcode("https://i.pinimg.com/236x/08/42/9a/08429a51d6feb998525ac0f42b3c1c4d.jpg")