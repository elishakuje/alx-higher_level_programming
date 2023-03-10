#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    var_len = len(argv) - 1

    result = 0
    for i in range(1, var_len + 1):
        result += int(argv[i])
    print(result)
