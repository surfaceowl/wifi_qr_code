import segno
from PIL import Image
input_file_original = "../images_input_art/baypiggies_logo_with_text_wide.png"

# Open the PNG file using Pillow
with Image.open(input_file_original) as img:
    # Ensure the image has an alpha channel for transparency
    img = img.convert("RGBA")

    # Create a new image with the same size and a transparent background
    transparent_img = Image.new("RGBA", img.size, (0, 0, 0, 0))

    # Paste the QR code image onto the transparent background
    transparent_img.paste(img, (0, 0), img)

    # Resize the image if necessary
    # new_size = (600, 600)  # Example size; adjust as needed
    # transparent_img = transparent_img.resize(new_size, Image.Resampling.LANCZOS)

    # Save the resized image with a transparent background
    transparent_img.save(input_file_original, "PNG")