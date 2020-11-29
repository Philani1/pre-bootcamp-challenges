def common_char(f_string, s_string):
    output = ""
    for i in range(len(s_string)):
        for j in range(len(f_string)):
            if s_string[i] == f_string[j]:
                output += f_string[j] + ", "
    return output

common_letters = common_char("house", "computers")

print(f"Common letters: {common_letters}" )