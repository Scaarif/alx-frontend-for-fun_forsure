#!/usr/bin/python3
""" Takes as argument 2 strings, the name of Markdown file
    and the output file name respectively.
    Requirements:
        - if the number of args < 2 print to STDERR
        'Usage: ./markdown2html.py README.md README.html' and exit 1
        - if the Markdown file doesn't exist print in STDERR
        'Missing <filename>' and exit 1
        - otherwise, print nothing and exit 0
"""
import sys
import os


if __name__ == '__main__':
    # check the number of args
    if len(sys.argv) < 3:
        print('Usage: {} README.md README.html'.format(
            sys.argv[0]), file=sys.stderr)
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        # build html headings
        html = []
        for line in lines:
            # determine heading level and create element
            h_level = line.rfind('#')  # get last '#' index
            if h_level == 0:
                html.append('<h1>' + line[h_level + 1:].strip() + '</h1>')
            if h_level == 1:
                html.append('<h2>' + line[h_level + 1:].strip() + '</h2>')
            if h_level == 2:
                html.append('<h3>' + line[h_level + 1:].strip() + '</h3>')
            if h_level == 3:
                html.append('<h4>' + line[h_level + 1:].strip() + '</h4>')
            if h_level == 4:
                html.append('<h5>' + line[h_level + 1:].strip() + '</h5>')
            if h_level == 5:
                html.append('<h6>' + line[h_level + 1:].strip() + '</h6>')
        # print(html)
        lines = len(html)
        with open(sys.argv[2], 'a') as f:
            for idx, elem in enumerate(html):
                f.write(elem)
                # add a new line if not last line
                if idx < lines - 1:
                    f.write('\n')
    exit(0)