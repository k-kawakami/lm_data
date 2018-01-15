# Convert normal text to lm file format
import codecs


def load_data(file_name, remove_space):
    with codecs.open(file_name, 'r', 'utf8') as f:
        data = []
        for line in f:
            if remove_space:
                line = line.strip().replace(' ', '')
            else:
                line = line.strip().replace(' ', '_')
            data.append(' '.join(list(line)))
    return data


def write_file(file_name, data):
    with codecs.open(file_name, 'w', 'utf8') as f:
        for datum in data:
            f.write(datum + '\n')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-file_name', type=str, required=True, help='file name')
    parser.add_argument('-remove_space', action='store_true')
    args = parser.parse_args()


    data = load_data(args.file_name, args.remove_space)
    if args.remove_space:
        write_file(args.file_name + '.char.nospace', data)
    else:
        write_file(args.file_name + '.char', data)
