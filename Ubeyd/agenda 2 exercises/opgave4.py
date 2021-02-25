def opgave4(x, y, z):
    median = (x + y + z) - min(x, y, z) - max(x, y, z)
    print(median)


def main():
    opgave4(29, 65, 100)


main()