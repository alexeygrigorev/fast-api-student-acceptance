import pickle

from fastapi import FastAPI


model_file = './artifacts/pipeline.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)


app = FastAPI()



@app.post('/predict')
async def predict(student: dict):
    y_pred = pipeline.predict_proba(student)[0, 1]
    admission = y_pred >= 0.5

    result = {
        'admission_probability': float(y_pred),
        'admission': bool(admission)
    }

    return result