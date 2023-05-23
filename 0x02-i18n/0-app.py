#!/usr/bin/env python3
"""Basic Flask app
"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ Returns template"""
    return render_template('index.html')
