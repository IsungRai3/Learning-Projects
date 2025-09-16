import qrcode

#User input
url = input("Enter the link : ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data("https://www.youtube.com/watch?v=fJ9rUzIMcZQ&list=RDKEvXoPFi28k&index=16")
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white" )
img.save('youtube_qr.png')