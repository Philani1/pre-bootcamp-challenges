def common_char(first_string, second_string):
    output = ""
    for character_sec in range(len(second_string)):
        for character_first in range(len(first_string)):
            if second_string[character_sec] == first_string[character_first]:
                output += first_string[character_first] + ", "
    return output


if __name__ == "__main__":
    print(f"Common letters: {common_char('house', 'computers')}")
