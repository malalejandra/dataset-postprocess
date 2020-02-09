import argparse
from pathlib import Path
import exifread


parser = argparse.ArgumentParser(
    description='Get the ISO speed from a RAW file',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('raw_file', type=Path, help='Path to RAW file to extract ISO from')


def main(args):
    with args.raw_file.open('rb') as f:
        tags = exifread.process_file(f)
    print(tags['EXIF ISOSpeedRatings'])

if __name__ == '__main__':
    main(parser.parse_args())
