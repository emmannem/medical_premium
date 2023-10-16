from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware

app = FastAPI(title='Medical Insurance Premium Prediction')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load(pathlib.Path('model/medical-premium-v1.joblib'))


class InputData(BaseModel):
    age: int = 20
    diabetes: int = 0
    bloodpressureproblems: int = 0
    anytransplants: int = 0
    anychronicdiseases: int = 1
    height: int = 177
    weight: int = 87
    knownallergies: int = 1
    historyofcancerinfamily: int = 0
    numberofmajorsurgeries: int = 0


class OutputData(BaseModel):
     premiumPrice: float = 15000


@app.post('/predict', response_model=OutputData)
def predict(data: InputData):
    model_input = np.array([v for k, v in data.dict().items()]).reshape(1, -1)
    predicted_price = model.predict(model_input)
    result = predicted_price[0]

    return {'premiumPrice': result}
