#!/bin/sh
readonly url="http://gihyo.jp"
echo "sample $url"

# -O: output file name
# -0 -: output to stdout
# -q: quiet
# default output file name: index.html
wget $url
wget $url -q -O -
wget $url -q -O top_page.html

# -r : recursive
# -l : recursive depth
# -np: not parent directory (--no-parent)
# -w : wait time
# -p : download page
# --restrict-file-names=nocontrol: not escape file name
# 上書き保存
wget $url -q -r -np -l 1 -w 1 -O depth_1.html