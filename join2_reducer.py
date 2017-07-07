#!/usr/bin/env python

import sys

tv_show = ""
count = 0
is_abc = False

for line in sys.stdin:
    key, value = line.split("\t")
    key = key.strip()
    value = value.strip()

    if key != tv_show:
        if is_abc:
            print format("%s\t%s" % (tv_show, count))
        is_abc = False
        count = 0
        tv_show = key

    if value == "ABC":
        is_abc = True
    else:
        count += int(value)

if is_abc:
    print format("%s\t%s" % (tv_show, count))
