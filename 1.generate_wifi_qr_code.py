"""
generate wifi qr code
"""
# Import module
import wifi_qrcode_generator as qr

# Use wifi_qrcode() to create a QR image
ssid="TBD"
password="TBD"
security_standard="WPA"
qrCode = qr.wifi_qrcode(ssid, False, security_standard, password)

# Display the qrImage
qrCode.show()

# Save the image as PNG file
qrCode.save("guest_wifi_qr.png")
