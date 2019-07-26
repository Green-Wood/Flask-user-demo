import requests

data = {
    'instances': [1, 2, 3]
}
res = requests.post('http://localhost:8501/v1/models/half_plus_two:predict', json=data)

print(res.json())