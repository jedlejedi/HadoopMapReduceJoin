#!/usr/bin/env python

import sys

for line in sys.stdin:
    key, value = line.split(",")
    key = key.strip()
    value = value.strip()
    if value == "ABC" or value.isdigit():
        print format("%s\t%s" % (key, value))

