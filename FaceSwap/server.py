import os
from flask import Flask, request
from subprocess import call
import overlay.py
app = Flask(__name__)

@app.route('/rec',methods=['POST'])
def rec():
	file=request.files['file']
	file.save


