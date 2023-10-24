#!/usr/bin/python3

import sys
import os
import re
import glob

if len(sys.argv) != 3:
    print("""Usage: reg-rename <pattern_source> <pattern_target>""")
    exit(0)

source_pattern = sys.argv[1]
target_pattern = sys.argv[2]


print(source_pattern, "->", target_pattern)

patt = re.compile(source_pattern)

files = glob.glob('./*')
for file in files:
    clean = file.replace("./", "")
    match = patt.match(clean)
    if not match:
        continue

    groups = match.groups()
    if groups:
        target_cur = target_pattern
        for i in range(len(groups)):
            target_cur = target_cur.replace(f"({i+1})", groups[i])

    print(file,"->",target_cur)
    os.rename(file, target_cur)

