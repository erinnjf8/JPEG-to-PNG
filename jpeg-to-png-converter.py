import os
from PIL import Image

def convert_jpeg_to_png(file_path):
    # Check if file is JPEG
    if not file_path.lower().endswith(('.jpg', '.jpeg')):
        print(f"File {file_path} is not a JPEG. Skipping.")
        return

    try:
        # Open JPEG File
        with Image.open(file_path) as img:
            # Convert to PNG
            png_path = os.path.splitext(file_path)[0] + '.png'
            # Save as PNG
            img.save(png_path, 'PNG')
            print(f"Converted {file_path} to {png_path}")
    except Exception as e:
        print(f"Error converting {file_path}: {str(e)}")
    finally:
        # Close File (this is handled automatically by the 'with' statement)
        pass

def main():
    print("JPEG to PNG Converter")
    file_path = input("Enter the path to the JPEG file: ")
    
    if os.path.exists(file_path):
        convert_jpeg_to_png(file_path)
    else:
        print("File not found. Please check the file path and try again.")

if __name__ == "__main__":
    main()
