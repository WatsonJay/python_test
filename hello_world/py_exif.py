from PIL import Image
from PIL.ExifTags import TAGS
import exifread
import re

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
    except Exception as e:
        print(e)

def 

if __name__ == '__main__':
    photoExif("G:/DICM/班级/IMG_20140315_090402.jpg")