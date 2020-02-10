# Пример простейшего динамического веб-сайта на Flask




## How to train and use NN models.

1) Run the duckling container:
```console
docker-compose up
``` 

2) Train the models:
```console
rm ~/.deeppavlov/models/ner_nlp_cnn/*
rm ~/.deeppavlov/models/classifier_word_cnn/*
./nlpython/bin/python server.py train ./pipelines/ner_nlp_cnn.json
./nlpython/bin/python server.py train ./pipelines/classifier_word_cnn.json
``` 

3) Establish a connection with UI:
```console
./nlpython/bin/dramatiq app --processes 1 --threads 1
``` 
