
def main():
    for x in range(1, 11):
        for y in range(1, 11):
            print("{} x {} = {}".format(x, y, x * y))
        print("\n---------------------------------------\n")

if __name__ == "__main__":
    main()