"""

"""
import argparse
import subprocess
import tempfile
import logging
import os
from bingo import bingo
from bingo import card_maker


def get_words_from_textfile(textfile_handler):
    """Yield the words by parsing a given text fileahandler."""
    for line in textfile_handler:
        line = line.rstrip()
        yield line


def make_bingo_card_deck(words, size, count):
    bingo_generator = bingo.BingoGenerator(size=size)
    bingo_generator.words = words
    bingo_card_maker = card_maker.LaTeXCardMaker(size)
    bingo_generator.maker = bingo_card_maker
    tempdir = tempfile.mkdtemp()
    pages = []
    for index, card in enumerate(bingo_generator.make_lots_of_cards(count)):
        filename = os.path.join(tempdir, "%s.tex" % index)
        with open(filename, 'w') as f:
            f.write(card)
        cmd = "pdflatex --output-directory=%s %s" % (tempdir, filename)
        logging.info("Generating PDF: %s" % cmd)
        status = subprocess.call(cmd, shell=True)
        # subprocess.Popen(cmd, shell=True,
        #                  stdout=subprocess.PIPE,
        #                  cwd=tempdir).communicate()
        pages.append(os.path.join(tempdir, "%s.pdf" % index))
    _merge_PDFs(pages)


def _merge_PDFs(pages):
    """Merge the given PDFs into one."""
    print pages
    output_filename = "bingo_deck.pdf"
    output_filepath = output_filename
    has_pyPdf = False
    try:
        import pyPdf
        has_pyPdf = True
    except ImportError:
        pass
    if has_pyPdf:
        logging.info("Using 'pyPdf' to join PDFs")
        output = pyPdf.PdfFileWriter()
        inputfiles = []
        for page in pages:
            inputstream = file(page, "rb")
            inputfiles.append(inputstream)
            reader = pyPdf.PdfFileReader(inputstream)
            output.addPage(reader.getPage(0))
        outputStream = file(output_filepath, "wb")
        output.write(outputStream)
        outputStream.close()
        for f in inputfiles:
            f.close()
    else:
        logging.warning("PyPDF not installed, cannot merge PDF slides")


def main():
    parser = argparse.ArgumentParser(description="Bingo generator")

    parser.add_argument("-s", "--size",
                        type=int,
                        dest="size",
                        metavar="SIZE",
                        required=False,
                        default=5,
                        help="The size of the bingo grid")
    parser.add_argument("-l", "--list", metavar="LIST",
                        dest="word_list",
                        type=argparse.FileType('r'),
                        help='A list of words')
    parser.add_argument("-c", "--count", metavar="COUNT",
                        dest="count",
                        required=False,
                        default=1,
                        type=int,
                        help='Number of grids to generate')
    parser.add_argument("words",
                        nargs='*',
                        metavar="WORDS",
                        help='A list of words')
    args = parser.parse_args()
    size = args.size

    log_level = logging.INFO
    logging.basicConfig(level=log_level)

    if args.word_list:
        words = list(get_words_from_textfile(args.word_list))
        make_bingo_card_deck(words, size, args.count)
    elif args.words:
        make_bingo_card_deck(args.words, size, args.count)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
