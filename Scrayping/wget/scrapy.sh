#!/bin/sh
readonly url="https://gihyo.jp/dp"

Crawl () {
    wget $1 -q -O -
}
Capture () {
    # ex s/$1/\1/
    echo "s$2$1$2$3$2"
}
Replace () {
    #"s/$1//g"
    echo "s$2$1$2$3$2g"
}



Crawl $url | grep -E 'class="paging-number".*-' | sed -E $(Replace '<[^>]*>' '/' '')
echo "capture"
Crawl $url | grep -E 'class="paging-number".*-' | sed -E "$(Capture '.*/ ([0-9]+).*' '@' '\1')"
echo "greedy（欲張り型）"
Crawl $url | grep -E 'class="paging-number".*-' | sed -E "$(Capture '.*([0-9]+).*' '@' '\1')"
echo "Microdata (itemprop)"
Crawl $url | grep -E 'itemprop="name"' | sed -E "$(Capture '<br/>' '@' ' ')" | sed -E $(Replace '<[^>]*>' '/' '') | sed -E "$(Capture '^ *' '@' '')"
