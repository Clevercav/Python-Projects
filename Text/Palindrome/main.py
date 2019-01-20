def main():
    print()
    print("Is your input a palindrome? Let's find out")
    while(True):
        value = input("Enter your word: ")
        palindrome(value.lower())


def palindrome(value):
    if(value == reverse_string(value)):
        print("It is!")
        return
    print("Unfortunatly not...")
    return


def reverse_string(x):
    return x[::-1]


if __name__ == '__main__':
    main()
