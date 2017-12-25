import sys

if len(sys.argv) < 3:
  sys.stderr.write('Usage: {} character-set.txt file1.txt [file2.txt ...]\n'.format(sys.argv[0]))
  sys.exit(1)

# This is that weird question mark character.
replacement_character = u'\uFFFD'
cset = sys.argv[1]
with open(cset, 'r') as f:
  line = f.read()
  chars = set(list(unicode(line, 'utf8')))

for text_infile in sys.argv[2:]:
  text_outfile = text_infile + '.unk'
  with open(text_infile, 'r') as inf:
    with open(text_outfile, 'w') as outf:
      for line in inf:
        t = [c if c in chars else replacement_character for c in unicode(line, 'utf8')]
        outf.write(''.join(t).encode('utf8'))
