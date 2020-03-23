import os
import pickle
import math
from flask import Flask,render_template,request,url_for,send_file
from io import BytesIO
import flask
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasAgg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import jinja2
from random import randint
import seaborn as sns
plt.style.use('ggplot')
app = Flask(__name__,static_url_path="/static/")
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('static')
])
app.jinja_loader = my_loader
df=pd.read_csv("visual.csv")
df1 = df.sort_values(by=['rating'] , ascending=False).copy()
zomato=pd.read_csv("zm.csv")
app=Flask(__name__,static_url_path="/static/")


def sortdic(x): #Used to sort the values in the dictionary
    dc={}
    for key in sorted(x):
        dc[key]=x[key]
    return dc

def get_cuisines(): #Used to pass the sorted, encoded version of cuisine to the web page
    cui={'North Indian': 0,
        'Chinese': 1,
        'Cafe': 2,
        'South Indian': 3,
        'Pizza': 4,
        'Italian': 5,
        'Bakery': 6,
        'Biryani': 7,
        'Street Food': 8,
        'Burger': 9,
        'Fast Food': 10,
        'Ice Cream': 11,
        'Healthy Food': 12,
        'Asian': 13,
        'Desserts': 14,
        'Goan': 15,
        'Continental': 16,
        'Seafood': 17,
        'Beverages': 18,
        'Mithai': 19,
        'Mangalorean': 20,
        'Rolls': 21,
        'Andhra': 22,
        'Thai': 23,
        'Salad': 24,
        'Bengali': 25,
        'Arabian': 26,
        'BBQ': 27,
        'Vietnamese': 28,
        'Juices': 29,
        'Mexican': 30,
        'Sandwich': 31,
        'Tibetan': 32,
        'Tea': 33,
        'Momos': 34,
        'Mughlai': 35,
        'Finger Food': 36,
        'Kebab': 37,
        'American': 38,
        'Kerala': 39,
        'Oriya': 40,
        'Bohri': 41,
        'African': 42,
        'Rajasthani': 43,
        'Hyderabadi': 44,
        'Maharashtrian': 45,
        'Tamil': 46,
        'Roast Chicken': 47,
        'Gujarati': 48,
        'South American': 49,
        'Konkan': 50,
        'Drinks Only': 51,
        'Awadhi': 52,
        'European': 53,
        'Japanese': 54,
        'Turkish': 55,
        'Modern Indian': 56,
        'Bihari': 57,
        'Lebanese': 58,
        'Australian': 59,
        'Mediterranean': 60,
        'Chettinad': 61,
        'Steak': 62,
        'Spanish': 63,
        'Portuguese': 64,
        'Parsi': 65,
        'Nepalese': 66,
        'Burmese': 67,
        'North Eastern': 68,
        'Lucknowi': 69,
        'Korean': 70,
        'Malaysian': 71,
        'Sushi': 72,
        'Kashmiri': 73,
        'French': 74,
        'Assamese': 75,
        'Coffee': 76,
        'Charcoal Chicken': 77,
        'Singaporean': 78,
        'Middle Eastern': 79,
        'Naga': 80,
        'Belgian': 81,
        'Russian': 82,
        'Iranian': 83,
        'Bar Food': 84,
        'German': 85,
        'British': 86}
    cui=sortdic(cui)
    return cui

def get_locations(): #Used to pass the sorted, encoded version of location to the web page
    loc={'Banashankari': 0,
        'Bannerghatta Road': 1,
        'Basavanagudi': 2,
        'Bellandur': 3,
        'Brigade Road': 4,
        'Brookefield': 5,
        'BTM': 6,
        'Church Street': 7,
        'Electronic City': 8,
        'Frazer Town': 9,
        'HSR': 10,
        'Indiranagar': 11,
        'Jayanagar': 12,
        'JP Nagar': 13,
        'Kalyan Nagar': 14,
        'Kammanahalli': 15,
        'Koramangala 4th Block': 16,
        'Koramangala 5th Block': 17,
        'Koramangala 6th Block': 18,
        'Koramangala 7th Block': 19,
        'Lavelle Road': 20,
        'Malleshwaram': 21,
        'Marathahalli': 22,
        'MG Road': 23,
        'New BEL Road': 24,
        'Old Airport Road': 25,
        'Rajajinagar': 26,
        'Residency Road': 27,
        'Sarjapur Road': 28,
        'Whitefield': 29}
    loc=sortdic(loc)
    return loc

def get_type(): #Used to pass the sorted, encoded version of restaurant type to the web page
    tp={'Casual Dining': 0,
        'Cafe': 1,
        'Quick Bites': 2,
        'Delivery': 3,
        'Mess': 4,
        'Dessert Parlor': 5,
        'Bakery': 6,
        'Pub': 7,
        'Takeaway': 8,
        'Fine Dining': 9,
        'Beverage Shop': 10,
        'Sweet Shop': 11,
        'Bar': 12,
        'Confectionery': 13,
        'Kiosk': 14,
        'Food Truck': 15,
        'Microbrewery': 16,
        'Lounge': 17,
        'Food Court': 18,
        'Dhaba': 19,
        'Club': 20,
        'Bhojanalya': 21,
        'Pop Up': 22}
    tp=sortdic(tp)
    return tp


@app.route('/')
@app.route('/home',methods=['GET','POST']) #homepage
def home():  
    return flask.render_template('main.html')

@app.route('/basic_graph',methods=['GET','POST'])
def basic_graph():
    return flask.render_template('home.html')

@app.route('/dynamic_des',methods=['GET','POST'])
def dynamic_des():
    if request.method=='POST':
        return flask.render_template('dynamic_des.html')  
    return flask.render_template('dynamic_des.html')

@app.route('/form_des',methods=['GET','POST'])
def form_des():
    if request.method=='POST':
        return flask.render_template('form_des.html')  
    return flask.render_template('form_des.html')

@app.route('/analysis',methods=['GET','POST'])
def analysis():
    if request.method=='POST':
        return flask.render_template('analysis.html')  
    return flask.render_template('analysis.html')

@app.route('/analyse',methods=['GET','POST'])
def analyse():
    if request.method=='POST':
        return flask.render_template('analyse.html')  
    return flask.render_template('analyse.html')

@app.route('/analysed',methods=['GET','POST'])
def analysed():
    if request.method=='POST':
        data = flask.request.form
        print(data)
        d=list(data.values())
        print(d)
        column_1 = zomato[d[0]]
        column_2 = zomato[d[1]]
        cor=0.0
        cor = column_1.corr(column_2)
        cor=round(cor,4)
        print(cor)
        if cor>0:
            if cor>0.2:
                al="These exhibits a strong positive correlation"
            if cor<0.2:
                al="These exhibits a weak positive correlation"
        else:
            if cor>(-0.31):
                al="These exhibits strong negative correlation"
            if cor<(-0.31):
                al="These exhibits weak negative correlation"
        return flask.render_template('analysed.html',corr=cor,al=al)  
    return flask.render_template('analysed.html')

@app.route('/grp')
def grp():
    return flask.render_template('grp.html')


@app.route('/form',methods=['GET','POST']) #Form used to get values which is used for prediction
def form():
    if request.method == 'GET':
        data = flask.request.form
        return flask.render_template('results.html',data=data)
    if request.method == 'POST':
        return flask.render_template('form.html',cuisines=get_cuisines(),restype=get_type(),location=get_locations())
    return flask.render_template('form.html',cuisines=get_cuisines(),restype=get_type(),location=get_locations())

def ValuePredictor(to_predict_list):
    md=pickle.load(open("/home/vaishnavi/Downloads/etree1.pkl","rb"))
    res=md.predict(to_predict_list)
    return (res[0])

@app.route('/graph1/') #general graph
def graph1(dt):
    print(dt)
    yaxis = dt[1]
    xaxis = dt[0]
    plt.figure(figsize=(dt[2],dt[3]))
    sns.set(font_scale = 2)
    if dt[5]!=100:
        c = dt[5]
    else:
        c=len(df)
    sns.set(font_scale = 2) 
    fig = sns.barplot(x=xaxis,y=yaxis, data= df1[:c])
    fig.set_xlabel(xaxis ,fontsize=dt[4])
    fig.set_ylabel(yaxis ,fontsize=dt[4])
    im=randint(0,50)
    fn='gr1'+str(im)+'.jpg'
    plt.savefig('/home/vaishnavi/ZAAR/static/'+fn)
    return(fn)

@app.route('/homepage')
def about():
    return flask.render_template('homepage.html')


@app.route('/results',methods=['GET','POST']) #Prediction and recommendation
def results():
    if request.method == 'POST':
        data = flask.request.form
        dt=[]
        d=data.values()
        dt=list(d)
        l=len(dt)
        for i in range(0,len(dt)):
            if i==5:
                dt[i]=float(dt[i])
            else:
                dt[i]=int(dt[i])
        res=ValuePredictor([dt])
        print(res)
        print(dt)
        res=round(res,2)
        feasibility = float((res/5)*100)
        feasibility = round(feasibility,2)
        def getkey(my_dict,val):
            key_list = list(my_dict.keys()) 
            val_list = list(my_dict.values()) 
            print(key_list[val_list.index(val)])
            return(key_list[val_list.index(val)])
        cui=get_cuisines()
        tp=get_type()
        loc=get_locations()
        d=[]
        vl=getkey(tp,dt[2])
        d.append(vl)
        vl=getkey(cui,dt[3])
        d.append(vl)
        vl=getkey(loc,dt[5])
        d.append(vl)
        print(d)
        recc=[]
        cuis = df['cuisines']==d[1]
        ty = df['rest_type']==d[0]  
        loc = df['location'] == d[2]

        #printing out the maximum count of occurences of cuisine in a particular location 
        lc=df[cuis]['location'].max()
        recc.append(lc)
        #printing out the maximum count of occurences of restaurant type based on cuisine and location
        rcl=df[loc & cuis & ty]['cost'].mean()
        print(rcl)
        if math.isnan(rcl):
            rcl=0
        else:
            rcl=round(rcl,1)
        recc.append(rcl)
        #printing out the maximum count of occurences of restaurant type based on location
        rl=df[loc]['rest_type'].max()
        recc.append(rl)
        print(recc)
        return flask.render_template('results.html',data=data,res=res,feasibility=feasibility,recc=recc)
    return flask.render_template('index.html')        

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    return flask.render_template('prediction.html')


@app.route('/dynamic',methods=['POST','GET'])
def dynamic():
    if request.method == 'POST':
        flask.render_template('show_dynamic.html')
    return flask.render_template('dynamic.html')

@app.route('/show_dynamic',methods=['POST','GET'])
def show_dynamic():
    if request.method == 'POST':
        data = flask.request.form
        dt = []
        dt=list(data.values())
        print("data in a list")
        for i in range(2,len(dt)):
            dt[i]=int(dt[i])
        print(dt)
        x=graph1(dt)
        print(type(x))
        print(x)
        return flask.render_template('show_dynamic.html',x=x)
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
 

