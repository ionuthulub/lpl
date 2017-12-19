import codecs
import sys

import gate
from nltk.tokenize import moses
import xml


def get_tokens():
    tree = xml.etree.ElementTree.parse('output.xml')
    root = tree.getroot()
    tokens = []
    for w in root.iter('w'):
        tokens.append(w.text)
    return tokens


@gate.executable
def main(document):
    tokens = get_tokens()
    output = moses.MosesDetokenizer().detokenize(tokens, return_str=True)
    with codecs.open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(output)
	return document


if __name__ == '__main__':
    main.start()
