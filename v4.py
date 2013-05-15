import json
import os
import Image
import ExifTags

def main():
    image_filename = os.path.join(os.path.dirname(__file__), 'image.jpg')
    handler = Image.open(image_filename)
    exif_tags = handler._getexif()
    decoded_exif = {ExifTags.TAGS.get(tag, tag): value
            for (tag, value) in exif_tags.iteritems()}
    decoded_exif.pop('MakerNote')

    print json.dumps(decoded_exif, indent=4)

if __name__ == '__main__':
    main()
