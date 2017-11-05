import codecs
import sys

import nltk


def get_corpus():
    with codecs.open(sys.argv[1], 'r', encoding='utf-8') as fin:
        return fin.read()


def generate_xml(tokens):
    partial_result = ''
    for i, token in enumerate(tokens):
        partial_result += u'<w id="{0}">{1}</w>'.format(i + 1, token)
    return u"""<?xml version="1.0" encoding="UTF-8"?>
<DOCUMENT>
    {0}
</DOCUMENT>""".format(partial_result)


def main():
    corpus = get_corpus()
    tokens = nltk.word_tokenize(corpus)
    xml = generate_xml(tokens)
    with codecs.open('output.xml', 'w', encoding='utf-8') as fout:
        fout.write(xml)


if __name__ == '__main__':
    main()
