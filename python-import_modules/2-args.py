#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lenArg = len(sys.argv)
    if lenArg <= 1:
        print("0 arguments.")
    elif lenArg == 2:
        print(f"{lenArg - 1} argument:")
    else:
        print(f"{lenArg - 1} arguments:")
    for item in range(1, lenArg):
        print(f"{item}: {sys.argv[item]}")
