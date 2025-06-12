import qrcode

img = qrcode.make("https://techstarter.de/wp-content/uploads/2024/03/image-student.jpg")

img.save("techstarter.png")