from typing import List, TextIO
import sys
import utility


def embiggen_square(list: List[List[utility.Pixel]]) -> List[utility.Pixel]:
    acc = []
    acc2 = []
    acc_final = []
    for row in list:
        for column in row:
            acc2.append(column)
            acc2.append(column)
        acc.append(acc2)
        acc.append(acc2)
        acc2 = []
    for row in acc:
        for column in row:
            acc_final.append(column)
    return acc_final
# I wrote a function that makes takes the list of lists and creates a new list that duplicates them by column and then
# duplicates the rows, where after it loops in to make it all one big list rather than a list of lists


def groups_of_n(sequence: List[utility.Pixel], width: int) -> List[List[utility.Pixel]]:
    acc = []
    for index in range(0, len(sequence), width):
        sub_list = []
        for i in range(0, width):
            sub_list.append(sequence[index + i])
        acc.append(sub_list)
    return acc
# this was copied from the previous task, it makes the initial image file into the list of lists format


def write_pixels(pixels: List[utility.Pixel], file: TextIO) -> None:
    for pixel in pixels:
        print('{} {} {}'.format(pixel.red, pixel.green, pixel.blue), file=file)
# this writes color values so that they are written into the file


def process_file(infile: TextIO, image_txt: TextIO) -> None:
    image_file = utility.get_image(infile)
    print('P3', file=image_txt)
    print('{} {}'.format(image_file.header.width * 2, image_file.header.height * 2), file=image_txt)
    print('{}'.format(image_file.header.max_color), file=image_txt)
    write_pixels(embiggen_square(groups_of_n(image_file.pixels, image_file.header.width)), image_txt)
# this process function writes the header, as well as sends the image file and the file to be written to the other
# functions to process it properly, and then it sends it to be written in the writing function.


def main(argv: List[str]) -> None:
    if len(sys.argv) > 1:
        try:
            print('opened')
            infile = open(sys.argv[1], 'r')
            image_txt = open('expanded.ppm', 'w')
            process_file(infile, image_txt)
            infile.close()
            image_txt.close()
        except (IndexError, FileNotFoundError) as e:
            print(e)
# I opened the file for reading, and then created and opened another file for writing, sent both to processing,
# and then closed them all, while checking for errors


if __name__ == '__main__':
    main(sys.argv)
