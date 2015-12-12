# coding: utf-8

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import requests
import json
import geocoder

access_token = "433872469-A9Ww56J5lr5Z0eesAB0rDbvwLZ6StvXLJhdIVIQj"
access_token_secret = "AHsiJHCVLfbUUCjtQYDU1sLR387uzrMCxUnPkr1SxlWu2"
consumer_key = "08qiuPSxrwhzWUfmg7rLmW89a"
consumer_secret = "u3n61RBVXdV9hmGYrd0A8Ro22C7OrT6qxVTjAWuEuBVSTeUuse"

url = 'http://159.203.139.137:3000/crimes'


class StdOutListener(StreamListener):

    def on_data(self, data):
        data_dict = json.loads(data)
        if data_dict.get('geo'):
            if data_dict.get('place') and (data_dict['place'].get('place_type') == 'city' and data_dict['place'].get('name') == 'Rio de Janeiro'):
                print('DEU BOM', data_dict)
                latitude = data_dict['geo']['coordinates'][0]
                longitude = data_dict['geo']['coordinates'][1]
                name = data_dict.get('text')
                description = "{} - {}".format(data_dict.get('user')['name'], data_dict.get('text'))
                date = datetime.datetime.now().strftime('%Y-%m-%d')
                neighbourhood = geocoder.google([latitude, longitude], method='reverse').sublocality

                data_request = {'latitude': latitude, 'longitude': longitude, 'name': name, 'description': description, 'date': date, 'neighbourhood': neighbourhood, 'data': data_dict}
                requests.post(url, json=data_request)
            else:
                print('LOCALIZACAO NAO EH RIO ', data_dict.get('place'))
        else:
            print('NAO TEM GEO')
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['roubo', 'tiro', 'tiroteio', 'pivete', u'arrastão', 'arrastao', 'furto', 'assalto'])
