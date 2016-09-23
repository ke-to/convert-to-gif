# -*- coding: utf-8 -*- 
#######################
# 使用する際のコマンド例
# $ python convert.py jpg xxx.gif
# $ python スクリプト名 拡張子 画像パス（半角スペース区切りで複数可）
#######################

import os, sys
from PIL import Image

for infile in sys.argv[2:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".%s" % sys.argv[1]
    im = Image.open(infile)

    if infile != outfile:
        try:
            if im.mode != "RGB":
                im = im.convert("RGB")
            im.save(outfile)
        except IOError:
            print "cannot convert", infile
