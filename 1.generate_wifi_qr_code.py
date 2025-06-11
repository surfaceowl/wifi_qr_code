"""
generate wifi qr_code_object code
"""
# Import module
import wifi_qrcode_generator as qr

# Use wifi_qrcode() to create a QR image
ssid="UCSFguest"
password=""
security_standard=None

if security_standard is not None:
    qrCode = qr.wifi_qrcode(ssid, False, security_standard, password)
else:
    qrCode = qr.wifi_qrcode(ssid, False, password)

# Display the qrImage
qrCode.show()

# Save the image as PNG file
qrCode.save("ucsf_guest_wifi_qr.png")
