import os
import Image

def main():
    image_filename = os.path.join(os.path.dirname(__file__), 'image.jpg')
    handler = Image.open(image_filename)
    print handler._getexif()

if __name__ == '__main__':
    main()
