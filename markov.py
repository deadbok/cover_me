#!/usr/bin/env python3
"""
Save word association statistics as JSON data
"""
import re
import sys
import json
import random
from collections import OrderedDict


def markov_gen(start_word=None, newline=False, n_words=1, corpus=None):
    if corpus is None:
        exit('No word corpus.')

    if start_word is None:
        last_word = random.choice(list(corpus.keys()))
    else:
        last_word = start_word

    if newline:
        capitalize = True
    else:
        capitalize = False

    space = False

    ret = ''

    while n_words > 0:
        if space:
            ret = ' '
        if newline:
            ret = '\n'

        if last_word is None:
            last_word = random.choice(list(corpus.keys()))
            if capitalize:
                last_word = last_word.capitalize()
                capitalize = False
            ret += last_word
            space = True
            n_words -= 1

        if last_word != '':
            # Use the corpus if the word is in there.
            if last_word in corpus.keys():
                # Good thing nobody is ever going to see this.
                word_dict = OrderedDict(sorted(corpus[last_word].items(),
                                               key=lambda x: x[1]))
                word_list = list(word_dict.keys())
                word_list.reverse()
                widx = random.randint(0, len(word_dict) - 1)
                word = word_list[widx]
                if capitalize:
                    word = word.capitalize()
                    capitalize = False
                if '\n' in word:
                    if word.strip('\n') not in ',.?!':
                        space = True
                    if word != ',':
                        capitalize = True

                    ret += word
                    last_word = None
                    n_words -= 1
                else:
                    if word not in ',.?!':
                        space = True
                    elif word in '.!?':
                        capitalize = True
                    ret += word
                    last_word = word
                    n_words -= 1
            else:
                last_word = None

        else:
            last_word = None
    return(ret)


def main():
    """
    Create a dictionary of word associations for later use in a markov
    generator and save it as a file.
    """
    print('')
    # Load JSON Markov seed corpus.
    with open("words.json") as corpus_file:
        corpus = json.load(corpus_file)

    if len(sys.argv) > 1:
        # Load a template file.
        with open(sys.argv[1]) as tpl_file:
            template = tpl_file.read()
    else:
        # Default to creating something in the form of "Moonage daydream".
        template = "{2}\n\n{3},{6}\n{4},{9}\n{4}\n{7}\n{8}\n\n"
        template += "{7}\n{\6}\n{\7},{1}\n{8}!\n\n"
        template += "{4},{6}\n{4},{1}\n{7}\n,{3},{6}\n{6}\n\n"
        template += "{7}\n{\6}\n{\7},{1}\n{8}!\n\n"
        template += "{2}\n{2}\n{2}\n"

    if len(sys.argv) > 2:
        # Load a text file of words to use with the Markov seed corpus.
        with open(sys.argv[2]) as word_file:
            words = word_file.read().split()
    else:
        words = None

    text = ''
    newline = False

    for tpl_token in re.findall(r'\w+|\n|{\d}| ', template):
        # Not a template command token.
        if '{' in tpl_token:
            n_words = int(tpl_token.strip('{}'))
            text += markov_gen(None, newline, n_words, corpus)
            newline = False
        elif tpl_token == '\n':
            newline = True
            text += tpl_token
        else:
            text += tpl_token
            newline = False

    print(text)

if __name__ == '__main__':
    main()
