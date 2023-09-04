#!/bin/sh
# BRE: Basic Regular Expression (POSIX)
# ERE: Extended Regular Expression (POSIX)
# PCRE: Perl Compatible Regular Expression. used in many languages

# meta character list
# .: any character
# ^: start of line
# $: end of line
# *: zero or more
# +: one or more
# ?: zero or one
# {n}: n times
# {n,}: n or more times
# {n,m}: n to m times
# []: character class
# [^]: negated character class
# (): group
# |: alternative
# \: escape
# \n: newline
# \r: carriage return
# \t: tab
# \v: vertical tab
# \f: form feed
# \a: alarm (bell)
# \e: escape
# \cX: control character
# \x: hexadecimal character
# \u: unicode character
# \l: lowercase next character
# \u: uppercase next character
# \L: lowercase all characters until \E
# \U: uppercase all characters until \E
# \Q: quote (disable) pattern metacharacters until \E
# \E: end case modification
# \w: word character
# \W: non-word character
# \s: whitespace character
# \S: non-whitespace character
# \d: digit
# \D: non-digit
# \b: word boundary
# \B: non-word boundary
# \A: start of string
# \Z: end of string
# \z: end of string (except for final line terminator)
# \G: end of previous match
# \p: unicode property
# \P: negated unicode property
# \Q: quote (disable) pattern metacharacters until \E
# \E: end case modification

readonly path="yakei_kobe.csv"
cat $path | grep -E "^1"
cat $path | grep -E ",.{5},"

echo abcdefgh | sed -E "s/.*(d.).*/\1/"