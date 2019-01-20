def main():
    while(True):
        string = input("Type in your string: ")
        vowels = get_vowels_dict(string)
        print_total_vowels(vowels)
        print_count_of_each_vowel(vowels)


def get_vowels_dict(input):
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for char in input:
        if(char.lower() in vowels):
            vowels[char] += 1
    return vowels


def print_count_of_each_vowel(vowels):
    for key, value in vowels.items():
        print(key, ":", value)


def print_total_vowels(vowels):
    print("Total vowels: ", sum(vowels.values()))


if __name__ == "__main__":
    main()
