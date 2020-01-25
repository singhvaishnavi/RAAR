import os
import flask
import pickle
from flask import Flask,render_template,request,url_for
app=Flask(__name__,static_url_path="/static")


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return flask.render_template('form.html')
    return flask.render_template('results.html')

@app.route('/home',methods=['POST','GET'])
def home():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
 

