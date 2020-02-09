import argparse
from pathlib import Path
import subprocess
import re
import sys


parser = argparse.ArgumentParser(
    description='Get the ISO speed from a RAW file',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('raw_file', type=Path, help='Path to RAW file to extract ISO from')


def main(args):
    iso_speed_regexp = re.compile(r'ISO speed: (\d+)')
    cli_command = ['dcraw', '-i', '-v', str(args.raw_file)]
    output = subprocess.run(cli_command, check=True, capture_output=True)
    dcraw_output = output.stdout.decode('utf-8')
    groups = iso_speed_regexp.search(dcraw_output)
    if not groups:
        print("Could not parse ISO speed from dcraw output")
        sys.exit(-1)
    iso_speed = int(groups[1])
    print(iso_speed)


if __name__ == '__main__':
    main(parser.parse_args())
