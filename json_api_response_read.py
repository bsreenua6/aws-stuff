#Program to call an HTTP URL and parse json response
import requests
import json

n = 0

#Replace your's api URL and using loads() function to convert json response to Python dict
response = requests.get('https://api.github.com/repos/facebook/react/issues') 
data_object = json.loads(response.text)

#Display json response as pretty_json
#print(json.dumps(data_object, indent = 3))

for data in data_object:
    #print(user['id'])
    n = n +1
    print(n, data['id'], data['user']['id'])
    #print(n, data['labels'][0]['node_id'])
    
