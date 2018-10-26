""" String Phrase Reversal Challenge

Objective:
    Write a function that will take any given string as input and
    will output the reverse order of the string phrase.
    * Punctuation should not be altered and should remain in place.

Examples:
    'Hello World!' would become 'World Hello!'
    'Everybody wants, to rule the world?' should become 'world the, rule to wants Everybody?'

Run the program:
    On windows:
        $ python app.py
    On mac:
        $ python3 app.py
"""


__author__ = 'Carlos Kidman'


import string


def reverse_phrase(phrase):
    split = phrase.split()
    punc_tokens = []
    word_tokens = []

    for word in split:
        ch = word[-1]
        if ch in string.punctuation:
            punc_tokens.append(ch)
            word_tokens.append(word.replace(ch, ''))
        else:
            punc_tokens.append('')
            word_tokens.append(word)

    word_tokens.reverse()
    words = []

    for index, word in enumerate(word_tokens):
        word += punc_tokens[index]
        words.append(word)

    return ' '.join(words)


if __name__ == '__main__':
    print(reverse_phrase('Hello, World!'))
    print(reverse_phrase('Everybody wants, to rule the world?'))
