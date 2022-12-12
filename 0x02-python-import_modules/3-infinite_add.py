#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    count = len(sys.argv)
    for i in range(count - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
