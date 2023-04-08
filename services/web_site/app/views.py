from flask import render_template
from app import app
from flask import request
from flask import json
from flask import g
from flask import Response
from flask import url_for
from flask import send_file
from pymongo import MongoClient
import pymongo

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return "Hello World"
