import random

def gen_random(count, start, end):
    for _ in range(count):
        yield random.randint(start, end)

if __name__ == '__main__':
    print(list(gen_random(10, 2, 8)))