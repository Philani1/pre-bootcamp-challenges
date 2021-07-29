def print_vowel(any_string):
    output = ""
    for vowel in any_string.lower():
        if vowel in "aeiou":
            output += vowel
    output = "Vowels: " + ", ".join(sorted(set(output), key=output.index))
    print(output)


if __name__ == "__main__":
    print_vowel("Umuzi")
