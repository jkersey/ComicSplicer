# ComicSplicer

A basic layout tool that takes a directory of comic pages and outputs the spreads necessary for printing.

A 16 page comic printed on a home printer would need images built from pages:

* [16, 1]
* [2, 15]
* [14, 3]
* [4, 13]
* [12, 5]
* [6, 11]
* [10, 7]
* [8, 9] (center spread)

Which then would be printed double-sized and saddle stitched.

This is an alternative to lots of copying/pasting in an image editor.

## Usage

(Note, uses Python 3.6 because I find f-strings handy)

> python ComicSplicer.py -i < input directory > -o < output_directory > 

Reads files in alphanumeric order from <input_directory>/pages/ and writes to <output_directory>/pages/


## Future Improvements

* Separately reading from a "cover" directory for front/back/front interior/back interior files
* Outputting a PDF for digital distribution
* Configuration files for standard comic sizes
* Cropping the original files before pasting into the spread

