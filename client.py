import requests
body = {
  "age": 20,
  "diabetes": 0,
  "bloodpressureproblems": 0,
  "anytransplants": 0,
  "anychronicdiseases": 1,
  "height": 177,
  "weight": 87,
  "knownallergies": 1,
  "historyofcancerinfamily": 0,
  "numberofmajorsurgeries": 0
}
response = requests.post(url='http://127.0.0.1:8000/predict',
                         json=body)
print(response.json())
# output: {'premiumPrice': 15000}
