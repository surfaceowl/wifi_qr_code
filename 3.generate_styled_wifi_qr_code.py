"""
https://pypi.org/project/qrcode/

"""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

# add logo as background
# image_bg = Image.open('wifi_icon.svg')

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# add wifi data
# try to use segno to generate data, then pass it back to artistic from qrcode lib

# this attempt works; generates valid qr that attaches to guest network
from segno import helpers
ssid="TBD"
password="TBD"
security_standard="WPA"

wifi_config = helpers.make_wifi_data(ssid=ssid, password=password, security=security_standard, hidden=False)

qr.add_data(wifi_config)

image = qr.make_image(image_factory=StyledPilImage,
                      color_mask=SolidFillColorMask(),
                      module_drawer=GappedSquareModuleDrawer(size_ratio=.725))

# CircleModuleDrawer
image.save("guest_wifi_styled_gapped_square.png")
