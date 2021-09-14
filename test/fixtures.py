import os.path

from _pytest.fixtures import fixture
from weatherest.Api import Weatherest
import yaml


@fixture
def config():
    # Quick and very, very dirty config loader
    print(f'Loading the config from: {os.path.curdir}')
    try:
        with open('../config.yaml', 'r') as config_file:
            config = yaml.load(config_file)
        return config
    except FileNotFoundError:
        return {
            'city': {
                'name': 'Mountain View',
                'region': 'CA',
                'country': 'US',
                'lat': 37.3861,
                'lon': -122.0838
            },
            'api_key': 'NoValid API Key Given!'
        }


@fixture
def city_info(config):
    yield config['city']
    print('Finished the test')
    return None


@fixture
def api_key(config):
    yield config['api_key']
    print('Finished the test')
    return None


@fixture
def data_by_city(city_info, api_key):
    eggs = Weatherest(api_key)
    result = eggs.current_weather_by_city(city_info['name'], region=city_info['region'],
                                          country=city_info['country'])
    yield result.status_code, result.json()
    print('Finished the test')
    result = None
    return None


@fixture
def everything_but_the_kitchen_sink(city_info, api_key):
    eggs = Weatherest(api_key)
    result = eggs.one_call(city_info['lat'], city_info['lon'])
    yield result.status_code, result.json()
    print('Finished the test')
    result = None
    return None
