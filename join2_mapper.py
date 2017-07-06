#!/usr/bin/env python

import sys

for line in sys.stdin:
    tv_show, channel_or_num_viewer = line.split(",")
    tv_show = tv_show.strip()
    channel_or_num_viewer = channel_or_num_viewer.strip()
    if channel_or_num_viewer == "ABC" or channel_or_num_viewer.isdigit():
        print format("%s\t%s" % (tv_show, channel_or_num_viewer))

