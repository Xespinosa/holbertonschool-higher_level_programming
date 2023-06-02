#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    k = 0
    x = int(sys.argv[1:])
    for i, arg in enumerate(x, start=1):
        k += arg
