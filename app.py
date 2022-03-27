import numpy as np
import argparse

from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests
import json
import io
from flask_csv import send_csv
from flask import make_response
from flask import session, redirect
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

app = Flask(__name__)

def get_labels(path):
    if path:
        with open(path, "r") as f:
            labels = f.read().splitlines()
        return labels
    else:
        return ["N", "C"]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', "GET"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    print(int_features)
    sentence = int_features[0]
    if int_features[1] == 'display':
        tokenizer = AutoTokenizer.from_pretrained("bert-cwi")
        model = AutoModelForTokenClassification.from_pretrained("bert-cwi")

        nlp = pipeline("token-classification", model=model, tokenizer=tokenizer, aggregation_strategy='first')  # grouped_entities=True, ignore_subwords=True
        cwi_results = nlp(sentence)
        print(cwi_results)
        cwords = []
        for item in cwi_results:
            if item['entity_group'] == 'C':
                allwords = item['word'].split()
                for word in allwords:
                    cwords.append(word)
        return render_template('index.html', prediction_text=cwi_results, complex_words=cwords, sentence=sentence)

    # elif int_features[1] == 'getls':
    #     tokenizer = AutoTokenizer.from_pretrained("bert-cwi")
    #     model = AutoModelForTokenClassification.from_pretrained("bert-cwi")
    #
    #     predictions, raw_outputs = model.predict([sentence])
    #     l = []
    #     for i in predictions[0]:
    #         dic = {}
    #         for j in i.keys():
    #             dic['word'] = j
    #             dic['tag'] = i[j]
    #         l.append(dic)
    #     return send_csv(l, "tags.csv", ["word", "tag"])


if __name__ == "__main__":
    app.run(debug=True)