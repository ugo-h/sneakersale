class Product(object):
    def __init__(self, name, oldPrice, specialPrice, link, img):
        self.name = name
        self.oldPrice = oldPrice
        self.specialPrice = specialPrice
        self.link = link
        self.img = img

    def __str__(self):
        return self.name
