# COVID-19 Rasa Chatbot

![COVID-19 Rasa Telegram Demo](https://github.com/e-tony/COVID-QA.gif)


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

### 2. Run Rasa bot
```
rasa run actions
rasa run
```

### 3. Run Rasa API
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


### Where Does Our Data Come From? 🌍
[COVID-QA](https://github.com/deepset-ai/COVID-QA)

[Coronavirus Tracker API](https://github.com/ExpDev07/coronavirus-tracker-api)
