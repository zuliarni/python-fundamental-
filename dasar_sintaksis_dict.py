from ctypes import HRESULT

users = {
    'id' : 1,
    'name' : 'Leanne Graham',
    'age' : 22,
    'gender' : 'male',
    'job' : 'Engineer',
    'email address' : 'arni.paloma@gmail.com',
    'adress': {
        'street address' : 'kulas light.',
        'suite address' : '123 Main St.',
        'city' : 'San Jose',
        'zip code' : '12345',
        'geo': {
            'latitude' : '41.6',
            'longitude' : '-8.1'
        }

    }
}
print(users)
print(users['id'])
print(users['name'])
print(users['age'])
print(users['gender'])
print(users['job'])
print(users['email address'])
print(users['adress']['street address'])
print(users['adress']['suite address'])
print(users['adress']['city'])
print(users['adress']['zip code'])
print(users['adress']['geo']['latitude'])
print(users['adress']['geo']['longitude'])


print(users)
print(type(users))
print ('\nubah disct ke json')
import json
result = json.dumps(users)
print (type(result))
print(result)


with open('result.json', 'w') as f:
    json.dump(users, f)


