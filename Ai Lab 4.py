# Task 1


def luhn_algorithm(card_number):
    digits = [int(d) for d in str(card_number)]
    numbers = digits.pop()
    digits.reverse()

    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits) + numbers
    return total % 10 == 0
card_number = 5590490233111416
print("Valid Card" if luhn_algorithm(card_number) else "Invalid Card")



# Task 2


def remove_punctuations(text):
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    result = ""
    for char in text:
        if char not in punctuations:
            result += char
    return result
text = "Hello! My name is --- Muhammad Zain!"
print(remove_punctuations(text))

# Task 3


def arrange_words(text):
    parts = text.split()
    n = len(parts)

    for a in range(n):
        for b in range(0, n - a - 1):
            if parts[b].lower() > parts[b + 1].lower():
                parts[b], parts[b + 1] = parts[b + 1], parts[b]

    return " ".join(parts)
def arrange_letters(text):
    words = text.split()
    new_list = []

    for item in words:
        letters = list(item)
        size = len(letters)

        for x in range(size):
            for y in range(0, size - x - 1):
                if letters[y].lower() > letters[y + 1].lower():
                    letters[y], letters[y + 1] = letters[y + 1], letters[y]

        new_list.append("".join(letters))

    return " ".join(new_list)

line = "My name is Zain Ali "
print("Words arranged:", arrange_words(line))
print("Letters arranged:", arrange_letters(line))
