rule debayer:
    input: "data/raw/{filename}.ARW"
    output: "data/interim/{filename}.TIFF"
    shell:
    """
    # -T = Write to TIFF
    # -6 = Write to 16-bit instead of 8 bit
    # -w = Use camera white balance if present
    dcraw -T -6 -w {input}
    mv {wildcards.filename}.TIFF {output}
    """


rule all:
   input: 
