import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_image_with_text(text, output_path, line_spacing_multiplier=1.5):
    # Define image parameters
    font_size = 20  # Desired font size for the system font
    noto_sans_path = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
    hack_font_path = "/usr/share/fonts/truetype/hack/Hack-Regular.ttf"

    # Attempt to load the Noto Sans font, then Hack font, or fall back to default
    try:
        font = ImageFont.truetype(noto_sans_path, font_size)
    except IOError:
        try:
            print(f"Could not load {noto_sans_path}, falling back to Hack font.")
            font = ImageFont.truetype(hack_font_path, font_size)
        except IOError:
            print(f"Could not load {hack_font_path}, falling back to default font.")
            font = ImageFont.load_default()

    margin = 5

    # Create a temporary image to calculate character size
    temp_image = Image.new('RGB', (1, 1), color='black')
    draw = ImageDraw.Draw(temp_image)

    # Calculate line height based on font metrics
    ascent, descent = font.getmetrics()
    line_height = ascent + descent

    # Wrap text to fit within a specified width
    wrap_width = len(text)  # Start with no wrapping
    lines = [text]
    while True:
        wrapped_text = textwrap.wrap(text, width=wrap_width)
        wrapped_width = max(draw.textbbox((0, 0), line, font=font)[2] - draw.textbbox((0, 0), line, font=font)[0] for line in wrapped_text)
        wrapped_height = len(wrapped_text) * line_height * line_spacing_multiplier

        # Check if text box fits within a 1:1 aspect ratio
        if wrapped_height > wrapped_width:
            break

        lines = wrapped_text
        wrap_width -= 1

    # Final text box dimensions
    max_width = max(draw.textbbox((0, 0), line, font=font)[2] - draw.textbbox((0, 0), line, font=font)[0] for line in lines) + 2 * margin
    total_height = len(lines) * line_height * line_spacing_multiplier + 2 * margin

    # Ensure the image is a square with minimum size that can fit the text
    dimension = int(max(max_width, total_height))

    # Create the actual image with appropriate dimensions
    image = Image.new('RGB', (dimension, dimension), color='black')
    draw = ImageDraw.Draw(image)

    # Calculate starting position
    current_y = margin

    # Draw each line of text left-justified with consistent line spacing
    for line in lines:
        draw.text((margin, current_y), line, font=font, fill="red")
        current_y += int(line_height * line_spacing_multiplier)

    # Save the image
    image.save(output_path)

def generate_unique_filename(base_path):
    counter = 1
    base, ext = os.path.splitext(base_path)
    while os.path.exists(base_path):
        base_path = f"{base}_{counter}{ext}"
        counter += 1
    return base_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 text_square_generator.py \"<text>\" [line_spacing_multiplier]")
        sys.exit(1)

    text = sys.argv[1]
    line_spacing_multiplier = float(sys.argv[2]) if len(sys.argv) > 2 else 1.5
    initial_output_path = os.path.expanduser("~/Pictures/text_image.png")
    output_path = generate_unique_filename(initial_output_path)

    create_image_with_text(text, output_path, line_spacing_multiplier)
    print(f"Image saved to {output_path}")
