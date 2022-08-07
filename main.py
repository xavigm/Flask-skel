from flask import Flask, render_template, request, redirect
import threading

from waitress import serve


app = Flask(__name__, static_folder='')
@app.route('/')
def index():

        templateData = {
        'title': 'Text',
    }

        return render_template('index.html', **templateData)

# app.run() ##Replaced with below code to run it using waitress
serve(app, host='127.0.0.1', port=80)  
    