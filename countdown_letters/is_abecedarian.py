"""
The following function returns True if the word passed as input is an
abecedarian word. That is a word where the each letter in the word is a
subsequent letter in the alphabet. 'Ant' would be a simple example.
"""


def is_string_abecederian(word: str) -> bool:
    max_letter = ''
    letters_tested = 0
    for letter in word.lower():
        if letter < max_letter:
            return False
        else:
            max_letter = letter
            letters_tested += 1
    if letters_tested == len(word):
        return True

results = []
with open('countdown_letters/words.txt', 'r') as test_file:
    for line in test_file:
        result = False
        tested_word = line.replace('\n', '')
        if is_string_abecederian(tested_word):
            results.append(tested_word)

print(f"There are {len(results)} abecedarian words in the file. These are: \n")
print(results)
