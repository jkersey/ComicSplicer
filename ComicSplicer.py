# OUTPUT SETTINGS
import os

DPI = 300
PAGE_WIDTH = 5.5
PAGE_HEIGHT = 7.25

# INPUT SETTINGS
CROP_LEFT = 0
CROP_RIGHT = 0
CROP_TOP = 0
CROP_BOTTOM = 0


class ComicSplicer:

    mypath = ""

    def __init__(self, mypath):
        self.mypath = mypath
        files = self.get_page_list()
        extra_pages = len(files) % 4
        if extra_pages:
            print(
                f"warning: number of pages is not divisible by 4, { extra_pages } blank page(s) will be added."
            )
        self.print_spliced_images(files)

    def print_spliced_images(self, files):

        num_pages = len(files)
        flip = False

        for i in range(0, int(num_pages / 2)):
            if flip:
                a, b = i, -(i + 1)
            else:
                a, b = -(i + 1), i
            print(files[a], files[b])
            flip = not flip

    def get_page_list(self):
        image_path = self.mypath + os.sep + "images"
        print(image_path)
        (_, _, filenames) = next(os.walk(image_path))
        return filenames


if __name__ == "__main__":
    comic_splicer = ComicSplicer(".")
