from typing import List, TextIO
import sys
import data
import utility


def groups_of_n(sequence: List[utility.Pixel], width: int) -> List[List[utility.Pixel]]:
    acc = []
    for index in range(0, len(sequence), width):
        sub_list = []
        for i in range(0, width):
            sub_list.append(sequence[index + i])
        acc.append(sub_list)
    return acc
# I made a groups function to get the file we are reading into a more digestible format


def shrink_square(list: List[List[utility.Pixel]], width: int) -> List[utility.Pixel]:
    acc = []
    if width % 2 == 0:
        for row in range(0, len(list), 2):
            for column in range(0, width, 2):
                red_value = (list[row][column].red + list[row][column + 1].red + list[row + 1][column].red +
                             list[row + 1][column + 1].red) // 4
                green_value = (list[row][column].green + list[row][column + 1].green + list[row + 1][column].green +
                             list[row + 1][column + 1].green) // 4
                blue_value = (list[row][column].blue + list[row][column + 1].blue + list[row + 1][column].blue +
                             list[row + 1][column + 1].blue) // 4
                acc.append(data.Pixel(red_value, green_value, blue_value))
    elif width % 2 == 1:
        for index in range(0, len(list) - 1, 2):
            for element in range(0, width - 1, 2):
                red_ave = (list[index][element].red + list[index][element + 1].red + list[index + 1][element].red +
                           list[index + 1][element + 1].red) // 4
                green_ave = (list[index][element].green + list[index][element + 1].green +
                             list[index + 1][element].green + list[index + 1][element + 1].green) // 4
                blue_ave = (list[index][element].blue + list[index][element + 1].blue + list[index + 1][element].blue
                            + list[index + 1][element + 1].blue) // 4
                acc.append(data.Pixel(red_ave, green_ave, blue_ave))
    print(len(acc))
    return acc
# I made a function that checks if the width of the file is odd or even, and then restricts the bounds accordingly so
# we don't get indexing errors when files have even or odd widths. Then I looped into the lists to take the average of
# the pixel values, and then only doing that average on the select square of pixels we want.


def write_pixels(pixels: List[utility.Pixel], file: TextIO) -> None:
    for pixel in pixels:
        print('{} {} {}'.format(pixel.red, pixel.green, pixel.blue), file=file)
# I made a helper function that will convene all my pixel information to be written into the file.


def process_file(infile: TextIO, image_txt: TextIO) -> None:
    image_file = utility.get_image(infile)
    print('P3', file=image_txt)
    print('{} {}'.format(image_file.header.width // 2, image_file.header.height // 2), file=image_txt)
    print('{}'.format(image_file.header.max_color), file=image_txt)
    write_pixels(shrink_square(groups_of_n(image_file.pixels, image_file.header.width), image_file.header.width),
                 image_txt)
# I wrote a process file that formats the header as well as runs all my functions and then sends the final list of
# pixels to a writing function to send it to the file


def main(argv: List[str]) -> None:
    if len(sys.argv) > 1:
        try:
            print('opened')
            infile = open(sys.argv[1], 'r')
            image_txt = open('shrunk.ppm', 'w')
            process_file(infile, image_txt)
            infile.close()
            image_txt.close()
        except (IndexError, FileNotFoundError) as e:
            print(e)
# I opened the file for reading, and then created and opened another file for writing, sent both to processing,
# and then closed them all, while checking for errors


if __name__ == '__main__':
    main(sys.argv)
