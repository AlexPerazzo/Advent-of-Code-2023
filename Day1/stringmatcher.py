def build_table(pattern, inputs):
    table = []

    for k in range(len(pattern) + 1):
        char_map = {}

        for letter in inputs:
            pk_letter = pattern[:k] + letter
            temp = [k + 1, len(pattern)]
            i = min(temp)

            while not pk_letter.endswith(pattern[:i]):
                i -= 1

            char_map[letter] = i

        table.append(char_map)

    return table


def string_matcher(text, pattern, inputs):
    table = build_table(pattern, inputs)
    state = 0
    match_state = len(table) - 1
    results = []

    for index in range(len(text)):
        state = table[state][text[index]]

        if state == match_state:
            results.append(index)
            state = 0  # Reset the state to 0 after a match

    return results


# # Example usage:
# text_example = "abababab"
# pattern_example = "ab"
# inputs_example = ['a', 'b']

# matches = string_matcher(text_example, pattern_example, inputs_example)
# print(matches)