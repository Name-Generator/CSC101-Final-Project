from typing import List, TextIO
import sys
import utility


def process_file(infile: TextIO, image_txt: TextIO) -> None:
    image_file = utility.get_image(infile)
    print('P3', file=image_txt)
    print('{} {}'.format(image_file.header.width, image_file.header.height), file=image_txt)
    print('{}'.format(image_file.header.max_color), file=image_txt)
    for pixel in image_file.pixels:
        red_value = int(pixel.red * 0.393 + pixel.green * 0.769 + pixel.blue * 0.189)
        if red_value > image_file.header.max_color:
            red_value = image_file.header.max_color
        green_value = int(pixel.red * 0.349 + pixel.green * 0.686 + pixel.blue * 0.168)
        if green_value > image_file.header.max_color:
            green_value = image_file.header.max_color
        blue_value = int(pixel.red * 0.272 + pixel.green * 0.534 + pixel.blue * 0.131)
        if blue_value > image_file.header.max_color:
            blue_value = image_file.header.max_color
        print('{} {} {}'.format(red_value, green_value, blue_value), file=image_txt)
# I formatted the file with the get image function, and then printed the header,
# then changed all of the color values for the pixels to be the shades specified, and then printed them into the file


def main(argv: List[str]) -> None:
    if len(sys.argv) > 1:
        try:
            print('opened')
            infile = open(sys.argv[1], 'r')
            image_txt = open('sepiafile.ppm', 'w')
            process_file(infile, image_txt)
            infile.close()
            image_txt.close()
        except (IndexError, FileNotFoundError) as e:
            print(e)
# I opened the file for reading, and then created and opened another file for writing, sent both to processing,
# and then closed them all, while checking for errors


if __name__ == '__main__':
    main(sys.argv)