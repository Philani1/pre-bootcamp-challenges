def print_vowel(any_string):
    output = ""
    for vowel in any_string.lower():
        if vowel in "aeiou":
            output += vowel
    return output


if __name__ == "__main__":
    print(print_vowel("HELLO"))
