"""This program prints the largest number in a non empty list."""

def find_max(xs : list[float]) -> int:
    """Returns the largest element of the given non-empty list."""
    max= 0
    x=1
    while x<len(xs):
        if xs[x]>xs[max]:
            max=x

        x+=1
    return max

def main():
    ys = [57.60, 85.43, 96.80, 8.92, 23.53, 78.40, 32.59, 97.81, 12.34, 10.70]
    max = find_max(ys)
    print(max)

if __name__ == '__main__':
    main()
