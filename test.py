import pickle
import joblib
"""
def ValuePredictor(to_predict_list):

    print("list in function")
    print(to_predict_list)
    loaded_model = joblib.load("etree.pkl")
    result = loaded_model.predict(to_predict_list)
    print(result[0])
    return result[0]
"""
ls=[[0, 0, 202, 6, 27, 500.0, 13]]
#res=ValuePredictor(ls)
#print (res)

md=pickle.load(open("/home/vaishnavi/Downloads/etree.pkl","rb"))
res=md.predict(ls)
print (res[0])
