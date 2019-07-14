# load file with pickle
# import pickle

# with open('modelPickle.pkl','rb') as fileku:
#     model=pickle.load(fileku)

# print(model.predict([[10,2,200]]))


#  load file with joblib 
import joblib # apabila file disave/didump menggunakan joblib harus diload menggunakan joblib, apabila menggunakan scikit.joblib harus menggunakan scikit.joblib juga

model=joblib.load('modelJoblib')
print(model.predict([[10,2,200]]))