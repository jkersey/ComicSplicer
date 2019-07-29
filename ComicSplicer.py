import getopt
import os
import sys

from PIL import Image

DPI = 300
PAGE_WIDTH = 5.5
PAGE_HEIGHT = 7.25

# INPUT SETTINGS
CROP_LEFT = 0
CROP_RIGHT = 0
CROP_TOP = 0
CROP_BOTTOM = 0


class ComicSplicer:

    input_dir = ""
    output_dir = ""

    page_spread = ""

    def __init__(self, input_dir, output_dir):

        if not output_dir:
            output_dir = input_dir + "_out"

        self.input_dir = input_dir
        self.output_dir = output_dir

        try:
            os.makedirs(self.output_dir + os.sep + "pages")
        except FileExistsError:
            pass

        self.page_spread = Image.new(
            "RGB", (int(PAGE_WIDTH * DPI * 2), int(PAGE_HEIGHT * DPI))
        )

        print(f"reading from {input_dir}, writing to {output_dir}")

        self.process_pages()
        self.process_cover()

    def process_pages(self):

        files = self.get_page_list()
        extra_pages = len(files) % 4
        if extra_pages:
            print("warning: number of pages is not divisible by 4")
            print("bailing out.")
            sys.exit(2)
        self.splice_all_pages(files)

    def process_cover(self):
        pass

    def splice_all_pages(self, files):

        num_pages = len(files)
        flip = False

        for i in range(0, int(num_pages / 2)):
            if flip:
                a, b = i, -(i + 1)
            else:
                a, b = -(i + 1), i
            self.splice_pages(i + 1, files[a], files[b])
            flip = not flip

    def get_page_list(self):
        page_path = self.input_dir + os.sep + "pages"
        filenames = []
        print(page_path)
        for _, _, filenames in os.walk(page_path):
            filenames = [f for f in filenames if not f[0] == "."]
        print(f"got { len(filenames) } pages.")
        return filenames

    def splice_pages(self, spread_number, left_page, right_page):
        left_image = Image.open(self.input_dir + os.sep + "pages" + os.sep + left_page)
        right_image = Image.open(
            self.input_dir + os.sep + "pages" + os.sep + right_page
        )

        left_image = left_image.resize(
            (int(PAGE_WIDTH * DPI), int(PAGE_HEIGHT * DPI)), resample=Image.BILINEAR
        )
        right_image = right_image.resize(
            (int(PAGE_WIDTH * DPI), int(PAGE_HEIGHT * DPI)), resample=Image.BILINEAR
        )

        self.page_spread.paste(left_image, (0, 0))
        self.page_spread.paste(right_image, (int(PAGE_WIDTH * DPI), 0))

        spread_str = str(spread_number).zfill(3)

        self.page_spread.save(
            self.output_dir
            + os.sep
            + "pages"
            + os.sep
            + "spread_"
            + spread_str
            + left_page
        )
        print(f"saving spread { spread_str } ( { left_page }, { right_page } )")


def main(argv):
    input_dir = ""
    output_dir = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["idir=", "odir="])
    except getopt.GetoptError:
        print("ComicSplicer.py -i <input_dir> -o <output_dir>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -i <input_dir> -o <output_dir>")
            sys.exit()
        elif opt in ("-i", "--idir"):
            input_dir = arg
        elif opt in ("-o", "--odir"):
            output_dir = arg
    print("Input directory is ", input_dir)
    print("Output file is ", output_dir)

    ComicSplicer(input_dir, output_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
