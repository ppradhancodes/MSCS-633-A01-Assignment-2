import qrcode

# URL to encode
url = "https://www.bioxsystems.com/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (boxes)
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("biox_qr_code.png")

# Show the image
img.show()