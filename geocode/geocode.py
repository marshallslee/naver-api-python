import requests
from config.config import address, client_id, client_secret


def get_latitude_and_longitude_by_address():
    longitude, latitude = None, None
    try:
        headers = {
            'X-NCP-APIGW-API-KEY-ID': client_id,
            'X-NCP-APIGW-API-KEY': client_secret,
        }

        params = {
            'query': address
        }

        r = requests.get(
            'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode',
            headers=headers,
            params=params
        )
        data = r.json()

        latitude = data['addresses'][0]['y']
        longitude = data['addresses'][0]['x']
    except IndexError as error:
        print("Failed to calculate latitude and longitude from the given address:", error)
    finally:
        return latitude, longitude
