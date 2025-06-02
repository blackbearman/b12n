wget https://github.com/Belarus/GrammarDB/releases/download/RELEASE-202309/RELEASE-20230920.zip
mkdir dict
unzip RELEASE-20230920.zip -d dict

mkdir dict/adv
python3 scripts/reversed.py dict/spellchecker/slovy-2008.txt dict/adv/slovy_adv.txt
python3 scripts/reversed.py dict/spellchecker/slovy-2008-stress.txt dict/adv/slovy-stress-adv.txt
