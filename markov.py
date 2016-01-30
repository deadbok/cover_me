#!/usr/bin/env python3
"""
Save word association statistics as JSON data
"""
import re
import sys
import json
import random
from collections import OrderedDict


def prepare_word(text, word, newline):
    """
    return a word that can be added to the text in a sensible way.

    :param text: Text to add word to.
    :type text: str.
    :param word: Word to add.
    :type word: str.
    :param newline: Filter out newlines.
    :type newline: Boolean.
    """
    # Capitalise I, and I'm...
    if word == 'i' or word.startswith("i'"):
        word = word.capitalize()

    if not newline:
        word = word.strip('\n')

    # Check if we are on a new line, with no text.
    if (re.search(r'\n\W*$', text) is not None):
        if word.strip('\n') in ',.!?':
            return(None, False)

    # Handle newline at the end.
    if text.endswith('\n'):
        word = word.capitalize()
        return(word, True)

    if word.strip('\n') not in ',.!?':
        if text == '':
            return(word, True)
        word = ' ' + word
        return(word, True)

    return(word, False)


def markov_gen(start_word=None, newline=True, n_words=1, corpus=None):
    """
    Generate a string.

    :param start_word: Word to start of with, a random if chosen if None.
    :type start_word: string or None
    :param newline: Allow newline in generated string.
    :type newline: Boolean
    :param n_words: Number of words to generate.
    :type n_words: int
    :param corpus: Dictionary to use for text generation.
    :type corpus: dict
    """
    if corpus is None:
        exit('No word corpus.')

    # Pick a random word if there is nowhere else to start.
    if (start_word is None) or (start_word.strip() == ''):
        last_word = random.choice(list(corpus.keys()))
    else:
        last_word = start_word

    ret = ''
    count = False

    while n_words > 0:
        # Make up something if there is nothing to go from.
        if last_word is None:
            last_word = random.choice(list(corpus.keys()))

            last_word, count = prepare_word(ret, last_word, newline)
            if count:
                n_words -= 1
            ret += last_word

        last_word = last_word.lower().strip(' ')

        if n_words > 0:
            # Use the corpus if the word is in there.
            if last_word in corpus.keys():
                # Good thing nobody is ever going to see this ugly sequence.
                # Get a dict sorted by occurrence.
                word_dict = OrderedDict(sorted(corpus[last_word].items(),
                                               key=lambda x: x[1]))
                # Make a list of words from it.
                word_list = list(word_dict.keys())
                # Highest first.
                word_list.reverse()
                # Get a random index into the list
                widx = random.randint(0, len(word_dict) - 1)
                if widx == 0:
                    word = word_list[widx]
                else:
                    # Choose a word between the start in that index.
                    word = random.choice(word_list[0:widx])

                word, count = prepare_word(ret, word, newline)
                if word is not None:
                    ret += word
                if count:
                    n_words -= 1

                last_word = word
            else:
                last_word = None

    return(ret)


def get_last_word(text):
    """
    # Return the last word in a string including last newline.

    :param text: String to search.
    :type text: str
    """
    ret = re.search(r'([\w\']+[-\w+]*)\W*$', text)
    if ret is not None:
        ret = ret.group(1)
        if text.endswith('\n'):
            ret += '\n'
    return(ret)


def add_string(text, string, capitalize):
    """
    Add a string to the text while taking care of capitalisation.

    :param text: text to add string to.
    :type text: str
    :param string: Word to add.
    :type string: str.
    """
    if capitalize:
        text += string[0].upper() + string[1:]
    else:
        text += string
    return(text)


def main():
    """
    Create a dictionary of word associations for later use in a markov
    generator and save it as a file.
    """
    print('')
    random.seed()
    # Load JSON Markov seed corpus.
    with open("words.json") as corpus_file:
        corpus = json.load(corpus_file)

    if len(sys.argv) > 1:
        # Load a template file.
        with open(sys.argv[1]) as tpl_file:
            template = tpl_file.read()
    else:
        # Default to creating 3 word title and 200 words Markov".
        template = "**{.!3}**\n\n{.50}\n"

    if len(sys.argv) > 2:
        # Load a text file of words to use with the Markov seed corpus.
        with open(sys.argv[2]) as word_file:
            words = word_file.read().split()
    else:
        words = None

    text = ''
    blocks = list()
    newline = False
    last_word = None
    capitalize = False

    for tpl_token in re.split(r'({[^}]+})', template):
        # Not a template command token.
        if '{' in tpl_token:
            # Allow newlines?
            if tpl_token[1] == '!':
                newline = False
            else:
                newline = True

            if '.' in tpl_token:
                capitalize = True
            else:
                capitalize = False

            # Get last word for the Markov generator.
            last_word = get_last_word(text)
            # Convert the numerical part of the token.
            value = int(tpl_token.strip('{}!.'))

            # Reference or new Markov string?
            if value > 0:
                # Keep a list of generated block.
                # Insert Markov string.
                blocks.append(markov_gen(last_word, newline, value, corpus))
                text = add_string(text, blocks[-1], capitalize)
            else:
                # Insert previous string.
                value = abs(value)
                if value > len(blocks):
                    exit("Reference to unknown block: " + str(value) + ".")
                blocks.append(blocks[value - 1])
                text = add_string(text, blocks[-1], capitalize)
        else:
            text += tpl_token

    print(text)

if __name__ == '__main__':
    main()
