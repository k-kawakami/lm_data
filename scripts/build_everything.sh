mkdir ../br
mkdir ../ctb
mkdir ../ptb
mkdir ../ptb_mikolov
mkdir ../icwb2
mkdir ../wikitext

python build_brent.py -d ../br 
python remove_oov_sentences.py -t ../br/br-phono/tr.txt -e ../br/br-phono/va.txt
python remove_oov_sentences.py -t ../br/br-phono/tr.txt -e ../br/br-phono/te.txt
python remove_oov_sentences.py -t ../br/br-text/tr.txt -e ../br/br-text/va.txt
python remove_oov_sentences.py -t ../br/br-text/tr.txt -e ../br/br-text/te.txt

python build_ctb.py -d ../ctb
python remove_oov_sentences.py -t ../ctb/tr.txt -e ../ctb/va.txt
python remove_oov_sentences.py -t ../ctb/tr.txt -e ../ctb/te.txt

python build_ptb.py -d ../ptb
python remove_oov_sentences.py -t ../ptb/tr.txt -e ../ptb/va.txt
python remove_oov_sentences.py -t ../ptb/tr.txt -e ../ptb/te.txt

python build_ptb_mikolov.py -d ../ptb_mikolov
python remove_oov_sentences.py -t ../ptb_mikolov/tr.txt -e ../ptb_mikolov/va.txt
python remove_oov_sentences.py -t ../ptb_mikolov/tr.txt -e ../ptb_mikolov/te.txt

python build_icwb2.py -d ../icwb2
python remove_oov_sentences.py -t ../icwb2/as/tr.txt -e ../icwb2/as/va.txt
python remove_oov_sentences.py -t ../icwb2/as/tr.txt -e ../icwb2/as/te.txt

python remove_oov_sentences.py -t ../icwb2/cityu/tr.txt -e ../icwb2/cityu/va.txt
python remove_oov_sentences.py -t ../icwb2/cityu/tr.txt -e ../icwb2/cityu/te.txt

python remove_oov_sentences.py -t ../icwb2/msr/tr.txt -e ../icwb2/msr/va.txt
python remove_oov_sentences.py -t ../icwb2/msr/tr.txt -e ../icwb2/msr/te.txt

python remove_oov_sentences.py -t ../icwb2/pku/tr.txt -e ../icwb2/pku/va.txt
python remove_oov_sentences.py -t ../icwb2/pku/tr.txt -e ../icwb2/pku/te.txt

python build_wikitext.py -d ../wikitext
perl remove-bom.pl ../wikitext/wikitext-2-raw/wiki.train.raw > ../wikitext/wikitext-2-raw/wiki.train.raw-nobom
mv ../wikitext/wikitext-2-raw/wiki.train.raw-nobom ../wikitext/wikitext-2-raw/wiki.train.raw
python build-character-set.py ../wikitext/wikitext-2-raw/wiki.train.raw > ../wikitext/wikitext-2-raw/valid_chars.txt
python remove-oov-characters.py ../wikitext/wikitext-2-raw/valid_chars.txt ../wikitext/wikitext-2-raw/*.raw
cp ../wikitext/wikitext-2-raw/wiki.train.raw ../wikitext/wikitext-2-raw/tr.txt
cp ../wikitext/wikitext-2-raw/wiki.valid.raw ../wikitext/wikitext-2-raw/va.txt
cp ../wikitext/wikitext-2-raw/wiki.test.raw ../wikitext/wikitext-2-raw/te.txt

perl remove-bom.pl ../wikitext/wikitext-103-raw/wiki.train.raw > ../wikitext/wikitext-103-raw/wiki.train.raw-nobom
mv ../wikitext/wikitext-103-raw/wiki.train.raw-nobom ../wikitext/wikitext-103-raw/wiki.train.raw
python build-character-set.py ../wikitext/wikitext-103-raw/wiki.train.raw > ../wikitext/wikitext-103-raw/valid_chars.txt
python remove-oov-characters.py ../wikitext/wikitext-103-raw/valid_chars.txt ../wikitext/wikitext-103-raw/*.raw
cp ../wikitext/wikitext-103-raw/wiki.train.raw ../wikitext/wikitext-103-raw/tr.txt
cp ../wikitext/wikitext-103-raw/wiki.valid.raw ../wikitext/wikitext-103-raw/va.txt
cp ../wikitext/wikitext-103-raw/wiki.test.raw ../wikitext/wikitext-103-raw/te.txt
