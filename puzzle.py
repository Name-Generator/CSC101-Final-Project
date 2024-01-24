from typing import List, TextIO
import sys
import utility


def process_file(infile: TextIO, image_txt: TextIO) -> None:
    image_file = utility.get_image(infile)
    print('P3', file=image_txt)
    print('{} {}'.format(image_file.header.width, image_file.header.height), file=image_txt)
    print('{}'.format(image_file.header.max_color), file=image_txt)
    for pixel in image_file.pixels:
        red_value = pixel.red * 10
        if red_value > image_file.header.max_color:
            red_value = image_file.header.max_color
        blue_value = red_value
        green_value = red_value
        if green_value > image_file.header.max_color:
            green_value = image_file.header.max_color
        if blue_value > image_file.header.max_color:
            blue_value = image_file.header.max_color
        print('{} {} {}'.format(red_value, green_value, blue_value), file=image_txt)
# I formatted the file with the get image function, and then printed the header,
# then changed all of the color values for the pixels where the red component
# was multiplied by 10, and the others were set equal to the origional red value.


def main(argv: List[str]) -> None:
    try:
        if len(sys.argv) > 1:
            print('opened')
            infile = open(sys.argv[1], 'r')
            image_txt = open('hiddenfile.ppm', 'w')
            process_file(infile, image_txt)
            infile.close()
            image_txt.close()
    except (FileNotFoundError, IndexError) as e:
        print(e)
# I opened the file for reading, and then created and opened another file for writing, sent both to processing,
# and then closed them all, while checking for errors


if __name__ == '__main__':
    main(sys.argv)
