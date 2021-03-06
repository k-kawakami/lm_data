import codecs
import math
import os
import subprocess


def download(target_dir):
    if os.path.exists('{}/wikitext'.format(target_dir)):
        print 'nothing to download'
        return True
    else:
        print 'downloading'
        try:
            subprocess.call(['wget', '-P', target_dir, 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-v1.zip'])
            subprocess.call(['unzip', '{}/wikitext-2-v1.zip'.format(target_dir), '-d', target_dir])
            subprocess.call(['rm', '{}/wikitext-2-v1.zip'.format(target_dir)])
            subprocess.call(['wget', '-P', target_dir, 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-v1.zip'])
            subprocess.call(['unzip', '{}/wikitext-103-v1.zip'.format(target_dir), '-d', target_dir])
            subprocess.call(['rm', '{}/wikitext-103-v1.zip'.format(target_dir)])

            subprocess.call(['wget', '-P', target_dir, 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-raw-v1.zip'])
            subprocess.call(['unzip', '{}/wikitext-2-raw-v1.zip'.format(target_dir), '-d', target_dir])
            subprocess.call(['rm', '{}/wikitext-2-raw-v1.zip'.format(target_dir)])
            subprocess.call(['wget', '-P', target_dir, 'https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-raw-v1.zip'])
            subprocess.call(['unzip', '{}/wikitext-103-raw-v1.zip'.format(target_dir), '-d', target_dir])
            subprocess.call(['rm', '{}/wikitext-103-raw-v1.zip'.format(target_dir)])
            return True
        except:
            return False

def load_data(file_name):
    f = codecs.open(file_name, 'r', 'utf_8_sig')
    sentences = []
    for line in f:
        sentence = ' '.join(line.strip().split())
        sentences.append(sentence)
    return sentences

def write_file(file_name, sentences):
    f = codecs.open(file_name, 'w', 'utf_8')
    for sentence in sentences:
        f.write(sentence + '\n')
    f.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, required=True, help='corpus dir')
    args = parser.parse_args()
    
    success = download(args.d) 
    #tr_sentences = load_data('{}/ptb/train_all_sents_raw.txt'.format(args.d))
    #va_sentences = load_data('{}/ptb/dev_sents_raw.txt'.format(args.d))
    #te_sentences = load_data('{}/ptb/test_sents_raw.txt'.format(args.d))

    ## Write
    #tr_file = '{}/tr.txt'.format(args.d)
    #va_file = '{}/va.txt'.format(args.d)
    #te_file = '{}/te.txt'.format(args.d)
    #write_file(tr_file, tr_sentences)
    #write_file(va_file, va_sentences)
    #write_file(te_file, te_sentences)
