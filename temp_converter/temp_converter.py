#!/usr/bin/python3

# process
#def c2f(c):
#    return c * 9 / 5 + 32
def f2c_raw(f):
    return f - 32 * 5 / 9

def f2c_op(f):
    return (f - 32) * 5 / 9

def main():
    f = 0           # input
    c = f2c(f)
    print(f"{f}F is {c} C")

if __name__ == "__main__":
    main()
