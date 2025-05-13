import segno
from PIL import Image

# URL you want to encode in the QR code
# url = "https://pybay.org/attending/schedule"
#output_filename = "pybay_2024_schedule_url.png"
# url = "https://pybay.org/attending/"
# output_filename = "pybay_2024_attending.png"

url = "https://pybay.org/sponsors/sponsor-us/"
output_filename = "pybay_2025_sponsors.png"


# Generate the QR code
qr = segno.make(url)

size = 600  # Example size

# Save the QR code as a PNG file with transparency
# Save the QR code as a PNG file
qr.save(output_filename, scale=10)  # Adjust the scale as needed

# Open the PNG file using Pillow
with Image.open(output_filename) as img:
    # Ensure the image has an alpha channel for transparency
    img = img.convert("RGBA")

    # Create a new image with the same size and a transparent background
    transparent_img = Image.new("RGBA", img.size, (0, 0, 0, 0))

    # Paste the QR code image onto the transparent background
    transparent_img.paste(img, (0, 0), img)

    # Resize the image if necessary
    new_size = (600, 600)  # Example size; adjust as needed
    transparent_img = transparent_img.resize(new_size, Image.Resampling.LANCZOS)

    # Save the resized image with a transparent background
    transparent_img.save(output_filename, "PNG")