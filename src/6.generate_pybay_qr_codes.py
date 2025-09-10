"""
Generates three styled PNGs for each filename:url target listed:
- Black on white background
- Black on transparent background
- White on transparent background

All outputs enforce a consistent final image size and consistent pixel margin (space) between the
QR code and the image border across all outputs.

https://pypi.org/project/qrcode/

"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer  # SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from project_utils import get_output_path
from PIL import Image

# Tunable layout parameters to keep all images visually consistent
FINAL_SIZE = 1200  # final square canvas size in pixels (width == height)
MARGIN_PX = 100    # desired pixel margin from QR code to canvas border on all sides
MODULE_DRAWER = GappedSquareModuleDrawer(size_ratio=.8)
ERROR_LEVEL = qrcode.constants.ERROR_CORRECT_L

# INPUT Current year and desired filename/URL targets as key:value pairs in the dictionary below (sort alpha please)
PYBAY_YEAR = "2025"
qr_labels_with_url = {
    "meetup-bapyacfp-submit-talk-proposal": "https://bit.ly/bapyacfp",
    "meetup-baypiggies": "https://www.meetup.com/baypiggies/",
    "meetup-pyninsula": "https://www.meetup.com/pyninsula-python-peninsula-meetup/",
    "meetup-sfpython": "https://www.meetup.com/sfpython/",
    "pretix-buy-tickets": "https://pretix.eu/bapya/pybay-2025/",
    "pycon-2025-youtube": "https://www.youtube.com/watch?v=flnVc2Ke-bw&list=PL2Uw4_HvXqvb98mQjN0-rYQjdDxJ_hcrs",
    "pycon-movie-documentary": "https://www.youtube.com/watch?v=pqBqdNIPrbo",
    "pybay-bluesky": "https://bsky.app/profile/pybay.bsky.social",
    "pybay-buy-tickets-page": "https://pybay.org/attending/",
    "pybay-facebook": "https://www.facebook.com/PyBayConf/",
    "pybay-fosstodon": "https://fosstodon.org/@pybay",
    "pybay-instagram": "https://www.instagram.com/py_bay/",
    "pybay-linkedin": "https://www.linkedin.com/company/18205092",
    "pybay-org-main-landing-page": "https://pybay.org",
    "pybay-org-about-our-team-page": "https://pybay.org/about/",
    "pybay-org-code-of-conduct": "https://pybay.org/code-of-conduct/",
    "pybay-org-sponsor-us": "https://pybay.org/sponsors/sponsor-us/",
    "pybay-org-sponsors-current": "https://pybay.org/sponsors/our-sponsors/",
    "pybay-twitter-x": "https://x.com/py_bay",
    "pybay-youtube": "https://www.youtube.com/c/SFPython",
    "pybay-org-speakers-call-for-proposals": "https://pybay.org/speaking/call-for-proposals/",
    "speakers-current": "https://pybay.org/speaking/current-speakers/",
}

# Precompute the inner target area for the QR code itself (excluding margin)
INNER_TARGET = max(1, FINAL_SIZE - 2 * MARGIN_PX)

# Determine a fixed QR version that can encode the largest payload among all URLs
max_version = 1
for _label, _url in qr_labels_with_url.items():
    tmp_qr = qrcode.QRCode(box_size=1, border=0, error_correction=ERROR_LEVEL)
    tmp_qr.add_data(_url)
    tmp_qr.make(fit=True)
    if hasattr(tmp_qr, "version") and tmp_qr.version is not None:
        max_version = max(max_version, tmp_qr.version)

# With fixed version, all codes share the same module grid size
modules_for_max = 17 + 4 * max_version
BOX_SIZE = max(1, INNER_TARGET // modules_for_max)

for qr_target, url in qr_labels_with_url.items():
    output_filename = f"pybay_{PYBAY_YEAR}_{qr_target}_qr_code.png"

    # Build QR with fixed version and no library border for consistent module and finder sizes
    qr_code_object = qrcode.QRCode(
        version=max_version,
        box_size=BOX_SIZE,
        border=0,
        error_correction=ERROR_LEVEL,
    )
    qr_code_object.add_data(url)
    # Enforce the fixed version without auto-resizing
    qr_code_object.make(fit=False)

    # Render base images at exact integer-scaled module size, with no quiet zone
    # This keeps module edges crisp (no resampling of the code itself)
    image_white_inner_wrapped = qr_code_object.make_image(
        image_factory=StyledPilImage,
        color_mask=SolidFillColorMask(front_color=(0, 0, 0), back_color=(255, 255, 255)),
        module_drawer=MODULE_DRAWER,
    )
    image_transparent_inner_wrapped = qr_code_object.make_image(
        image_factory=StyledPilImage,
        color_mask=SolidFillColorMask(front_color=(0, 0, 0, 255), back_color=(255, 255, 255, 0)),
        module_drawer=MODULE_DRAWER,
    )
    image_white_on_transparent_inner_wrapped = qr_code_object.make_image(
        image_factory=StyledPilImage,
        color_mask=SolidFillColorMask(front_color=(255, 255, 255, 255), back_color=(255, 255, 255, 0)),
        module_drawer=MODULE_DRAWER,
    )

    # Unwrap to actual PIL.Image.Image objects for Pillow operations
    image_white_inner = (
        image_white_inner_wrapped.get_image() if hasattr(image_white_inner_wrapped, "get_image") else image_white_inner_wrapped
    )
    image_transparent_inner = (
        image_transparent_inner_wrapped.get_image() if hasattr(image_transparent_inner_wrapped, "get_image") else image_transparent_inner_wrapped
    )
    image_white_on_transparent_inner = (
        image_white_on_transparent_inner_wrapped.get_image() if hasattr(image_white_on_transparent_inner_wrapped, "get_image") else image_white_on_transparent_inner_wrapped
    )

    # Ensure RGBA for transparent compositing
    if getattr(image_transparent_inner, "mode", None) != "RGBA":
        image_transparent_inner = image_transparent_inner.convert("RGBA")
    if getattr(image_white_on_transparent_inner, "mode", None) != "RGBA":
        image_white_on_transparent_inner = image_white_on_transparent_inner.convert("RGBA")

    # Compute actual inner size (modules * box_size)
    inner_w, inner_h = image_white_inner.size

    # Create final canvases
    canvas_white = Image.new("RGB", (FINAL_SIZE, FINAL_SIZE), (255, 255, 255))
    canvas_transparent = Image.new("RGBA", (FINAL_SIZE, FINAL_SIZE), (255, 255, 255, 0))
    canvas_white_on_transparent = Image.new("RGBA", (FINAL_SIZE, FINAL_SIZE), (255, 255, 255, 0))

    # Center with the requested minimum margins; if inner is smaller than INNER_TARGET due to
    # integer box sizing, distribute the extra pixels evenly to keep perfect centering.
    extra_w = FINAL_SIZE - (inner_w + 2 * MARGIN_PX)
    extra_h = FINAL_SIZE - (inner_h + 2 * MARGIN_PX)
    offset_x = MARGIN_PX + max(0, extra_w // 2)
    offset_y = MARGIN_PX + max(0, extra_h // 2)

    # Paste onto canvases; for transparent, use the inner image as mask to preserve alpha
    canvas_white.paste(image_white_inner, (offset_x, offset_y))
    canvas_transparent.paste(image_transparent_inner, (offset_x, offset_y), image_transparent_inner)
    canvas_white_on_transparent.paste(image_white_on_transparent_inner, (offset_x, offset_y), image_white_on_transparent_inner)

    # Save outputs with existing naming conventions
    white_path = get_output_path(output_filename, output_filename.rsplit('.', 1)[0])
    canvas_white.save(str(white_path))
    print(f"{white_path.name} - white background image saved...")

    transparent_default_stem = white_path.stem + "-transparent"
    transparent_path = get_output_path(None, transparent_default_stem)
    canvas_transparent.save(str(transparent_path))
    print(f"{transparent_path.name} - transparent background image saved...")

    transparent_white_default_stem = white_path.stem + "-transparent-white"
    transparent_white_path = get_output_path(None, transparent_white_default_stem)
    canvas_white_on_transparent.save(str(transparent_white_path))
    print(f"{transparent_white_path.name} - white QR on transparent background image saved...")
