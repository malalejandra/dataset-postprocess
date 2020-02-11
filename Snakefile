from pathlib import Path

#path.stem - The final path component, without its suffix

IMAGES = [p.stem for p in Path('data/raw/images/').iterdir()]


rule all:
   input: ["data/interim/tiff/{}.TIFF".format(image) for image in IMAGES]

rule debayer_sony:
    input: "data/interim/images_by_iso/{scene}/{camera}/{iso}/{filename}.ARW"
    output: "data/interim/debayed/{scene}/{camera}/{iso}/{filename}.TIFF"
    shell:
      """
      # -T = Write to TIFF
      # -6 = Write to 16-bit instead of 8 bit
      # -w = Use camera white balance if present
      dcraw -T -6 -w {input}
      mv "$(dirname {input})"/{wildcards.filename}.tiff {output}
      """

rule register:
    input: "data/interim/tiff/{filename}.TIFF"
    output: "data/registered/tiff/{filename}.TIFF"
    # shell: python path_to_script

rule subtract_dark:
    input:
        raw_file="data/images/{iso}/{filename}",
        dark_frame="data/dark_frames/{iso}"
    output: "data/dark_subtracted/{iso}/{filename}.TIFF"
    shell:
      """
      # -T = Write to TIFF
      # -6 = Write to 16-bit instead of 8 bit
      # -w = Use camera white balance if present
      dcraw -T -6 -w {input.raw_file}
      mv data/raw/images/{wildcards.filename}.tiff {output}
      """

