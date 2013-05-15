import json
import os
import Image

def main():
    image_filename = os.path.join(os.path.dirname(__file__), 'image.jpg')
    handler = Image.open(image_filename)
    exif_tags = handler._getexif()
    exif_tags.pop(37500)
    print json.dumps(exif_tags, indent=4)

if __name__ == '__main__':
    main()
