from math import fabs

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print(sorted(data, key=fabs, reverse=False))
    print(sorted(data, key=lambda i: fabs(i), reverse=False))
