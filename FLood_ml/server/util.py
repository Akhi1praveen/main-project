import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

__data_columns = None
__model = None

def predict_flood(Rainfall , Temperature, Humidity ,River_Discharge, Water_Level, Elevation, Historical_Floods):
    v = np.zeros(len(__data_columns))
    v[0]=Rainfall
    v[1]=Temperature
    v[2]=Humidity
    v[3]=River_Discharge
    v[4]=Water_Level
    v[5]=Elevation
    v[6]=Historical_Floods
    return round(__model.predict([v])[0],2)


def load_artifacts():
    print("loading server artifacts...start")
    global __data_columns
    global __model
    with open("./artifacts/flood_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open("./artifacts/flood_predict.pickle","rb") as f:
        __model=pickle.load(f)
    print("loading server artifacts...done")


if __name__ == "__main__":
    load_artifacts()
    print(predict_flood(349, 29, 60, 590, 1.5, 1600, 1))
