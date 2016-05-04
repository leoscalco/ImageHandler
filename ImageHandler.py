from PIL import Image as pil_im

class ImageHandler:

    def __init__(self, range):
        self.range = 80
        self.black = [0, 0, 0, 255]
        self.white = [255, 255, 255, 255]
        self.trasparent = (255, 255, 255, 0) # not vector

    def remove_background(self, im, color):
        # http://stackoverflow.com/questions/21217384/remove-background-colour-from-image-using-python-pil
        # http://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
        self.im = im.convert('RGBA')
        self.data = im.getdata()

        newData = []
        for item in self.data:
            if self.is_in_range(item[0], color[0], self.range) and self.is_in_range(item[1], color[1], self.range) and self.is_in_range(item[2], color[2], self.range):
                newData.append(self.trasparent)
            else:
                newData.append(item)
        self.im.putdata(newData)
        self.save_image(self.im, "transparent.png", "PNG")

    def put_background(self, background):
        # http://stackoverflow.com/questions/13637028/adding-a-background-image-in-python
        # http://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python
        background = background.convert('RGBA')
        im_w, im_h = self.im.size
        bg_w, bg_h = background.size
        offset = ((bg_w - im_w) / 2, (bg_h - im_h) / 2)
        # http://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil
        background.paste(self.im, offset, self.im)
        self.save_image(background, "implusback.png", "PNG")



    def is_in_range(self, item, val, tolerance):
        if item > (val - tolerance) and item < (val + tolerance):
            return True
        else:
            return False

    def save_image(self, i, name, type):
        print type
        i.save("images/outputs/"+name, type)


ih = ImageHandler(80)

im = pil_im.open("images/inputs/fundoVerde.jpg")
# color = [(90, 110), (160, 185), (105, 130)] # valor original
color = [1, 255, 2]
ih.remove_background(im, color)
back_im = pil_im.open("images/inputs/background.jpg")
ih.put_background(back_im)