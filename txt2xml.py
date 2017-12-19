import codecs
import sys
import json

import nltk
import gate


def get_corpus():
    with codecs.open('corpus.txt', 'r', encoding='utf-8') as fin:
        return fin.read()


def generate_xml(tokens):
    partial_result = ''
    for i, token in enumerate(tokens):
        partial_result += u'<w id="{0}">{1}</w>'.format(i + 1, token)
    return u"""<?xml version="1.0" encoding="UTF-8"?>
<DOCUMENT>
    {0}
</DOCUMENT>""".format(partial_result)


@gate.executable
def main(document):
    # corpus = get_corpus()
    corpus = document.text
    tokens = nltk.word_tokenize(corpus)
    xml = generate_xml(tokens)
    with codecs.open('output.xml', 'w', encoding='utf-8') as fout:
        fout.write(xml)
	return document


if __name__ == '__main__':
    main.start()
