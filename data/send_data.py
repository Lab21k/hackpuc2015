# coding: utf-8


def send_data(data):
    import requests
    url = 'http://159.203.139.137:3000/crimes'
    #url = 'http://139.82.241.185:3000/crimes'

    for index, d in enumerate(data):
        print 'Sending crime ', index + 1
        data_dict = {'latitude': d['latitude'], 'longitude': d['longitude'], 'name': d['titulo'], 'description': d['descricao'], 'date': d['data'], 'neighbourhood': d['bairro'], 'data': d}

        requests.post(url, json=data_dict)


def send_all():
    import json

    file = open('data_all.json', 'r')

    data = json.loads(file.readline())

    init = 0
    end = len(data)
    arr = []

    print 'Starting send data crimes ({})...'.format(end)

    while init < end:
        end_index = min(init + 99, end - 1)
        arr.append((init, end_index))
        init = end_index + 1

    for a in arr:
        print 'Indexes ', a[0], a[1]
        send_data(data[a[0]:a[1]])

    file.close()
