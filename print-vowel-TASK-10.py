any_string = input("Enter any string: ")


def print_vowel(any_string):
    output = ""
    for vow in any_string:
        if vow in 'aeiou':
            output +=vow
    return output
    
print_vow = print_vowel(any_string.lower())
print(print_vow)
