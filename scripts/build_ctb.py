import codecs
import math
import os
import subprocess


def download(ctb_dir):
    if os.path.exists('{}/ctb'.format(ctb_dir)):
        print 'nothing to download'
        return True
    else:
        print 'downloading'
        try:
            subprocess.call(['wget', '-P', ctb_dir, 'https://s3.eu-west-2.amazonaws.com/k-kawakami.com/lm/ctb.zip'])
            subprocess.call(['unzip', '{}/ctb.zip'.format(ctb_dir), '-d', ctb_dir])
            subprocess.call(['rm', '{}/ctb.zip'.format(ctb_dir)])
            return True
        except:
            return False

def load_data(file_name):
    f = codecs.open(file_name, 'r', encoding='utf_8_sig')
    sentences = []
    for line in f:
        sentence = ' '.join([ w.split('#')[0] for w in line.strip().split()])
        sentences.append(sentence)
    return sentences

def write_file(file_name, sentences):
    f = codecs.open(file_name, 'w', encoding='utf8')
    for sentence in sentences:
        f.write(sentence + '\n')
    f.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, required=True, help='corpus dir')
    args = parser.parse_args()
    
    success = download(args.d) 
    tr_sentences = load_data('{}/ctb/train-tagged.txt'.format(args.d))
    va_sentences = load_data('{}/ctb/dev-tagged.txt'.format(args.d))
    te_sentences = load_data('{}/ctb/test-tagged.txt'.format(args.d))

    # Write
    tr_file = '{}/tr.txt'.format(args.d)
    va_file = '{}/va.txt'.format(args.d)
    te_file = '{}/te.txt'.format(args.d)
    write_file(tr_file, tr_sentences)
    write_file(va_file, va_sentences)
    write_file(te_file, te_sentences)
