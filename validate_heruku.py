"""
Heroku Api test script
"""
import requests

data = {
            'age': 19,
            'workclass': 'Private',
            'fnlgt': 149184,
            'education': 'HS-grad',
            'marital_status': 'Never-married',
            'occupation': 'Prof-specialty',
            'relationship': 'Not-in-family',
            'race': 'White',
            'sex': 'Male',
            'hoursPerWeek': 60,
            'nativeCountry': 'United-States'
    }

r = requests.post('https://cdudacity.herokuapp.com/', json=data)

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())
