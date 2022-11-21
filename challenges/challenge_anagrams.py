def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    first_string_text = "".join(bubble_sort(first_string))
    second_string_text = "".join(bubble_sort(second_string))

    if first_string_text == second_string_text:
        return (first_string_text, second_string_text, True)
    else:
        return (first_string_text, second_string_text, False)


def bubble_sort(word):
    size = len(word)
    list_words = list(word.lower())

    for i in range(0, size):
        for j in range(0, size):
            if list_words[i] < list_words[j]:
                list_words[i], list_words[j] = list_words[j], list_words[i]
    return list_words
