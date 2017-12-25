import codecs
import math
import os
import subprocess


def download(iwcb2_dir):
    if os.path.exists('{}/icwb2-data'.format(iwcb2_dir)):
        print 'nothing to download'
        return True
    else:
        print 'downloading'
        try:
            subprocess.call(['wget', '-P', iwcb2_dir, 'http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip'])
            subprocess.call(['unzip', '{}/icwb2-data.zip'.format(iwcb2_dir), '-d', iwcb2_dir])
            subprocess.call(['rm', '{}/icwb2-data.zip'.format(iwcb2_dir)])
            return True
        except:
            return False

def load_data(file_name):
    f = codecs.open(file_name, 'r', encoding='utf_8_sig')
    sentences = []
    for line in f:
        sentence = ' '.join(line.strip().split())
        sentences.append(sentence)
    return sentences

def write_file(file_name, sentences):
    f = codecs.open(file_name, 'w', encoding='utf8')
    for sentence in sentences:
        f.write(sentence + '\n')
    f.close()

def train_valid_split(data, ratio):
    tr_size = int(math.ceil(len(data) * ratio))
    return data[:tr_size], data[tr_size:]


if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, required=True, help='icwb2 dir')
    parser.add_argument('-r', type=float, default=0.9, help='train/valid split ratio (default=0.9)')
    args = parser.parse_args()
    
    success = download(args.d) 

    if success:
        datasets = ['as', 'cityu', 'msr', 'pku']
        for dataset in datasets:
            subprocess.call(['mkdir', '-p', '{}/{}'.format(args.d, dataset)])

            tr_sentences = load_data('{}/icwb2-data/training/{}_training.utf8'.format(args.d, dataset))
            tr_sentences, va_sentences = train_valid_split(tr_sentences, args.r)

            if dataset == 'as':
                te_sentences = load_data('{}/icwb2-data/gold/{}_testing_gold.utf8'.format(args.d, dataset))
            else:
                te_sentences = load_data('{}/icwb2-data/gold/{}_test_gold.utf8'.format(args.d, dataset))

            # Write
            tr_file = '{}/{}/tr.txt'.format(args.d, dataset)
            va_file = '{}/{}/va.txt'.format(args.d, dataset)
            te_file = '{}/{}/te.txt'.format(args.d, dataset)
            write_file(tr_file, tr_sentences)
            write_file(va_file, va_sentences)
            write_file(te_file, te_sentences)
