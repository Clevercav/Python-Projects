def main():
    while(True):
        i = input("Type in the string to reverse: ")
        reverse(i)


# Reverses string
def reverse(input):
    result = ""
    for i in range(len(input)):
        result += input[-i - 1]
    print("Result: \"" + result + "\"")


if __name__ == '__main__':
    main()
