import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".gif"
    im = Image.open(infile)

    if infile != outfile:
        try:
            if im.mode != "RGB":
                im = im.convert("RGB")
            im.save(outfile)
        except IOError:
            print "cannot convert", infile
