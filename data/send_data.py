# coding: utf-8

def send_data():
    import requests
    import json
    print 'Starting send data crimes...'
    url = 'http://159.203.139.137:3000/crimes'
    #url = 'http://139.82.241.185:3000/crimes'
    file = open('data.json')

    data = json.loads(file.readline())

    for index, d in enumerate(data):
        print 'Sending crime ', index + 1
        data_dict = {'latitude': d['latitude'], 'longitude': d['longitude'], 'name': d['titulo'], 'description': d['descricao'], 'date': d['data'], 'neighbourhood': d['bairro'], 'data': d}

        requests.post(url, json=data_dict)
