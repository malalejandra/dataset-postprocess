import argparse
from pathlib import Path
import os
import exifread
from pyunraw import PyUnraw

parser = argparse.ArgumentParser(
    description="Organise a bunch of RAW files into folders by ISO",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "raw_files_dir", type=Path, help="Path to folder containing raw files"
)
parser.add_argument(
    "organised_files_dir",
    type=Path,
    help="Path to folder containing raw files organised by ISO",
)


def get_iso(raw_path: Path) -> int:
    f = PyUnraw(str(raw_path))
    props = f.get_file_properties()
    try:
        return props["ISO"]
    except (KeyError, TypeError):
        raise Exception(f"Could not read ISO speed from {raw_path}")


def symlink_relative(source: Path, target: Path) -> None:
    source = Path(str(source))
    target = Path(str(target))
    symlink_source = os.path.relpath(source, start=target.parent)
    symlink_dir = target.parent
    symlink_dir.mkdir(exist_ok=True, parents=True)
    try:
        dir_fd = os.open(symlink_dir, os.O_RDONLY)
        os.symlink(symlink_source, target.name, dir_fd=dir_fd)
    finally:
        if dir_fd:
            os.close(dir_fd)


def main(args):
    raw_path: Path
    for raw_path in args.raw_files_dir.iterdir():
        if any([raw_path.suffix.lower().endswith(ext) for ext in ['arw', 'nef']]):
            iso = get_iso(raw_path)
            target = args.organised_files_dir / str(iso) / raw_path.name
            symlink_relative(raw_path, target)


if __name__ == "__main__":
    main(parser.parse_args())
