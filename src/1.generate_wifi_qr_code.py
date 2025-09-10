"""
generate wifi qr_code_object code
"""
# Import module
import wifi_qrcode_generator as qr
from project_utils import get_output_path

# Use wifi_qrcode() to create a QR image
output_filename = "ucsf-guest-wifi-qr-code.png"
ssid = "UCSFguest"
password = ""
security_standard = None

if security_standard is not None:
    qrCode = qr.wifi_qrcode(ssid, False, security_standard, password)
else:
    qrCode = qr.wifi_qrcode(ssid, False, password)

# Display the qrImage
qrCode.show()

# Build output path using shared helper (saves under project_root/output_qr_codes)
default_stem = f"{ssid}-wifi-qr-code"
output_path = get_output_path(output_filename, default_stem)
qrCode.save(str(output_path))
