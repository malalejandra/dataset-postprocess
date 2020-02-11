import argparse
from pathlib import Path
import pyunraw
from pyunraw import PyUnraw

parser = argparse.ArgumentParser(
    description='Get the ISO speed from a RAW file',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('raw_file', type=Path, help='Path to RAW file to extract ISO from')


def main(args):
    print(PyUnraw(str(args.raw_file)).get_file_properties()['ISO'])

if __name__ == '__main__':
    main(parser.parse_args())
