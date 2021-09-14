from apitherapy.api import Api


class Weatherest():
    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = 'https://api.openweathermap.org/data/2.5'

    def current_weather_city(self, city, region=None, country=None):
        city_query = city + ((','+region) if region else '') + ((','+country) if country else '')
        result = Api(self._base_url, params=['q', 'appid'])\
            .add_param('appid', self._api_key)\
            .add_param('q', city_query)\
            .query('/weather')
        return result

    def current_weather_coords(self, lat, lon):
        result = Api(self._base_url, params=['lat', 'lon', 'appid'])\
            .add_param('appid', self._api_key)\
            .add_param('lat', lat) \
            .add_param('lon', lon) \
            .query('/weather')
        return result

    def current_weather_zip(self, zip, country=None):
        zip_code = zip + ((',' + country) if country else '')
        result = Api(self._base_url, params=['zip', 'appid']) \
            .add_param('appid', self._api_key) \
            .add_param('zip', zip_code) \
            .query('/weather')
        return result
