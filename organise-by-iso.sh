#!/usr/bin/env bash
set -ex
shopt -s nullglob

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

for scene_dir in data/raw/images/*; do
  for camera_dir in "$scene_dir"/*; do
    target_camera_dir="data/interim/images_by_iso/$(basename "$scene_dir")/$(basename "$camera_dir")"
    python organise_by_iso.py "$camera_dir" "$target_camera_dir" &
  done
done
for camera_dir in data/raw/dark_frames/*; do
  target_camera_dir="data/interim/dark_frames/$(basename "$camera_dir")"
  python organise_by_iso.py "$camera_dir" "$target_camera_dir" &
done

wait