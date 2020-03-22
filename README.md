# COVID-19 Rasa Chatbot


### Getting started

Set-up
```
git clone https://github.com/e-tony/COVID-19-Rasa
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
```


Start rasa
```
rasa run actions
rasa shell
```

### Making changes
```
rasa train
rasa run actions
rasa shell
```
