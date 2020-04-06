import requests
from config.config import address, client_id, client_secret


def get_latitude_and_longitude_by_address():
    try:
        headers = {
            'X-NCP-APIGW-API-KEY-ID': client_id,
            'X-NCP-APIGW-API-KEY': client_secret,
        }

        params = {
            'query': address
        }

        r = requests.get('https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode',
                         headers=headers, params=params)
        data = r.json()

        latitude = data['addresses'][0]['y']
        longitude = data['addresses'][0]['x']

        print("Latitude: {}, Longitude: {}".format(latitude, longitude))

    except Exception as e:
        print("An exception occurred:", str(e))
        pass
