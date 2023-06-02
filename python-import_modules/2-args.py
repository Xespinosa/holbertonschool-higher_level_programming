#!/usr/bin/env python3
import sys
args = sys.argv[1:]
argc = len(args)
i = 0

if argc == 0:
    print(argc, " arguments.")
elif argc == 1:
    print(argc, " argument:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
else:
    print(argc, " arguments:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
