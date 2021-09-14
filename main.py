from apitherapy import api


if __name__ == '__main__':
    bee = api.Api('https://api.openweathermap.org/data/2.5', params=['q', 'appid'])\
        .add_param('q', 'Mountain View,CA')\
        .add_param('appid', '3366b579242d65b6b3dff0ce0e155d8b')\
        .query('/weather')
    print(bee.headers)
