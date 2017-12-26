import codecs
import math
import os
import subprocess


def download(ptb_dir):
    if os.path.exists('{}/ptb_mikolov'.format(ptb_dir)):
        print 'nothing to download'
        return True
    else:
        print 'downloading'
        try:
            subprocess.call(['wget', '-P', ptb_dir, 'https://s3.eu-west-2.amazonaws.com/k-kawakami.com/lm/ptb_mikolov.zip'])
            subprocess.call(['unzip', '{}/ptb_mikolov.zip'.format(ptb_dir), '-d', ptb_dir])
            subprocess.call(['rm', '{}/ptb_mikolov.zip'.format(ptb_dir)])
            subprocess.call(['mv', '{}/ptb_mikolov/char'.format(args.d), '{}'.format(args.d)])
            subprocess.call(['mv', '{}/ptb_mikolov/word'.format(args.d), '{}'.format(args.d)])
            subprocess.call(['rm', '-r', '{}/ptb_mikolov'.format(args.d)])
            return True
        except:
            return False

def load_data(file_name):
    f = codecs.open(file_name, 'r', 'utf_8_sig')
    sentences = []
    for line in f:
        sentence = ''.join(line.strip().split()).replace('_',' ')
        sentences.append(sentence)
    return sentences

def write_file(file_name, sentences):
    f = codecs.open(file_name, 'w', 'utf8')
    for sentence in sentences:
        f.write(sentence + '\n')
    f.close()

if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, required=True, help='corpus dir')
    args = parser.parse_args()
    
    success = download(args.d) 
