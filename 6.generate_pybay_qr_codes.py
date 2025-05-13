"""
https://pypi.org/project/qrcode/

"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
import os

# add logo as background
# image_bg = Image.open('wifi_icon.svg')

pybay_year = "2025"
leads_to_recruit = {"sponsors": "https://pybay.org/sponsors/sponsor-us/",
        "speakers-call-for-proposals": "https://pybay.org/speaking/call-for-proposals/"}


for lead_type in leads_to_recruit:
    filename = f"pybay_{pybay_year}_{lead_type}_qr_code.png"

    qr = qrcode.QRCode(box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(leads_to_recruit[lead_type])

    image = qr.make_image(image_factory=StyledPilImage,
                          color_mask=SolidFillColorMask(),
                          module_drawer=GappedSquareModuleDrawer(size_ratio=.8))

    # CircleModuleDrawer
    image.save(filename)
    print(f"{filename} - image saved...")
