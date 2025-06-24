"""
https://pypi.org/project/qrcode/

"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer  # SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

pybay_year = "2025"
qr_labels_with_url = {"sponsors": "https://pybay.org/sponsors/sponsor-us/",
                      "speakers-call-for-proposals": "https://pybay.org/speaking/call-for-proposals/",
                      "tickets-on-sale": "https://pretix.eu/bapya/pybay-2025/",
                      "pybay-linkedin": "https://www.linkedin.com/company/18205092",
                      "pybay-fosstodon": "https://fosstodon.org/@pybay",
                      "pybay-bluesky": "https://bsky.app/profile/pybay.bsky.social",
                      "pybay-youtube": "https://www.youtube.com/c/SFPython",
                      "speakers_call_for_proposals":"https://pybay.org/speaking/call-for-proposals/",
                      "speakers_current":"https://pybay.org/speaking/current-speakers/",
                      "sponsors_current":"https://pybay.org/sponsors/our-sponsors/",
                      "sponsor_us":"https://pybay.org/sponsors/sponsor-us/",
                      "code_of_conduct":"https://pybay.org/code-of-conduct/",
                      "buy_tickets_pybay_page":"https://pybay.org/attending/",
                      "buy-tickets-pretix": "https://pretix.eu/bapya/pybay-2025/",
                      "about_our_team": "https://pybay.org/about/"
                      }

for qr_target in qr_labels_with_url:
    output_filename = f"pybay_{pybay_year}_{qr_target}_qr_code.png"

    qr_code_object = qrcode.QRCode(box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr_code_object.add_data(qr_labels_with_url[qr_target])

    image = qr_code_object.make_image(image_factory=StyledPilImage,
                                      color_mask=SolidFillColorMask(),
                                      module_drawer=GappedSquareModuleDrawer(size_ratio=.8))

    # CircleModuleDrawer
    image.save(output_filename)
    print(f"{output_filename} - image saved...")
