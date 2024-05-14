from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template
from markupsafe import Markup

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
