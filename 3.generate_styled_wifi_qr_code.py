"""
https://pypi.org/project/qrcode/

"""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

# add logo as background
# image_bg = Image.open('wifi_icon.svg')

qr = qrcode.QRCode(box_size=100, error_correction=qrcode.constants.ERROR_CORRECT_H)

# add wifi data
# try to use segno to generate data, then pass it back to artistic from qrcode lib

# this attempt works; generates valid qr_code_object that attaches to guest network
from segno import helpers
ssid="UCSFguest"
password=""
# security_standard="WPA"
security_standard=None

if security_standard is not None:
    wifi_config = helpers.make_wifi_data(ssid=ssid, password=password, security=security_standard, hidden=False)
else:
    wifi_config = helpers.make_wifi_data(ssid=ssid, password=password,  hidden=False)
qr.add_data(wifi_config)

image = qr.make_image(image_factory=StyledPilImage,
                      color_mask=SolidFillColorMask(),
                      module_drawer=GappedSquareModuleDrawer(size_ratio=.725))

# CircleModuleDrawer
image.save("UCSFguest_wifi_styled_gapped_square.png")

image_square = qr.make_image(image_factory=StyledPilImage,
                      color_mask=SolidFillColorMask(),
                      module_drawer=SquareModuleDrawer(size_ratio=.725))

image_square.save("UCSFguest_wifi_styled_square_square.png")
