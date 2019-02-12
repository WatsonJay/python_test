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

def phot_exifRead(imageFilePath):
    try:
        imgfile = open(imageFilePath, 'rb')
        tags = exifread.process_file(imgfile)
        Exif_Date = tags["EXIF DateTimeOriginal"].printable
    except:
        return "ERROR:请确保照片包含经纬度等EXIF信息。"
    else:
        return Exif_Date

if __name__ == '__main__':
    phot_exifRead('G:/yw/DCIM/DCIM/100_CFV5/DSC_0001.JPG')
