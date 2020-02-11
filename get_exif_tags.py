import argparse
from pathlib import Path
from pprint import pprint

import exifread


parser = argparse.ArgumentParser(
    description='Get the EXIF data from a RAW file',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('raw_file', type=Path, help='Path to RAW file')


def main(args):
    with args.raw_file.open('rb') as f:
        tags = exifread.process_file(f)
    pprint(tags)


if __name__ == '__main__':
    main(parser.parse_args())