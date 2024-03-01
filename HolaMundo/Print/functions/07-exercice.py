def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


# print(no_space("Hello World"))


def reverse(text):
    text_reverse = ""
    for char in text:
        text_reverse = char + text_reverse
    return text_reverse


def is_palindrome(phrase):
    phrase = no_space(phrase)
    text_reverse = reverse(phrase)
    # print(text_reverse)
    return phrase.lower() == text_reverse.lower()


print(is_palindrome("Hello"))
