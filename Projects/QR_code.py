import qrcode

data = input("Enter the data: ").strip()
filename = input("Enter the file name: ").strip()

# Create a QRCode object
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)  
qr.make()

# Generate image
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code saved as {filename}")
