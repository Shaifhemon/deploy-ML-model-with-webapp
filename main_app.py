import numpy as np
from flask_ngrok import run_with_ngrok
from flask import Flask, request, render_template, redirect, url_for
import pickle
from googletrans import Translator

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getspeech',methods=['POST'])
def getspeech():    

    input =  request.form["text"]
    translator = Translator()
    ar = translator.translate(input, dest='bn').text

    return render_template('index.html', output='your text :{}'.format(ar))

if __name__ == "__main__":
    app.run()
