#!/usr/bin/python3

# process
#def c2f(c):
#    return c * 9 / 5 + 32
def f2c(f):
    return f - 32 * 5 / 9

def main(fah):
    return f2c(fah)

if __name__ == "__main__":
    f = 0           # input
    print(main(f))  # output
