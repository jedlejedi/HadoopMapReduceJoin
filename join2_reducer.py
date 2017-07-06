#!/usr/bin/env python

import sys

tv_show = ""
count = 0
for line in sys.stdin:
    key, value = line.split("\t")
    key = key.strip()
    value = value.strip()

    if value == "ABC":
        print format("%s\t%s" % (tv_show, count))
    else:
        if key != tv_show:
            count = 0
            tv_show = key
        count += int(value)
