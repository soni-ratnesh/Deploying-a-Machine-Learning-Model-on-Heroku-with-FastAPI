"""
Heroku Api test script
"""
import requests


data = {
    "age": 22,
    "workclass": "Private",
    "education": "Some-college",
    "maritalStatus": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "hoursPerWeek": 80,
    "nativeCountry": "United-States"
    }
r = requests.post('https://cdudacity.herokuapp.com/', json=data)

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())
