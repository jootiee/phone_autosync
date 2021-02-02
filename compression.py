from PIL import Image

def compress(image):
    img = Image.open(image)
    img = img.resize(img.size, Image.ANTIALIAS)
    img.save(image)