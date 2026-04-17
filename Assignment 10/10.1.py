import requests
request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request).json()
for joke in response.keys():
    if joke == 'value':
        print(response[joke])