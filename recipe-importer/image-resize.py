import sys
from PIL import Image

def resize(path):
    im = Image.open(path)
    size = 612, 306
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im.save(path)

if len(sys.argv) != 2:
    print('Needs exactly 1 argument - the path to the image to resize')
else:
    print(resize(sys.argv[1]))