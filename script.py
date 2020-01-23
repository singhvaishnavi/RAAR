import os
import flask
import pickle
from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
@app.route('/form')
def form():
    return flask.render_template('form.html')

@app.route('/home')
def home():
    return flask.render_template('home.html')
