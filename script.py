import os
import flask
import pickle
from flask import Flask,render_template,request,url_for
app=Flask(__name__,static_url_path="/static")


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
"""
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("etree.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
"""
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        return flask.render_template('result.html')
    return flask.render_template('form.html')

@app.route('/result',methods=['GET','POST'])
def result():

    """
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
    prediction=str(result)
    """
    if request.method == 'GET':
        prediction="prediction"
        return flask.render_template('result.html',prediction=prediction)
    return flask.render_template('index.html')        

@app.route('/home',methods=['POST','GET'])
def home():
    return flask.render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
 

