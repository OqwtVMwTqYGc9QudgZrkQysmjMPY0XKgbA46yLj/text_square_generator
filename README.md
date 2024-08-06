# Text Square Generator

A Python script to generate square images containing a specified text. The script automatically wraps the text and adjusts the image dimensions to ensure the text fits within a square aspect ratio.

## Features

- Generates square images with specified text
- Automatically wraps text to fit within the image
- Adjustable line spacing
- Supports custom fonts, with fallback to default fonts if necessary

## Requirements

- Python 3.x
- PIL (Pillow)
- Fonts: Noto Sans, Hack (ensure these are installed or modify the script to use available fonts)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/<your-username>/text_square_generator.git
    cd text_square_generator
    ```

2. Install the required packages:

    ```sh
    pip install Pillow
    ```

## Usage

Run the script with the text you want to include in the image:

    ```sh
    python3 text_square_generator.py "<your_text>" [line_spacing_multiplier]
    ```

- `<your_text>`: The text you want to include in the image.
- `[line_spacing_multiplier]` (optional): A multiplier for line spacing (default is 1.5).

### Example

    ```sh
    python3 text_square_generator.py "Hello, World!" 1.2
    ```

This command generates an image with the text "Hello, World!" and a line spacing multiplier of 1.2. The image is saved to the `~/Pictures/` directory with a unique filename.

## Script Details

The script, `text_square_generator.py`, performs the following steps:

1. Loads the specified text and font.
2. Wraps the text to fit within a square aspect ratio.
3. Creates an image with the required dimensions.
4. Draws the text on the image.
5. Saves the image to the specified output path.

### Functions

- `create_image_with_text(text, output_path, line_spacing_multiplier=1.5)`: Generates an image with the specified text.
- `generate_unique_filename(base_path)`: Generates a unique filename to avoid overwriting existing files.

### Fonts

The script attempts to use the Noto Sans font, falling back to the Hack font, and finally to the default system font if the others are unavailable. You can customize the font paths in the script as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or feedback, please contact [your-email@example.com].
