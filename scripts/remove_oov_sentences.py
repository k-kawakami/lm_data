'''A script to remove sentences with OOV characters.

Usage: python remove_oov_sentences.py -t tr.txt -e va.txt
'''
import codecs


def build_vocab(file_name):
    f = codecs.open(file_name, 'r', 'utf_8_sig')
    vocab = set()
    for line in f:
        words = line.split()
        for word in words:
            for char in word:
                vocab.add(char)
    f.close()
    return vocab

def remove_oov_sentences(file_name, vocab):
    ''' Screen out sentences with ooc words.
    '''
    removed = 0
    f = codecs.open(file_name, 'r', 'utf_8_sig')
    sentences = []
    for i, line in enumerate(f):
        no_ooc = True
        words = line.split()
        for word in words:
            for char in word:
                if char not in vocab:
                    no_ooc = False
        if no_ooc:
            sentences.append(line)
        else:
            removed += 1
            #print "Removing sentence num.{}: {}".format(i, line.strip().encode('utf-8'))

    print '{} sentences (removed {} sentences)'.format(len(sentences), removed)
    f.close()
    return sentences

def write_file(file_name, sentences):
    f = codecs.open(file_name, 'w', 'utf_8_sig')
    for sentence in sentences:
        f.write(sentence)
    f.close()


if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=str, required=True, help='training corpus')
    parser.add_argument('-e', type=str, required=True, help='evaluation corpus')
    args = parser.parse_args()

    vocab = build_vocab(args.t)
    screened_sentences = remove_oov_sentences(args.e, vocab)
    write_file(args.e, screened_sentences)
