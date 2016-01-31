#!/usr/bin/env python3
"""
Save word association statistics as JSON data

:copyright: (c) 2016 by Martin Grønholdt.
:license: GPLv3, see LICENSE for more details.
"""
import sys
import json
import re
import argparse


__version__ = '0.0.4'


def main():
    """
    Create a dictionary of word associations for later use in a markov
    generator and save it as a file.
    """
    # Parse command line
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-o", "--output", type=argparse.FileType('w'),
                            dest="outfile", default=None,
                            help="Write output to a this file.")
    arg_parser.add_argument("-v", "--verbose",
                            action="store_true", dest="verbose", default=False,
                            help="Be verbose.")
    arg_parser.add_argument("corpusfile", type=argparse.FileType('r'),
                            help="Text file to process.")
    args = arg_parser.parse_args()
    n_words = 0
    n_lines = 0
    words = dict()
    prev = None
    text = ''

    if args.corpusfile is None:
        exit('Error reading input file.')

    # Read text input.
    text += args.corpusfile.read().lstrip()

    # Isolate tokens and run through them.
    for word in re.findall(r'[\w\']+[-\w+]*\n?|\.\n?|\,\n?|!\n?|\?\n?', text):
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
                        if args.verbose:
                            print('.', end='')
                    else:
                        # No new line, just save the current word.
                        prev = word
                elif '\n' not in word:
                    # No previous word use current.
                    prev = word

    # Save as JSON.
    if args.outfile is not None:
        json.dump(words, args.outfile, ensure_ascii=False, indent=4,
                  sort_keys=True)
    else:
        print(json.dumps(words, ensure_ascii=False, indent=4,
                         sort_keys=True))

    if args.verbose:
        print("Total lines found: " + str(n_lines))
        print("Total words found: " + str(n_words))

if __name__ == '__main__':
    main()
