#!/bin/sh
# cat: concatenate. files and print on the standard output
# -n: number all output lines
# -b: number non-blank output lines

# grep: print lines matching a pattern
# -n: line number
# -i: ignore case distinctions
# -v: select non-matching lines
# -c: print only a count of matching lines
# -l: print only names of FILEs containing matches
# -L: print only names of FILEs containing no match
# -r: recursive
# -w: select only those lines containing matches that form whole words
# -x: select only those matches that exactly match the whole line
# -f: obtain PATTERN from FILE
# -e: use PATTERN as a pattern
# -E: use PATTERN as an extended regular expression
# -F: use PATTERN as a set of fixed strings
# -o: show only the part of a line matching PATTERN
# -q: quiet
# -s: suppress error messages
# -H: print the file name for each match

# cut: remove sections from each line of files
# -c: select only these characters
# -f: select only these fields; also print any line that contains no delimiter character, unless the -s option is specified
# -d: use DELIM instead of TAB for field delimiter
# -s: do not print lines not containing delimiters

# sed: stream editor for filtering and transforming text
# -n: suppress automatic printing of pattern space
# -e: add the script to the commands to be executed
# -f: add the contents of script-file to the commands to be executed
# -i: edit files in place (makes backup if extension supplied)
# -r: use extended regular expressions in the script
# -s: consider files as separate rather than as a single continuous long stream

readonly path="yakei_kobe.csv"
readonly keyword="六甲"
readonly regex="s/,/ /g"

cat $path | grep -i $keyword
cat $path | grep -i $keyword | cut -d , -f 1,2
cat $path | grep -i $keyword | sed "${regex}"