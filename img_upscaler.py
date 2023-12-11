import sys
from PIL import Image
import os


def scale(input, output, factor):
    source = Image.open(input)

    width, height = source.size
    new_width = int(width * factor)
    new_height = int(height * factor)

    scaled_image = source.resize((new_width, new_height), Image.NEAREST)
    scaled_image.save(output)


def upscale_folder_contents(input_folder, output_folder, img_type, factor):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith("." + img_type):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            scale(input_path, output_path, factor)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python img_upscaler.py <input_folder> <output_folder> <img_type> <factor>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    img_type = sys.argv[3]
    factor = float(sys.argv[4])

    upscale_folder_contents(input_folder, output_folder, img_type, factor)

    print("Done.")
