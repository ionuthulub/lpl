import codecs
import sys

from nltk.tokenize import moses
import xml


def get_tokens():
    tree = xml.etree.ElementTree.parse(sys.argv[1])
    root = tree.getroot()
    tokens = []
    for w in root.iter('w'):
        tokens.append(w.text)
    return tokens


def main():
    tokens = get_tokens()
    output = moses.MosesDetokenizer().detokenize(tokens, return_str=True)
    with codecs.open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(output)


if __name__ == '__main__':
    main()
