python3 -m venv venv
source venv/bin/activate

pip3 install --upgrade pip
pip3 install testresources
pip3 install --upgrade setuptools
pip3 install --upgrade protobuf

pip3 install -r requirements.txt
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
