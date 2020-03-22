# COVID-19 Rasa Chatbot


### Getting started

Set-up
```
./install.sh
```

### 1. Run Rasa
```
rasa run actions
rasa shell
```

### 2. Run Rasa API
```
rasa run actions
rasa run -m models --enable-api --log-file out.log
```
Test
```
curl -X POST \
  http://localhost:5005/model/parse \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 434d91fe-d8cc-3f21-e751-ed223db2509e' \
  -d '{
  "text": "how many persons are infected in germany"
}'
```

### Making changes
```
rasa train
rasa run actions
rasa shell
```
