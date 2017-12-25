import sys
import unicodedata
from collections import defaultdict

# remove characters that have fewer than MIN_COUNT examples if they are not
# present in RETAIN_CODEPAGES
MIN_COUNT = 25
RETAIN_CODEPAGES = set(['LATIN'])

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} training-data.txt\n'.format(sys.argv[0]))
  sys.exit(1)

train = sys.argv[1]
sys.stderr.write("TRAIN: {}\n".format(train))
sys.stderr.write("MINIMUM CHARACTER COUNT IS {} UNLESS CODEPAGE IS IN [{}]\n".
    format(MIN_COUNT, ', '.join(RETAIN_CODEPAGES)))
# This is that weird question mark character.
replacement_character = u'\uFFFD'
char_vocab = set([replacement_character])

char_counts = defaultdict(int)
with open(train, 'r') as f:
  chars = [char for line in f for char in unicode(line.strip(), 'utf8')]
  for char in chars:
    char_counts[char] += 1

removed = 0
oov_instances = 0
for char, count in char_counts.items():
  try:
    name = unicodedata.name(char)
  except:
    name = 'UNKNOWN'
  char_type_proxy = name.split()[0]
  if count > MIN_COUNT or char_type_proxy in RETAIN_CODEPAGES:
    char_vocab.add(char)
  else:
    removed += 1
    oov_instances += count

sys.stderr.write('REMOVED {} CHARACTER TYPES\n'.format(removed))
if oov_instances == 0:
  sys.stderr.write('WARNING! No characters were filtered. There will be no '
      'support in training data for the {} character\n'.
      format(replacement_character.encode('utf8')))
svocab = sorted(char_vocab, key=lambda x: char_counts[x],reverse=True)
vocab_str = ' '.join(svocab).encode('utf8')
sys.stderr.write('SURVIVING CHARSET: {}\n'.format(vocab_str))
sys.stderr.write('SURVIVING CHARSET SIZE: {}\n'.format(len(char_vocab)))

print ''.join(svocab).encode('utf8')

