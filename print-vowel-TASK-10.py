def print_vowel(any_string):
    output = ""
    for vowel in any_string.lower():
        if vowel in 'aeiou':
            output +=vowel
    return output
    
print_vow = print_vowel("HELLO")
print(print_vow)
