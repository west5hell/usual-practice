import argparse
import os
from PIL import Image


def resize_image(input_path, output_path, width, height):
    """Resize an image to specified dimensions"""
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height), Image.LANCZOS)
            resized_img.save(output_path)
            print(f"Image resized to {width}x{height} and saved as {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")


def main():
    parser = argparse.ArgumentParser(description="Image clipper - resize images")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("width", type=int, help="New width in pixels")
    parser.add_argument("height", type=int, help="New height in pixels")
    parser.add_argument("-o", "--output", help="Output file path (optional)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found")
        return
    
    if args.output:
        output_path = args.output
    else:
        base, ext = os.path.splitext(args.input)
        output_path = f"{base}_resized_{args.width}x{args.height}{ext}"
    
    resize_image(args.input, output_path, args.width, args.height)


if __name__ == "__main__":
    main()
