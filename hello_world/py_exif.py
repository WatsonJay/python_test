from PIL import Image
from PIL.ExifTags import TAGS

def photoExif(imageFilePath):
    try:
        exifData = {}
        imgFile = Image.open(imageFilePath)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
                exifGPS = exifData['GPSinfo']
                if exifGPS:
                    print('[*]contains GPS MetaData,' + exifGPS)
    except:
        pass