#!/usr/bin/env python3
"""
Save word association statistics as JSON data
"""
import sys
import json
import re


def main():
    """
    Create a dictionary of word associations for later use in a markov
    generator and save it as a file.
    """
    n_words = 0
    n_lines = 0
    words = dict()
    prev = None
    text = ''

    # Open text input.
    if len(sys.argv) > 1:
        for filename in sys.argv[1:-1]:
            with open(filename) as txt_file:
                text += txt_file.read().lstrip()
    else:
        print("Please add some input files on the command line.")
        exit(1)

    # Isolate tokens and run through them.
    for word in re.findall(r'[\w\']+\n?|\.\n?|\,\n?|!\n?|\?\n?', text):
        if word is not None:
            # Get rid of some characters that mostly messes things up.
            word = word.lower().strip('"()* ')
            if word != "":
                # Ignore first word.
                if prev is not None:
                    # If base token is not there, create it.
                    if prev not in words:
                        words[prev] = dict()
                    # token is not there, create it.
                    if word not in words[prev]:
                        words[prev][word] = 0

                    # Increase occurrence count.
                    words[prev][word] += 1

                    n_words += 1
                    # Handle line ends.
                    if '\n' in word:
                        # Don't link to last word of previous line.
                        prev = None
                        n_lines += 1
                        print('.', end='')
                    else:
                        # No new line, just save the current word.
                        prev = word
                elif '\n' not in word:
                    # No previous word use current.
                    prev = word

    print('\n')
    # Save as JSON.
    with open("words.json", mode="w") as word_file:
        json.dump(words, word_file, ensure_ascii=False, indent=4,
                  sort_keys=True)

    print("Total lines found: " + str(n_lines))
    print("Total words found: " + str(n_words))

if __name__ == '__main__':
    main()
